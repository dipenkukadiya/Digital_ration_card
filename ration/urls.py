from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = 'Digtal Ration Card Admin'
admin.site.site_title = 'Digtal Ration Card Admin'
admin.site.index_title = 'Digtal Ration Card Admin'

urlpatterns = [
                path('',views.index,name ='index'),
                path('register_submit/',views.register_submit,name ='register_submit'),  
                path('login_submit/',views.login_submit,name ='login_submit'),  
                path('home/',views.home,name ='home'),
                path('ration/',views.ration,name ='ration'),
                path('ration_record/',views.ration_record, name ='ration_record'),
                path('ration_submit/',views.ration_submit,name='ration_submit'),
                path('profile/',views.profile,name ='profile'),
                path('feedback/',views.feedback,name ='feedback'),
                path('feedback_sub/',views.feedback_sub,name='feedback_sub'),
                path('validee/',views.validee,name='validee'),
                path('tokon/',views.user_tokon,name='tokon'),
                path('tokon_home/',views.tokon_home,name='tokon_home'),
                path('update_tok/', views.update_tok, name='update_tok'),
                path('take_tok/', views.take_tok, name='take_tok'),
                path('ration_next/', views.ration_next, name='ration_next'),
                path('deal_home/', views.deal_home, name='deal_home'),
               

            ]




