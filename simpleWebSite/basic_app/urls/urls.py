from django.urls import path
from basic_app.views import connect4_view
from basic_app.views import cv_view
from basic_app.views import login_view
from basic_app.views import register_view
from basic_app.views import xo_view





urlpatterns = [
   path('connect4_page/', connect4_view.connect4, name='connect4'),
   path('cv_page/', cv_view.cv, name="cv"),
   path('login_page/', login_view.user_login, name="user_login"),
   path('register_page/', register_view.register, name="register"),
   path('xo_page/', xo_view.xo, name="xo"),
]