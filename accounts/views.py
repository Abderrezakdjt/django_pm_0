from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserRegisterForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm
from django.contrib import messages


@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # لا تقم بتسجيل خروج المستخدم
            messages.success(request, 'Password changed successfully.')  # إضافة رسالة النجاح
            return render(request, 'change_password.html', {'form': form})  # إعادة عرض نفس الصفحة
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})




class RegisterView(CreateView):
    form_class = UserRegisterForm
    # success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get_success_url(self):
        login(self.request, self.object)
        return reverse_lazy('Project_list')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            # Save profile picture if uploaded
            if 'profile_picture' in request.FILES:
                user.profile_picture = request.FILES['profile_picture']
            user.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})



@login_required
def delete_account(request):
    if request.method == 'POST':
        if request.POST.get('confirm') == 'yes':
            request.user.delete()
            logout(request)
            return redirect('login')
        else:
            return render(request, 'delete_account.html', {'error': 'Confirmation failed.'})
    else:
        return render(request, 'delete_account.html')


