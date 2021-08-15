from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

from . import views
from main import views
from main.views import HomeView
from main.views import UserCreateView, UserCreateDoneTV


urlpatterns = [
    path('', views.main),
    path('/seoul', views.seoul ),
    # path('/경기', views.gg ),
    # path('main/', include('main_patterns')),
 
    # path('post/<int:pk>/', views.local_detail, name='local_detail'),
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
]

