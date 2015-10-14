# -*- coding: utf-8 -*-

from django import forms
from insa_record.models import *
from django.contrib.auth.models import User
from datetimewidget.widgets import DateTimeWidget, DateWidget
	
class InsaForm(forms.ModelForm):
	name_kor = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'8'}))
	name_eng = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'8'}))
	civil_code = forms.CharField(required=False)
	gender = forms.ChoiceField(required=False, widget=forms.Select())
	married = forms.ChoiceField(required=False, widget=forms.Select())
	birthday = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'10'}))
	birthday_type = forms.ChoiceField(required=False, widget=forms.Select())
	email = forms.EmailField(
                required=False,
                widget=forms.EmailInput(
                        attrs={
                                'size' : '20',
                                'required' : 'False',   
                        }
                )
        )
	address_civil = forms.CharField(required=False, widget=forms.TextInput(attrs={'size':'70'}))
	address_live = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'70'}))
	phone = forms.CharField(required=False)
	mobile_phone = forms.CharField(required=False)
	head_house = forms.CharField(required=False)
	house_type = forms.ChoiceField(required=False, widget=forms.Select())
	handicap_type = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'6'}))
	handicap_grade = forms.ChoiceField(required=False, widget=forms.Select())
	
	handicap_trial = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'10'}))
	handicap_num = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'6'}))
	handicap_div = forms.CharField(required=False)
	military_serve = forms.ChoiceField(required=False, widget=forms.Select())
	military_type = forms.ChoiceField(required=False, widget=forms.Select())
	military_branch = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'10'}))	
	military_exampt = forms.CharField(required=False)
	military_class = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'10'}))
	employ_day = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'10'}))
	#employ_part = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'8'}))
	employ_part = forms.ChoiceField(required=False, widget=forms.Select())
	employ_kind = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'6'}))
	
	#employ_type = forms.ChoiceField(required=False,widget=forms.RadioSelect())	
	employ_intro = forms.CharField(required=False)
	employ_etc = forms.CharField(required=False)
	
	emergency_name = forms.CharField(required=False)
	emergency_rel = forms.CharField(required=False)
	emergency_address = forms.CharField(required=False)
	emergency_call = forms.CharField(required=False)

	sign = forms.CharField(required=False)
	retire_date = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'10'}))
	retire_reason = forms.CharField(required=False)
	info_image = forms.ImageField(required=False,widget=forms.FileInput(attrs={'style':'width:150px'}))
	etc = forms.CharField(required=False,widget=forms.Textarea(attrs={'cols':'50'}))
	
	def __init__(self, *args, **kwargs):
		super(InsaForm, self).__init__(*args, **kwargs)
		self.fields['birthday_type'].choices = [(1,'양력'),(2,'음력')]
		self.fields['birthday_type'].initial = 1
		self.fields['gender'].choices = [(1,'남'),(2,'여')]
		self.fields['gender'].initial = 1
		self.fields['married'].choices = [(1,'미혼'),(2,'기혼')]
		self.fields['married'].initial = 1
		self.fields['house_type'].choices = [(1,'자가'),(2,'전세'),(3,'월세'),(4,'기숙사')]
		self.fields['house_type'].initial = 1
		self.fields['handicap_grade'].choices = [(1,'해당없음'),(2,'1급'),(3,'2급'),(4,'3급')]
		self.fields['handicap_grade'].initial = 1
		self.fields['military_serve'].choices = [(1,'면제'),(2,'기필'),(3,'미필')]
		self.fields['military_serve'].initial = 1
		self.fields['military_type'].choices = [(1,'해당없음'),(2,'육군'),(3,'해군'),(4,'공군'),(5,'해병대'),(6,'의무경찰'),(7,'의무소방')]
		self.fields['military_type'].initial = 1
		self.fields['employ_part'].choices = [('미지정','미지정'),('의료진','의료진'),('관리과','관리과'),('총무과','총무과'),('원무과','원무과'),('외래간호','외래간호'),('6병동','6병동'),('7병동','7병동'),('운동재활센터','운동재활센터'),('약제과','약제과'),('내과','내과'),('영상의학과','영상의학과'),('임상병리실','임상병리실'),('피부과','피부과'),('비수술센터','비수술센터')]
		self.fields['employ_part'].initial = '미지정'
		#self.fields['employ_type'].choices = [(1,'정규직'),(2,'계약직'),(3,'공개채용'),(4,'사내추천'),(5,'재입사'),(6,'기타')] 
	class Meta:
		model = Myinfo
		fields = '__all__'
