# -*- coding: utf-8 -*-

import os
import random

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse

from django.conf import settings
from django.views.generic import TemplateView, DetailView, FormView
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.db.models import F, Value as V, Q
from django.db.models.functions import Concat

from registration.forms import RegistrationFormUniqueEmail
from utils.decorators import authenticated_redirect

from .forms import ProfileForm, AvatarForm, UserEditForm
from .models import Account


@login_required
def view_profile(request, username):
    """View Profile"""
    selected_user = Account.objects.get(username=username)

    context = {
        'selected_user': selected_user
    }

    return render(request, 'view_profile.html', context)


@login_required
def edit_profile(request):
    """Edit Profile"""
    user = request.user
    form = ProfileForm(request.POST or None, user=user)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'user': user,
        'form': form
    }

    return render(request, 'edit_profile.html', context)


@login_required
def edit_avatar(request):
    """Edit User Avatar"""
    user = request.user
    form = AvatarForm(request.POST or None, request.FILES or None, user=user)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('edit-avatar')

    context = {
        'user': user,
        'form': form
    }

    return render(request, 'avatar.html', context)


@login_required
def remove_avatar(request):
    """Remove User Avatar"""
    file_path = request.user.avatar.path

    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

    request.user.avatar = None
    request.user.save()

    return redirect('edit-avatar')


@authenticated_redirect
def auth_login(request):
    """Login Page"""
    error = None

    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))

        if user and user.is_active:
            login(request, user)
            return redirect('home')

        error = 'Could not authenticate user'

    login_style = random.randint(0, 6)
    context = {
        'error': error,
        'login_style': login_style,
    }

    return render(request, 'user_auth/login.html', context)


@csrf_exempt
@login_required
def auth_logout(request):
    """Logout"""
    logout(request)
    return redirect('home')


class UsersListView(ListView):
    model = Account
    template_name = 'user_auth/users_mgmt.html'

    def get_pagination_page(self, page=1, maxitems=settings.CLIENTS_PAGINATE_BY, filters=None,
                            sortfield=None, sortasc='1'):
        items = self.get_objects()
        items = items.annotate(display_name=Concat('first_name', V(' '), 'last_name'))
        if filters:
            ifilter = Q()
            filter_enabled = False
            for ff in filters:
                ffs = ff.split('*', 1)
                if len(ffs) > 1:
                    fname, fvalue = ffs
                    if fvalue and fname == 'clientfilter':
                        ifilter |= Q(username__icontains=fvalue)
                        ifilter |= Q(display_name__icontains=fvalue)
                        ifilter |= Q(email__icontains=fvalue)
                        filter_enabled = True
            if filter_enabled:
                items = items.filter(ifilter)
        if sortfield:
            if sortasc == '0':
                items = items.order_by("-%s" % sortfield)
            else:
                items = items.order_by("%s" % sortfield)
        paginator = Paginator(items, maxitems)
        try:
            page = int(page)
        except ValueError:
            page = 1

        try:
            items = paginator.page(page)
        except (EmptyPage, InvalidPage):
            items = paginator.page(paginator.num_pages)

        return items

    def get_context_data(self, page=1, maxitems=settings.CLIENTS_PAGINATE_BY, is_ajax=False):
        context = {}
        context['items'] = self.get_pagination_page(page, maxitems)
        context['prelast'] = context['items'].paginator.num_pages - 1
        return context

    def get_objects(self):
        return self.model.objects.all()

    def get(self, request):
        if not request.is_ajax():
            return super().get(request)
        page = request.GET.get('page', 1)
        filters = request.GET.getlist('filters[]', [])
        maxitems = request.GET.get('maxitems', settings.CLIENTS_PAGINATE_BY)
        sortfield = request.GET.get('sort', 'id')
        sortasc = str(request.GET.get('asc', '1'))
        items = self.get_pagination_page(page, maxitems, filters, sortfield, sortasc)
        prelast = items.paginator.num_pages - 1
        return render_to_response('user_auth/user_list.html', {'items': items, 'prelast': prelast})


class UserCreateUpdateView(SingleObjectTemplateResponseMixin, ModelFormMixin, ProcessFormView):
    model = Account

    form_class = UserEditForm
    # template_name = 'user_auth/registration/form.html'
    template_name = 'user_auth/user_edit_form.html'

    def get_object(self, queryset=None):
        try:
            retval = super().get_object(queryset)
            return retval
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('users_list')
