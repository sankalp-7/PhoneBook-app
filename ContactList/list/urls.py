from django.urls import path
from . import views
app_name="list"
urlpatterns=[ 
    path('',views.home,name='home'),
    path('add/',views.formview.as_view(),name='form'),
    path('view/',views.ViewList,name='view'),
    path('update/<int:pk>',views.UpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.DeleteView.as_view(),name='delete'),
]