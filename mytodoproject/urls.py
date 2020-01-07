from django.contrib import admin
from django.urls import path

from todo.views import home, delete, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('delete/<int:id>', delete),
    path('update/<int:id>', update),
	
]
