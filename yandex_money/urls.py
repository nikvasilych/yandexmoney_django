# -*- coding: utf-8 -*-

from django.urls import path, re_path

from .views import NoticeFormView
from .views import CheckOrderFormView


urlpatterns = [
    re_path(r'^check/', CheckOrderFormView.as_view(), name='yandex_money_check'),
    re_path(r'^aviso/', NoticeFormView.as_view(), name='yandex_money_notice'),
]

