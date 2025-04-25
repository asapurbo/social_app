from uuid import UUID
import uuid
from django.shortcuts import redirect, render
from account.models import SignUp
from utils.get_public_id_from_url import get_public_id_from_url
import cloudinary
import cloudinary.uploader
# from cloudinary.utils import cloudinary_url
from decouple import config

def will_be_editing(request, id):
    # check this user is editing his own profile
    if request.user.id != int(id):
        return redirect('account:profile')
    user = request.user
    context = {
        'title': '📝Edit Profile',
        'user_info': None
    }

    if request.method == 'POST':
# that feature implemented in the future
        # username = request.POST.get('username', None)
        # email = request.POST.get('email', None)

        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)


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

            public_id = get_public_id_from_url(request.user.signup.profile_pic)

            if public_id is None:
                public_id = uuid.uuid4().hex[:18]

            overwrite = False
            if public_id:
                cloudinary.uploader.destroy(public_id)
                overwrite = True

            image = request.FILES.get('image', None)

            if image:
                size = (128, 128)
                # profile_pic = image_fit(image, size)
                # Upload an image
                upload_result = cloudinary.uploader.upload(
                    image,
                    folder="profile_pic",
                    public_id=public_id,
                    overwrite=overwrite,
                    transformation=[
                        {"width": size[0], "height": size[1], "crop": "auto", "gravity": "auto"},
                        {"fetch_format": "auto", "quality": "auto"}
                    ]
                )
                profile_pic = upload_result["secure_url"]

# that feature implemented in the future
        # user.username = username
        # user.email = email
        # user.save()

        signUpData = SignUp.objects.filter(user=user).first()

        if signUpData:
            signUpData.first_name = first_name
            signUpData.last_name = last_name
            if profile_pic:
                signUpData.profile_pic = profile_pic
            signUpData.save()


        return redirect('account:profile')

    user_info = SignUp.objects.filter(user=user).first()
    if user_info:
        context['user_info'] = user_info

    return render(request, 'accounts/edit_profile.html', context=context)
