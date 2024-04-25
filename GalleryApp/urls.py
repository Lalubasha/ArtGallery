from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import DjangoDetail


urlpatterns = [
    path('', views.AllPostsView.as_view(), name='home'),
    path('django/', views.DjangoList.as_view(), name='django'),
    
    path('create_post/', views.create_post, name='create_post'),
    path('django/<int:pk>/', DjangoDetail.as_view(), name='django_detail'),

  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)