#('name_kor','name_eng','civil_code','gender','married','birthday','birthday_type','email','address_civil','address_live','phone','mobile_phone','head_house','house_type','handicap_type','handicap_grade','handicap_trial','handicap_num','handicap_div','military_serve','military_type','military_branch','military_exampt','military_class','employ_day','employ_part','employ_kind','employ_type','employ_intro','employ_etc','emergency_name','emergency_rel','emergency_address','emergency_call','sign','retire_date','retire_reason','info_image','etc',)	

class FamilyForm(forms.ModelForm):
	family_relation = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	family_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	family_birthday = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'10'}))
	family_academic = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	family_job = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'6'}))
	family_together = forms.ChoiceField(required=False, widget=forms.Select())
	def __init__(self, *args, **kwargs):
		super(FamilyForm, self).__init__(*args, **kwargs)
		self.fields['family_together'].choices = [(1,'동거'),(2,'별거')]
		self.fields['family_together'].initial = 1
	class Meta:
		model = Family
		fields = '__all__'
		exclude = ('family_myinfo',)

class AcademicForm(forms.ModelForm):
	academic_trial_start = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'7'}))
	academic_trial_end = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'7'}))
	academic_school_title = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'15'}))
	academic_school_part = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	academic_graduated = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	class Meta:
		model = Academic
		fields = '__all__'
		exclude = ('academic_myinfo',)
		
class CareerForm(forms.ModelForm):
	career_trial_start = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'7'}))
	career_trial_end = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'7'}))
	career_oldjob = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	career_job_type = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	career_job_position = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	career_retire_reason = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	class Meta:
		model = Career
		fields = '__all__'
		exclude = ('career_myinfo',)
		
class LicenseForm(forms.ModelForm):
	license_title = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	license_number = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	license_getday = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'10'}))
	license_organization = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'20'}))
	license_etc = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'2'}))
	class Meta:
		model = License
		fields = '__all__'
		exclude = ('license_myinfo',)

class LanguageForm(forms.ModelForm):
	lang_language = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	lang_grade = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	lang_score = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'style':'width:50px'}))
	lang_pubtest = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'20'}))
	lang_getday = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'10'}))
	class Meta:
		model = Language
		fields = '__all__'
		exclude = ('lang_myinfo',)

class AppointmentForm(forms.ModelForm):
	appoint_type = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	appoint_apday = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'7'}))
	appoint_part = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	appoint_position = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	appoint_work = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'20'}))
	class Meta:
		model = Appointment
		fields = '__all__'
		exclude = ('appoint_myinfo',)

class EduinfoForm(forms.ModelForm):
	edu_type = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	edu_title = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	edu_trial_start = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'10'}))
	edu_trial_end = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'10'}))
	edu_organization = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	edu_cost = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	class Meta:
		model = Eduinfo
		fields = '__all__'
		exclude = ('edu_myinfo',)
		
class RewardnpunishForm(forms.ModelForm):
	rnp_reward_date = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'10'}))
	rnp_reward_content = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	rnp_reward_result = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	rnp_punish_date = forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker','readonly':'true','size':'10'}))
	rnp_punish_content = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	rnp_punish_result = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':'5'}))
	class Meta:
		model = Rewardnpunish
		fields = '__all__'
		exclude = ('rnp_myinfo',)