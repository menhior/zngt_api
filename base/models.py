from django.db import models

# Create your models here.

class Listing(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	title2 = models.CharField(max_length=100, null=True, blank=True)
	price = models.CharField(max_length=30, null=True, blank=True)
	currency = models.CharField(max_length=10, null=True, blank=True)
	sale_or_rent = models.CharField(max_length=20, null=True, blank=True)
	size_of_appartment = models.CharField(max_length=10, null=True, blank=True)
	number_or_rooms = models.CharField(max_length=10, null=True, blank=True)
	features = models.CharField(max_length=200, null=True, blank=True)
	other_features = models.CharField(max_length=200, null=True, blank=True)
	realtor_company_name = models.CharField(max_length=15, null=True, blank=True)
	date_published = models.CharField(max_length=20, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)