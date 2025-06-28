from django.urls import path
from . import views
urlpatterns = [
   path('insert_employee/',views.insert_employee, name='insert_employee'),
   path('view_employee/', views.view_employee,  name = 'view_employee'),
   path('insert_student/',views.insert_student, name='insert_student'),
   path('view_student/', views.view_student,  name = 'view_student'), 
   path('insert_facalty/',views.insert_facalty, name='insert_facalty'),
   path('view_facalty/', views.view_facalty,  name = 'view_facalty'),                                 
   path('delete_employee/<int:pk>',views.delete_employee,
           name='delete_employee'),
   
   path('delete_facalty/<int:pk>',views.delete_facalty,name='delete_facalty'),
   path('update_employee/<int:pk>', views.update_employee,
           name = 'update_employee'),
   path('update_student/<int:pk>', views.update_student,
           name = 'update_student'),
   path('update_facalty/<int:pk>', views.update_facalty,
           name = 'update_facalty'),
]

