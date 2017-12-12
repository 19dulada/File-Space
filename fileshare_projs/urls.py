f"""Defines URL patterns for fileshare_projs."""
from django.conf.urls import url
from . import views
urlpatterns = [
# Home page
url(r'^$',views.index, name='index'),
# Upload page
url(r'^upload/$',views.upload, name='upload'),
# Download page
url(r'^download/$', views.download, name='download'),
# Manage Files page
url(r'manage_files/', views.manage_files, name='manage_files'),
# Troubleshooting page
url(r'^troubleshooting/$', views.troubleshooting, name='troubleshooting'),
# ??? page
url(r'^egg/$', views.egg, name='egg'),

]
