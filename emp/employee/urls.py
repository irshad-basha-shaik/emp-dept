from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('saveform', views.saveform, name='saveform'),
    path('edit', views.edit, name='edit'),
    path('editform', views.editform, name='editform'),
    path('delete', views.delete,name='delete'),
    path('dentry',views.dentry,name='dentry'),
    path('dmenu',views.dmenu,name='dmenu'),

]