from django.contrib import admin

# Register your models here.
from .models import EmployeeModel
admin.site.register(EmployeeModel)
from .models import StudentModel
admin.site.register(StudentModel)
from .models import FacaltyModel
admin.site.register(FacaltyModel)
