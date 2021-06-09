from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_FIR_view,name='FIR_FORM'),
    path('FIRInfo/',views.FIR_registerd,name='FIRInfo'),
    path('search/', views.post_search, name='post_search'),
    path('statistics/',views.chart_select_view,name='statistics'),
]