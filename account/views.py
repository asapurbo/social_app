from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from account.models import ExtraInfo, SignUp
from controllers.accounts.change_password import password
from controllers.accounts.register_view import register
from controllers.accounts.verify_email import email_verify
from utils.send_to_mail import send_to_mail
from controllers.accounts.login_view import _login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from controllers.accounts.edit_profile import will_be_editing
from django.contrib.auth.models import User
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
import json

# Create your views here.

# this is the register view
# Define a function called register_view that takes in a request as a parameter
def register_view(request):
    if request.user.is_authenticated:
        return redirect('social:index')
    # Call the register function and pass in the request as an argument
    # views.py
    return register(request)


# email verification view
def verify_email(request):
    if request.user.is_authenticated:
        return redirect('social:index')

    if request.session.get('send_email', None):
        send_to_mail(request)
        request.session['send_email'] = False
    return email_verify(request)

# Define a function called resend_email that takes in a request as a parameter
def resend_email(request):
    if request.user.is_authenticated:
        return redirect('social:index')

    request.session['send_email'] = True
    return redirect('account:verify_email')

# Define a function called login_view that takes in a request as a parameter
def login_view(request):
    if request.user.is_authenticated:
        return redirect('social:index')

    return _login(request)

@login_required
def logout_view(request):
    logout(request)
    return redirect('account:login')

@login_required
def profile_view(request):
    context = {
        'title': '👤Profile',
        'info': None
    }
    data = SignUp.objects.filter(user=request.user).first()
    context['info'] = data

    return render(request, 'accounts/profile.html', context=context)

@login_required
def edit_profile(request, id):
    return will_be_editing(request, id)

@login_required
def change_password(request, id):
    return password(request, id)

@method_decorator(csrf_protect, name='dispatch')
class EditBio(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            bio = data.get('bio', None)

            exInfo = ExtraInfo.objects.filter(user=request.user).first()

            if exInfo:
                exInfo.bio = bio
                exInfo.save()
            else:
                exInfo = ExtraInfo.objects.create(user=request.user, bio=bio)


            return JsonResponse({"success": 'Bio updated successfully'}, status=200)


        except json.JSONDecodeError:
            return JsonResponse({"error": 'Something went wrong'}, status=400)













