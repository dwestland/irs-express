from django import forms
from django.utils.translation import ugettext_lazy as _

from utils.forms import ImprovedForm
from .models import Account


class ProfileForm(forms.Form):
    """User Profile Form"""
    email = forms.EmailField()
    first_name = forms.CharField(max_length=40, required=False)
    last_name = forms.CharField(max_length=40, required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self._build_initial()
        super(ProfileForm, self).__init__(*args, **kwargs)

    def _build_initial(self):
        for field in self.base_fields:
            if field in dir(self.user):
                self.base_fields[field].initial = getattr(self.user, field)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email != self.user.email and Account.objects.get(email=email):
            raise forms.ValidationError('That email already exists.')

        return email

    def save(self):
        for field, value in self.cleaned_data.items():
            if field in self.base_fields:
                setattr(self.user, field, value)

        self.user.save()
        return self.user


class AvatarForm(forms.ModelForm):
    """Avatar Form"""
    class Meta:
        model = Account
        fields = ('avatar',)

    def __init__(self, *args, **kwargs):
        """Intialize Form"""
        self.user = kwargs.pop('user')

        # Get Avatar Upload
        if args[1] is not None:
            self.avatar = args[1]['avatar']

        super(AvatarForm, self).__init__(*args, **kwargs)

    def save(self, commit=False):
        profile = super(AvatarForm, self).save(commit)

        self.user.avatar = self.avatar
        self.user.save()

        return self.user


class UserEditForm(ImprovedForm, forms.ModelForm):

    class Meta:
        model = Account
        exclude = ('avatar', 'last_login')
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'is_admin', 'is_active')

    required_css_class = 'required'

    username = forms.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=30,
        label=_("Username"),
        error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    email = forms.EmailField(label=_("E-mail"))
    password = forms.CharField(widget=forms.PasswordInput, label=_("Password"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print(self.data)
        if self.instance.pk:  # and not self.data:
            self.fields['password'].required = False
            self.fields['password'].widget.attrs['placeholder'] = ""  # dirty hack
            self.fields['password'].initial = ""
            self.fields['password'].help_text = "Leave empty if you do not want to change"
            self.initial['password'] = ""

    def clean_password(self):
        if not self.cleaned_data['password']:
            if self.instance.pk:
                return self.instance.password
            raise forms.ValidationError(_("Password is required!"))
        return self.cleaned_data['password']

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.

        """
        if not self.instance.pk:
            existing = self._meta.model.objects.filter(username__iexact=self.cleaned_data['username'])
        else:
            existing = self._meta.model.objects.filter(username__iexact=self.cleaned_data['username']).\
                exclude(pk=self.instance.pk)
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        return self.cleaned_data['username']
