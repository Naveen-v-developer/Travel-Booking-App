from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .forms import UserRegisterForm, UserUpdateForm


# ✅ Register View
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            messages.success(request, '🎉 Registration successful! Welcome aboard.')
            return redirect('travels:travel_list')  # Redirect to Travel Options
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# ✅ Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'✅ Welcome back, {user.username}!')
            # Redirect to "next" if present, otherwise Travel Options
            next_url = request.POST.get('next') or request.GET.get('next')
            return redirect(next_url or reverse('travels:travel_list'))
        else:
            messages.error(request, "❌ Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


# ✅ Logout View
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "👋 You’ve been logged out successfully.")
    return redirect('index')  # Go back to Home page


# ✅ Profile View
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Profile updated successfully.')
            return redirect('users:profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'users/profile.html', {'form': form})
