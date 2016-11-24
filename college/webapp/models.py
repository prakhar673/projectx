from django.db import models
from datetime import datetime 

class Colleges(models.Model):
	college_id=models.AutoField(primary_key=True)
	college_name=models.CharField(max_length=128,unique=True)
	college_address=models.CharField(max_length=128, default='', unique=False)
	inception_year=models.DateTimeField(default=datetime.now(), blank=True)
	co_website=models.CharField(max_length=128, default='', unique=True)
	c_ownership_type=models.CharField(max_length=128, unique=False, default='')
	c_area=models.IntegerField(default=0)

class Stream_Master(models.Model):
	college_id=models.AutoField(primary_key=True)
	stream_id=models.IntegerField(default=0)
	stream_name=models.CharField(max_length=128, default='', unique=False)
	




