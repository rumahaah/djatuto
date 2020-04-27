from django.db import models

# Create your models here.
class Abc(models.Model):
	aaa = models.CharField(max_length=200)
	bbb = models.CharField(max_length=200)
	flagcalc = models.BooleanField(default=True)
	# votes = models.IntegerField(default=0)