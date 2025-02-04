from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('list/', views.TeacherListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.TeacherDetailView.as_view(), name='detail'),
    path('create/', views.TeacherCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TeacherDeleteView.as_view(), name='delete'),
]
