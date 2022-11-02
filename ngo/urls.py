from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Index, name='index'),
    path('about/', About, name='about'),
    path('member/register/', memberRegister, name='member_register')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)