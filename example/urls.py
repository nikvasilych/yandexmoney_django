# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from .app.views import OrderPage

admin.autodiscover()

urlpatterns = ['',
                       re_path(r'payment-form/$', OrderPage.as_view(), name='payment_form'),
                       re_path(r'fail-payment/$', TemplateView.as_view(template_name='fail.html'), name='payment_fail'),
                       re_path(r'success-payment/$', TemplateView.as_view(template_name='success.html'), name='payment_success'),
                       re_path(r'^admin/', include(admin.site.urls)),
                       re_path(r'^yandex-money/', include('yandex_money.urls')),]

urlpatterns += staticfiles_urlpatterns()