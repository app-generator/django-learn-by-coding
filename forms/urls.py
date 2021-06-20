# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from forms import views

urlpatterns = [

    # The home page
    path('forms/', views.index, name='home'),
]
