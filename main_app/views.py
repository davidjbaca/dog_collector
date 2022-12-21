from django.shortcuts import render

# Add the following import
from django.http import HttpResponse


class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

# This the array, we are injecting into the template
dogs = [
  Dog('Kona', 'German Shepard', 'spoiled lovable brat', 5),
  Dog('Bud', 'Golden Retriver', 'Old reliable', 7),
  Dog('Cheese', 'Pittbull', 'All bark no bite', 2),
  Dog('Cooper', 'Labrador', 'Young Blood', 0)
  
]




# Define the home view
def home(request):
	return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})