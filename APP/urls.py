from django.urls import path,include 
from APP import views
urlpatterns = [
    path('',views.StudentCreateView.as_view(),name="Home"),
    path('data-show/',views.StudentListView.as_view(),name="listView"),
    path('data-show/<int:pk>/',views.StudentUpdateView.as_view(),name="Update"),
    path('<int:pk>',views.StudentDeleteView.as_view(),name="Delete"),
    path('data-show/',views.StudentDetailView.as_view(),name="listView"),
]