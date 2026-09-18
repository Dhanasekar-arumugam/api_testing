from django.db import models

# Create your models here.

class Employee(models.Model):

    employee_id = models.IntegerField(primary_key=True)

    first_name = models.CharField(max_length=100, null=True, blank=True)

    last_name = models.CharField(max_length=100, null=True, blank=True)

    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    manager_id = models.IntegerField(null=True, blank=True)

    hire_date = models.DateField()

    department_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)