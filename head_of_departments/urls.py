from django.urls import path
from . import views

app_name = 'head_of_departments'

urlpatterns = [
    path('list/', views.HeadOfDepartmentListView.as_view(), name='list'),
    path('create/', views.HeadOfDepartmentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.HeadOfDepartmentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.HeadOfDepartmentDeleteView.as_view(), name='delete'),
]
