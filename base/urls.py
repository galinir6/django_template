"""
app

"""
from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('books',views.books ),
    path('books/<int:id>',views.books),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
