from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class MomentsToDocument(models.Model):
	title_Of_Moment = models.CharField(max_length = 255)
	created_by = models.ForeignKey(User,on_delete=models.CASCADE)
	date_Of_Moment = models.CharField(max_length = 255)
	body_Text_Of_Moment = models.TextField()

	def __str__(self):
		return self.title_Of_Moment + ' | ' + str(self.created_by) + " | " + self.date_Of_Moment

	def get_absolute_url(self):
		return reverse('home')

# Create your models here.
