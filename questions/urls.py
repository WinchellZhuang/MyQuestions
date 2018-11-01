from django.urls import path
from django.conf.urls import url
from django.urls import include
from questions import views

urlpatterns = [
    # --------------主框架和首页-----------------
    url(r'^index', views.index),
    url(r'^first', views.first),
    url(r'^qst_record',views.qst_record),
    # --------------用户管理-----------------
    url(r'^userManager$', views.userManager),
    url(r'^user_save$', views.user_save),
    url(r'^user_list$', views.user_list),
    url(r'^user_update$', views.user_update),
    url(r'^user_del$', views.user_del),
    # --------------科目管理-----------------
    url(r'^subject$', views.subjectManager),
    url(r'^subject_save$', views.subject_save),
    url(r'^subject_list$', views.subject_list),
    url(r'^subject_update$', views.subject_update),
    url(r'^subject_del$', views.subject_del),
    # --------------问题来源-----------------
    url(r'^qstSource', views.qstManager),
    url(r'^qst_save$', views.qst_save),
    url(r'^qst_list$', views.qst_list),
    url(r'^qst_update$', views.qst_update),
    url(r'^qst_del$', views.qst_del),
    # --------------解决等级-----------------
    url(r'^solveLevel', views.solveLevel),
    url(r'^sl_save$', views.sl_save),
    url(r'^sl_list$', views.sl_list),
    url(r'^sl_update$', views.sl_update),
    url(r'^sl_del$', views.sl_del),
]
