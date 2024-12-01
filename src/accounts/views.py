from itertools import product

from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Model, Q
from django.http import HttpResponse
from django.shortcuts import render  # NOQA
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, ListView, RedirectView
from oauthlib.uri_validate import query

from accounts.forms import UserRegistrationForm
from accounts.models import UserProfile
from accounts.services.emails import send_registration_email
from accounts.utils.token_generators import TokenGenerator
from products.models import Basket, Product


class UserLogin(LoginView):
    pass


class UserLogout(LogoutView):
    next_page = reverse_lazy("index")


class UserRegistration(CreateView):
    template_name = "registration/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()

        send_registration_email(user_instance=self.object, request=self.request)

        return super().form_valid(form)


class UserActivationView(RedirectView):
    url = reverse_lazy("index")

    def get(self, request, uuid64, token, *args, **kwargs):
        try:
            pk = force_str(urlsafe_base64_decode(uuid64))
            current_user = get_user_model().objects.get(pk=pk)
        except (get_user_model().DoesNotExist, ValueError, TypeError):
            return HttpResponse("Wrong data!!!")

        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            UserProfile(user=current_user).save()
            current_user.save()

            login(request, current_user)

            return super().get(request, *args, **kwargs)

        return HttpResponse("Wrong data!!!")


class BasketView(ListView):
    model = Basket
    template_name = "user_basket.html"

    def get_queryset(self):
        product_id  = self.request.GET.get("p")
        user = self.request.user
        object_list = Basket.objects.get(user=user)
        if (product_id is not None):
            product = Product.objects.get(id=product_id)
            object_list.products.remove(product)

        return object_list
