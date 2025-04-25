import uuid
import cloudinary
from django.shortcuts import render, redirect

import cloudinary
import cloudinary.uploader
# from cloudinary.utils import cloudinary_url
from decouple import config
from social.models import Post

# Create your views here.
def index(request):
    context = {
        'title': 'Home Page',
    }

    if request.method == 'POST':
        cloudinary.config(
            cloud_name = config('CLOUD_NAME'),
            api_key = config('API_KEY'),
            api_secret = config('API_SECRET'),
            secure=True,
        )

        content = request.POST.get('content', None)
        image = request.FILES.get('image', None)

        content_image = None

        print('image', image)
        print('data', request.POST)
        if image:
            size = (280, 146)
            upload_result = cloudinary.uploader.upload(
                image,
                folder="content_img",
                public_id=uuid.uuid4().hex[:20],
                transformation=[
                    {"width": size[0], "height": size[1], "crop": "auto", "gravity": "auto"},
                    {"fetch_format": "auto", "quality": "auto"}
                ]
            )
            content_image = upload_result["secure_url"]

        post = Post.objects.create(user=request.user ,content=content, image=content_image)

        post.save()
        return redirect('account:profile')

    return render(request, 'social/index.html', context=context)

