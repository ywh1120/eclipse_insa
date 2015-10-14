# -*- coding: utf-8 -*-

import os
from django.db import models
#from imagekit.models import ProcessedImageField
#from imagekit.processors import ResizeToFill
# Create your models here.

def generate_filename(self, filename):
	url = '/'.join(['content',self.civil_code, filename])
	return url	

class Myinfo(models.Model):
	name_kor = models.CharField(max_length=30)
	name_eng = models.CharField(max_length=50)
	civil_code = models.CharField(max_length=60)
	gender = models.IntegerField(default=1)
	married = models.IntegerField(default=1)
	birthday = models.DateField()
	birthday_type = models.IntegerField(default=1)
	email = models.EmailField()
	address_civil = models.CharField(max_length=200)
	address_live = models.CharField(max_length=200)
	phone = models.CharField(max_length=100)
	mobile_phone = models.CharField(max_length=100)
	head_house = models.CharField(max_length=60)
	house_type = models.IntegerField(default=1)
	handicap_type = models.CharField(max_length=30,null=True)
	handicap_grade = models.IntegerField(default=1)
	handicap_trial = models.DateField(null=True)
	handicap_num = models.CharField(max_length=100,null=True)
	handicap_div = models.CharField(max_length=100,null=True)
	military_serve = models.IntegerField(default=1)
	military_type = models.IntegerField(default=1)
	military_branch = models.CharField(max_length=30,null=True)
	military_exampt = models.CharField(max_length=80,null=True)
	military_class = models.CharField(max_length=20,null=True)
	employ_day = models.DateField()
	employ_part = models.CharField(max_length=30)
	employ_kind = models.CharField(max_length=30)
	employ_type = models.IntegerField(default=1)
	employ_intro = models.CharField(max_length=50)
	emergency_name = models.CharField(max_length=30)
	emergency_rel = models.CharField(max_length=20)
	emergency_address = models.CharField(max_length=200)
	emergency_call = models.CharField(max_length=80)
	sign = models.CharField(max_length=150)	
	retire_date = models.DateField(null=True)
	retire_reason = models.CharField(max_length=150,null=True)
	info_image = models.ImageField(null=True,upload_to=generate_filename)
	salary_class = models.CharField(max_length=50,null=True)
	pay_step = models.CharField(max_length=100,null=True)
	etc = models.CharField(max_length=200,null=True)
	
	def delete(self, *args, **kwargs):
		self.info_image.delete()
		super(Myinfo, self).delete(*args, **kwargs)
	
	def __unicode__(self) : 
		return self.name_kor

class Academic(models.Model):
	academic_myinfo = models.ForeignKey(Myinfo,null=True)
	academic_trial_start = models.DateField(null=True)
	academic_trial_end = models.DateField(null=True)
	academic_school_title = models.CharField(max_length=80,null=True)
	academic_school_part = models.CharField(max_length=50,null=True)
	academic_graduated = models.CharField(max_length=20,null=True)
	
	def __unicode__(self):
		return self.academic_myinfo.name_kor
	
class Family(models.Model):
	family_myinfo = models.ForeignKey(Myinfo,null=True)
	family_relation = models.CharField(max_length=20,null=True)
	family_name = models.CharField(max_length=20,null=True)
	family_birthday = models.DateField(null=True)
	family_academic = models.CharField(max_length=30,null=True)
	family_job = models.CharField(max_length=50,null=True)
	family_together = models.CharField(max_length=30,null=True)
	
	def __unicode__(self) : 
		return self.family_myinfo.name_kor
	
class Career(models.Model):
	career_myinfo = models.ForeignKey(Myinfo,null=True)
	career_trial_start = models.DateField(null=True)
	career_trial_end = models.DateField(null=True)
	career_oldjob = models.CharField(max_length=80,null=True)
	career_job_type = models.CharField(max_length=30,null=True)
	career_job_position = models.CharField(max_length=30,null=True)
	career_retire_reason = models.CharField(max_length=50,null=True)

class License(models.Model):
	license_myinfo = models.ForeignKey(Myinfo,null=True)
	license_title = models.CharField(max_length=60,null=True)
	license_number = models.CharField(max_length=50,null=True)
	license_getday = models.DateField(null=True)
	license_organization = models.CharField(max_length=60,null=True)
	license_etc = models.CharField(max_length=60,null=True)

class Language(models.Model):
	lang_myinfo = models.ForeignKey(Myinfo,null=True)
	lang_language = models.CharField(max_length=30,null=True)
	lang_grade = models.CharField(max_length=10,null=True)
	lang_score = models.IntegerField(default=0,null=True)
	lang_pubtest = models.CharField(max_length=50,null=True)
	lang_getday = models.DateField(null=True)

class Appointment(models.Model):
	appoint_myinfo = models.ForeignKey(Myinfo,null=True)
	appoint_type = models.CharField(max_length=50,null=True)
	appoint_apday = models.DateField(null=True)
	appoint_part = models.CharField(max_length=60,null=True)
	appoint_position = models.CharField(max_length=50,null=True)
	appoint_work = models.CharField(max_length=80,null=True)

class Eduinfo(models.Model):
	edu_myinfo = models.ForeignKey(Myinfo,null=True)
	edu_type = models.CharField(max_length=50,null=True)
	edu_title = models.CharField(max_length=100,null=True)
	edu_trial_start = models.DateField(null=True)
	edu_trial_end = models.DateField(null=True)
	edu_organization = models.CharField(max_length=60,null=True)
	edu_cost = models.IntegerField(default=0,null=True)


class Rewardnpunish(models.Model):
	rnp_myinfo = models.ForeignKey(Myinfo,null=True)
	rnp_reward_date = models.CharField(max_length=80,null=True)
	rnp_reward_content = models.CharField(max_length=150,null=True)
	rnp_reward_result = models.CharField(max_length=80,null=True)
	rnp_punish_date = models.DateField(null=True)
	rnp_punish_content = models.CharField(max_length=150,null=True)
	rnp_punish_result = models.CharField(max_length=80,null=True)


