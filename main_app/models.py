from django.db import models
from django.urls import reverse

from datetime import date


class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Dog(models.Model):

	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	age = models.IntegerField()
	toys = models.ManyToManyField(Toy)


	def get_absolute_url(self):

		return reverse('detail', kwargs={'dog_id': self.id})

	def fed_for_today(self):

		return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)


class Feeding(models.Model):
	date = models.DateField('Feeding date')
	meal = models.CharField(
		max_length=1,
		
		choices=MEALS, 
		default=MEALS[0][0])

	# create a cat_id FK (Cat is our model)
	dog = models.ForeignKey(Dog, on_delete=models.CASCADE) # <- If you delete cat, delete all the feeding associated with the cat as well
	
	def __str__(self):

		return f"{self.get_meal_display()} on {self.date}"

	class Meta:
		ordering = ['-date']