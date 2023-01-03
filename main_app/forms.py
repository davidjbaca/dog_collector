from django.forms import ModelForm
from .models import Feeding

class FeedingForm(ModelForm):
	# meta class, this instructions for the class
	class Meta:
		model = Feeding
		fields = ['date', 'meal']