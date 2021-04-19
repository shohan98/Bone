from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

from Boneadmin.models import User
from .models import BoneUser


class UserSignUpForm(UserCreationForm):
    email = forms.CharField(required=True)
    user_ip = forms.CharField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.email = self.cleaned_data.get('email')
        user.save()
        admin = BoneUser.objects.create(user=user)
        admin.save()
        return admin
#        fields = '__all__'
