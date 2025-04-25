from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

def password(request, id):
    context = {
        'title': '🔑Change Password',
        'error': None,
    }

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = get_object_or_404(User, id=id)

        if not (user.check_password(old_password)):
            context['error'] = 'Old password is incorrect'
            return render(request, 'accounts/change_password.html', context=context)

        if new_password != confirm_password:
            context['error'] = 'New password and confirm password do not match'
            return render(request, 'accounts/change_password.html', context=context)

        user.set_password(new_password)
        user.save()

        # update the session with the new password
        update_session_auth_hash(request, user)

        return redirect('account:profile')

    return render(request, 'accounts/change_password.html', context=context)
