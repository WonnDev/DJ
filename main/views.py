from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, contactForm, postForm, upForm, Category, Food
from .forms import CreateNewList, contact_Form, contact__Form, uploadfileform, uploadfilefromform, FoodSerializer, postFood #uploadMulti, 
from django.core.paginator import Paginator
from django.views.generic.edit import FormView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.


def index(response, id):
	# return HttpResponse("<h1>Welcome to Django</h1>")
	ls = ToDoList.objects.get(id=id)

	# {"save":["save"], "c1":["clicked"]}
	if response.method == "POST":
		print(response.POST)
		if response.POST.get("save"):
			for item in ls.item_set.all():
				if response.POST.get("c" + str(item.id)) == "clicked":
					item.complete = True
				else:
					item.complete = False

				item.save()


		elif response.POST.get("newItem"):
			txt = response.POST.get("new")

			if len(txt) > 2:
				ls.item_set.create(text=txt, complete=False)
			else:
				print("invalid")


	return render(response, "main/list.html", {"ls":ls})

# def test(response, name):
# 	ls = ToDoList.objects.get(name=name)
# 	item = ls.item_set.get(id=1)
# 	return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))

# def home(response):
# 	# return render(response, "main/home.html", {})
# 	pass

def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()

		return HttpResponseRedirect("/%i" %t.id)
	else:
		form = CreateNewList()
		return render(response, "main/create.html", {"form":form})

def login(request):
	return render(request, 'main/login.html', {})
# def contact(request):
# 	cf = contact__Form
# 	return render(request, 'main/pagecontact.html', {'cf':cf})
def home_login(request):
	category = Category.objects.all()
	return render(request, 'main/pagehome.html', {'category':category})
def contact(request):
	context = {'cf': contact_Form}
	return render(request, 'main/pagecontact.html',context)
def product(request):
	UF = uploadfileform
	return render(request, 'main/pageproduct.html', {'UF':UF})
def showlist(request):
	pf = postForm.objects.all()
	uf = upForm.objects.all()
	paginator = Paginator(uf, 1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'main/pageabout.html',{'pf':pf,'uf':uf,'page_obj':page_obj})


def getContact(request):
	if request.method == "POST":
		cf = contact_Form(request.POST)
		if cf.is_valid():
			cf.save()
			return HttpResponse("Save Data Successful with Models")
	else:
		return HttpResponse('not POST')

def saveContact(request):
	if request.method == "POST":
		cf = contact__Form(request.POST)
		if cf.is_valid():
			saveCF = contactForm(username = cf.cleaned_data['username'],
				email = cf.cleaned_data['email'],
				body = cf.cleaned_data['body'])
			saveCF.save()
			return HttpResponse('Save Successful from Form to Data without Models')

def getFile(request):
	form = uploadfileform(request.POST, request.FILES)
	if form.is_valid:
		form.save()
		return HttpResponse('save image with models')
	# form = uploadfilefromform(request.POST, request.FILES)
	# if form.is_valid:
	# 	form = upForm(image=request.FILES['imageform'])
	# 	form.save()
	# 	return HttpResponse('save image with form')

#CREATE views api
@api_view(['GET'])
def getFood(request):
	food = Food.objects.all()
	serializer = FoodSerializer(food, many=True)
	return Response(food.values_list('name', flat=True))
	# print(serializer.data)
	# return Response(serializer.data)

@api_view(['POST'])
def postFood(request):
	# serializer = FoodSerializer(data=request.data)
	# if serializer.is_valid():
	# 	serializer.save()
	# return Response(serializer.data)
	
	# if request.method == "POST":
	# 	food = Food.objects.all()
		# pF = postFood(data=request.data)
	# 	if pF.is_valid():
	# 		pF.save()
	# 		return Response(food.values_list('name'))
	# else:
	# 	return HttpResponse('not POST')

	serializer = postFood(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)



