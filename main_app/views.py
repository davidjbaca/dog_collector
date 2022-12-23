from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from django.http import HttpResponse

from .models import Dog

class DogUpdate(UpdateView):
  model = Dog
  # disallow the update of the name
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  # want to define the success_url, since when we delete something we can't redirect to the detail page
  success_url = '/dogs/' 

class DogCreate(CreateView):
  model = Dog 
  
  fields = '__all__' 



# Define the home view
def home(request):
	return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
  # use our model Cat (Capital cat) to retrieve whatever row
  # from our db the cat_id matches
  dog = Dog.objects.get(id=dog_id)
  #cats/detail.html <-- refers to template
  return render(request,'dogs/detail.html', {'dog': dog})
