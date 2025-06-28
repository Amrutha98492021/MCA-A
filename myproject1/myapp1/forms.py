from django.forms import fields  
from .models import EmployeeModel  
from django import forms  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = EmployeeModel  # To specify the model to be used to create form
        fields = '__all__'  
from .models import StudentModel  
from django import forms  
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = StudentModel  # To specify the model to be used to create form
        fields = '__all__' 
from .models import FacaltyModel  
from django import forms   
class FacaltyForm(forms.ModelForm):  
    class Meta:  
        model = FacaltyModel  # To specify the model to be used to create form
        fields = '__all__' 