from django.urls import path
from app import views

urlpatterns = [
    path('add/', views.Add.as_view(), name='add'),
    path('double/', views.Double.as_view(), name='double'),
    path('multthree/', views.Mult_three.as_view(), name='multthree'),
    path('earnings/', views.Earnings.as_view(), name='earnings'),
    path('both/', views.Both.as_view(), name='both'),
    path('walk-or-drive/', views.WalkOrDrive.as_view(), name='walk-or-drive'),
]
