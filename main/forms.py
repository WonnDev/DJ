from django import forms
from .models import contactForm, upForm, Food
from rest_framework import serializers, generics

class CreateNewList(forms.Form):
	name = forms.CharField(label="Name", max_length=200)
	check = forms.BooleanField(required=False)

class contact_Form(forms.ModelForm):
	class Meta:
		model = contactForm
		fields = ['username', 'email']

class contact__Form(forms.Form):
	username = forms.CharField(max_length = 30)
	email = forms.EmailField()
	body = forms.CharField(widget = forms.Textarea)

class uploadfileform(forms.ModelForm):
	class Meta:
		model = upForm
		fields = ['title', 'image', 'body']

class uploadfilefromform(forms.Form):
	title = forms.CharField(max_length=255)
	imageform = forms.FileField()
	body = forms.CharField(widget=forms.Textarea)

# class uploadMulti(forms.Form):
# 	image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

#API
class FoodSerializer(serializers.Serializer):
	class Meta:
		models = Food
		fields = ['name','description']
class postFood(generics.ListCreateAPIView):
	class Meta:
		model = Food
		fields = ('name','description')

