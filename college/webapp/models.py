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
	college_id=models.IntegerField(primary_key=True)
	stream_id=models.IntegerField(primary_key=True, default=0)
	stream_name=models.CharField(max_length=128, default='', unique=False)

class Stream_Data(models.Model):
	college_id=models.IntegerField(primary_key=True)
	stream_id=models.IntegerField(default=0)
	year=models.DateTimeField(default=datetime.now(), blank=True)
	opening_rank=models.IntegerField(default=0)
	closing_rank=models.IntegerField(default=0)
	faculty_number=models.IntegerField(default=0)
	students_placed=models.IntegerField(default=0)
	

class Faculty_Data(models.Model):
	college_id=models.IntegerField(primary_key=True)
	stream_id=models.IntegerField(default=0)
	faculty_name=models.CharField(max_length=128, default='', unique=False)	
	faculty_rating=models.IntegerField(default=0)
	
class Placement_Data(models.Model):
	college_id=models.IntegerField(primary_key=True)
	stream_id=models.IntegerField(default=0)
	company_id=models.IntegerField(default=0)
	year=models.DateTimeField(default=datetime.now(), blank=True)
	package=models.IntegerField(default=0)
	number_of_students=models.IntegerField(default=0)
	
class Company_Master(models.Model):
	company_id=models.IntegerField(default=0)
	company_name=models.CharField(max_length=128, default='', unique=False)
	
class Hostel_Master(models.Model):
	college_id=models.IntegerField(primary_key=True, default=0)
	hostel_type=models.CharField(max_length=128, primary_key=True)
	number_of_hostel=models.IntegerField(default=0)
	
class Hostel_Facility_Master(models.Model):
	facility_id=models.IntegerField(primary_key=True, default=0)
	facility_name=models.CharField(max_length=128, default='', unique=False)
	
class Hostel_Data(models.Model):
	college_id=models.IntegerField(primary_key=True)
	hostel_id=models.IntegerField(primary_key=True)
	hostel_capacity=models.IntegerField(default=0)
	facility_id_list=models.CharField(max_length=128, default='', unique=False)
	event_id_list=models.CharField(max_length=128, default='', unique=False)
	
class Hostel_Event_Data(models.Model):
	college_id=models.IntegerField(primary_key=True)
	hostel_id=models.IntegerField(primary_key=True)
	event_id=models.IntegerField(primary_key=True)
	event_name=models.CharField(max_length=128, default='', unique=False)
	event_description=models.CharField(max_length=128, default='', unique=False)
	
	
	




