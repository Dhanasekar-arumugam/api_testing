from django.urls import path

from app1.views import EmployeeDetailView, EmployeeListCreateView

urlpatterns = [
    path('employee/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
]