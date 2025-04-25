import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from account.models import SignUp
from utils import image_fit, send_to_mail
from django.db.models import Q
import cloudinary
import cloudinary.uploader
# from cloudinary.utils import cloudinary_url
from decouple import config

def register(request):
    context = {
        'title': 'Sign Up',
        'error': None
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']

        # if username and password and email and password and confirm_password:
        if not (username and password and email and password and confirm_password):
            context['error'] = 'Please fill all the fields'
            return render(request, 'accounts/signup.html', context=context)

        # if password != confirm_password
        if password != confirm_password:
            context['error'] = 'Password does not match'
            return render(request, 'accounts/signup.html', context=context)

        # user has been exists
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            context['error'] = 'User already exists'
            return render(request, 'accounts/signup.html', context=context)

        # email validation
        try:
            validate_email(email)
        except ValidationError:
            context['error'] = 'Invalid email'
            return render(request, 'accounts/signup.html', context=context)

        # create user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        profile_pic = None
        # create signup data
        if 'image' in request.FILES:
            # Configuration
            cloudinary.config(
                cloud_name = config('CLOUD_NAME'),
                api_key = config('API_KEY'),
                api_secret = config('API_SECRET'),
                secure=True,
            )
            image = request.FILES.get('image', None)

            if image:
                size = (128, 128)
                upload_result = cloudinary.uploader.upload(
                    image,
                    folder="profile_pic",
                    public_id=uuid.uuid4().hex[:18],
                    transformation=[
                        {"width": size[0], "height": size[1], "crop": "auto", "gravity": "auto"},
                        {"fetch_format": "auto", "quality": "auto"}
                    ]
                )
                profile_pic = upload_result["secure_url"]

        # create Sign-up data
        signup_data = SignUp.objects.create(user=user, profile_pic=profile_pic)
        signup_data.save()

        # save session
        request.session['email'] = email
        request.session['signup_id'] = signup_data.pk
        send_to_mail.send_to_mail(request)

        return redirect('account:verify_email')

    return render(request, 'accounts/signup.html', context=context)
