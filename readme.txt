Django:
+ StartProject: django-admin startproject <namefolder>
+ database API control: (<\namefolder>) python manage.py startapp <namefolder> (create)
+ Change code (data field)*(/models):
	+ python manage.py makemigrations *main (create/build table data)
	+ Python manage.py migrate (save/apply table data)
    (+) then Admin.py add (from .models import <name>), admin.site.register(name)
+ Access:
	+ python manage.py shell:
		+ from main.models import ToDoList:
			+ t = ToDoList(name=“List”), t.save()
			+ ToDoList.objects.all() : <QuerySet [<ToDoList: List>]> (total)
			+ ToDoList.objects.get(id=1) :<ToDoList: List> (been)
			+ t.item_set.all() : <QuerySet [ ]> (empty)
			+ t.item_set.create(text="Go to Market", complete=False)
			+ t.item_set.all( ) : <QuerySet [<Item: Go to Market>]> (been)
			+ del_objects = t.get(id=2), del_objects.delete( ) (delete list with id =2)
		+ //:
			+ t.filter(name__startswith="W”) (name)
			+ t1 = ToDoList(name="First”), t1.save( ) (add new list)
			+ t = ToDoList.objects, t.all() (<QuerySet [<ToDoList: List>,<ToDoList: First>)
			+ quit( )
	+ create superuser:
		+ python manage.py createsuperuser:
			+ name, email, pass, repass,y
		+ from django.contrib.auth.models import User:
			+ user=User.objects.create_user(‘admin', password=‘123’)
			+ user.is_supperuser=True
			+ user.is_staff=True
			+ user.save()