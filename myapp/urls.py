
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup_page, name="signup"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('covid/', views.covid_info, name="covid"),
    path('dashboard/', views.create_account, name="create_account"),
    path('loginUser/', views.login, name='loginUser'),
    path('results/', views.search_result, name="results"),
    path('results/singleProperty/', views.single_property, name="single_property"),
    path('addProperty/', views.add_property, name="add_property"),
    path('saveProperty/', views.save_property, name="save_property"),
]