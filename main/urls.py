from django.urls import path

from . import views

urlpatterns = [
	# path("", views.index, name="index"),
	# path("<str:name>", views.test, name="Test"),
	# path("", views.home, name="Home"),
	path("<int:id>", views.index, name="index"),
	path("create/", views.create, name="create"),
	path('login/', views.login, name="login"),
	path('login/pagecontact/', views.contact, name="contact"),
	path('login/pageproduct/', views.product, name="product"),
	path('login/pageshowlist/', views.showlist, name="showlist"),
	path('getContact/', views.getContact, name="getContact"),
	path('saveContact/', views.saveContact, name="saveContact"),
	path('login/pagehome/', views.home_login, name="homeLogin"),
	#
	path('getFile/', views.getFile, name="getFile"),
	#API
	path('getFood/', views.getFood),
	# path('getFood', views.getFood.as_view(),{}),
	path('postFood/', views.postFood),
]