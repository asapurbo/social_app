from django.contrib import admin
from django.urls import path, include
from social_project.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('account/', include('account.urls')),
    path('home/', include('social.urls')),
]
