# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app_pdf     import views

urlpatterns = [

    # The home page
    path('pdf/'     , views.index    ),
    path('pdf_dw/'  , views.pdf_dw   ),
    path('pdf_img/' , views.pdf_img  )
]
