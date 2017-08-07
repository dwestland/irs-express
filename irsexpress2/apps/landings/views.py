from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    """
    Home View
    """
    if request.user.is_authenticated:
        return redirect('clients_list')
        # return redirect('dashboard')
    return render(request, 'landings/home.html', {})


@login_required
def dashboard(request):
    """
    Dashboard View
    """
    return render(request, 'landings/dashboard.html', {})
