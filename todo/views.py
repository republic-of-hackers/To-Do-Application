from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .models import Todo

def home(request):
	if request.method == "POST":
		todo_des = request.POST.get('todo_inp',None)
		if request.POST['opt'] == "None":
			obj = Todo()
			obj.todo_des = todo_des
			obj.save()
		else:
			obj_id = request.POST['opt']
			obj = Todo.objects.filter(id=obj_id).first()
			obj.todo_des = todo_des
			obj.save()
		qs = Todo.objects.all()
		context = { 'qs' : qs } 
		return render(request, 'todo.html', context)
	qs = Todo.objects.all()
	if qs.count() == 0:
		context = {}
	else:
		context = { 'qs' : qs }
	return render(request, 'todo.html', context)

def update(request, id):
	return HttpResponseRedirect("/")

def delete(request, id):
	Todo.objects.filter(id=id).delete()
	return HttpResponseRedirect("/")

