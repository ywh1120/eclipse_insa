# -*- coding: utf-8 -*-

from django.shortcuts import render
from insa_record.models import *
from insa_record.forms import *
from django.views import generic
from django.shortcuts import(
	render,get_object_or_404,redirect
)
from django.forms.formsets import formset_factory
from django.http import Http404
from django.db.models.fields import Empty
from django.forms.models import modelformset_factory
# Create your views here.
def save_formset(formset, request, infopk, tabval):
	if formset.is_valid():
		for ffo in formset:
			ffo_inst = ffo.save(commit=False) 
			if tabval == 'family':
				ffo_inst.family_myinfo = infopk
			elif tabval == 'academic':
				ffo_inst.academic_myinfo = infopk
			elif tabval == 'career':
				ffo_inst.career_myinfo = infopk
			elif tabval == 'license':
				ffo_inst.license_myinfo = infopk		
			elif tabval == 'lang':
				ffo_inst.lang_myinfo = infopk
			elif tabval == 'appoint':
				ffo_inst.appoint_myinfo = infopk
			elif tabval == 'edu':
				ffo_inst.edu_myinfo = infopk
			elif tabval == 'rnp':
				ffo_inst.rnp_myinfo = infopk	
			ffo_inst.user = request.user
			ffo_inst.save()	
		else:
			return render(request, 'insert/error.html', {'errorform':formset})
		
		
def detail_load(list, qdata, template, pre):
	if list : 
		myform = list(queryset=qdata, prefix=pre)
	else :
		myform = template()
	
	return myform

def insert(request):
	insaform = InsaForm()
	fformlist = formset_factory(FamilyForm, extra=5, max_num=5)
	academiclist = formset_factory(AcademicForm, extra=4, max_num=4)
	careerlist = formset_factory(CareerForm, extra=5, max_num=5)
	licenselist = formset_factory(LicenseForm, extra=4, max_num=4)
	languagelist = formset_factory(LanguageForm, extra=2, max_num=2)
	appointlist = formset_factory(AppointmentForm, extra=7, max_num=7)
	edulist = formset_factory(EduinfoForm, extra=13, max_num=13)
	edulist2 = formset_factory(EduinfoForm, extra=13, max_num=13)
	rnplist = formset_factory(RewardnpunishForm, extra=7, max_num=7)
	if request.method == "GET":	
		fform = fformlist(prefix='family')
		academic = academiclist(prefix='academic')
		career = careerlist(prefix='career')
		license = licenselist(prefix='license')
		language = languagelist(prefix='lang')
		appoint = appointlist(prefix='appoint')
		edu = edulist(prefix='edu')
		edu2 = edulist2(prefix='edu2')
		rnp = rnplist(prefix='rnp')
	elif request.method == "POST":
		insaform = InsaForm(request.POST, request.FILES)
		fform = fformlist(request.POST, prefix='family')
		academic = academiclist(request.POST, prefix='academic')
		career = careerlist(request.POST, prefix='career')
		license = licenselist(request.POST, prefix='license')
		language = languagelist(request.POST, prefix='lang')
		appoint = appointlist(request.POST, prefix='appoint')
		edu = edulist(request.POST, prefix='edu')
		edu2 = edulist2(request.POST, prefix='edu2')
		rnp = rnplist(prefix='rnp')
		if insaform.is_valid():
			insert = insaform.save(commit=False)
			insert.user = request.user
			insert.save()
			
			save_formset(fform, request, insert, 'family')
			save_formset(academic, request, insert, 'academic')
			save_formset(career, request, insert, 'career')
			save_formset(license, request, insert, 'license')
			save_formset(language, request, insert, 'lang')
			save_formset(appoint, request, insert, 'appoint')
			save_formset(edu, request, insert, 'edu')
			save_formset(edu2, request, insert, 'edu')
			save_formset(rnp, request, insert, 'rnp')
					
			return render(request, 'insert/complete.html')
		else:
			return render(request, 'insert/error.html', {'errorform':insaform,'fform':fform})		
	return render(request, 'insert/index.html', 
				{'insaform':insaform,
				'fform':fform,
				'academic':academic,
				'career':career,
				'license':license,
				'lang':language,
				'appoint':appoint,
				'edu':edu,
				'edu2':edu2,
				'rnp':rnp})

def list(request):
	list = Myinfo.objects.all()
	return render(request, 'list/list.html', {'list':list})

def mainpage(request):
	return render(request, 'index.html')

def detail(request, detail_id):
	#쿼리로드영역
	infodata = Myinfo.objects.get(id = detail_id)#POST에서 인식못함
	fadata = Family.objects.filter(family_myinfo__id = detail_id)#FK필드값 접근은 언더바 두개
	acdata = Academic.objects.filter(academic_myinfo__id = detail_id)
	cadata = Career.objects.filter(career_myinfo__id = detail_id)
	lidata = License.objects.filter(license_myinfo__id = detail_id)
	ladata = Language.objects.filter(lang_myinfo__id = detail_id)
	apdata = Appointment.objects.filter(appoint_myinfo__id = detail_id)
	edudata = Eduinfo.objects.filter(edu_myinfo__id = detail_id)
	rnpdata = Rewardnpunish.objects.filter(rnp_myinfo = detail_id)
	#폼생성영역
	
	insaform = InsaForm(instance=infodata)
	fformlist = modelformset_factory(Family, FamilyForm, extra=5, max_num=5)
	academiclist = modelformset_factory(Academic, AcademicForm, extra=4, max_num=4)
	careerlist = modelformset_factory(Career, CareerForm, extra=5, max_num=5)
	licenselist = modelformset_factory(License, LicenseForm, extra=4, max_num=4)
	languagelist = modelformset_factory(Language, LanguageForm, extra=2, max_num=2)
	appointlist = modelformset_factory(Appointment, AppointmentForm, extra=7, max_num=7)
	edulist = modelformset_factory(Eduinfo, EduinfoForm, extra=13, max_num=13)
	rnplist = modelformset_factory(Rewardnpunish, RewardnpunishForm, extra=7, max_num=7)
	
	#inlineformset_factory(parent_model, model, form, formset, fk_name, fields, exclude, extra, can_order, can_delete, max_num, formfield_callback, widgets, validate_max, localized_fields, labels, help_texts, error_messages, min_num, validate_min)
	if request.method == "GET":
		fform = detail_load(fformlist,fadata,FamilyForm,'family')
		academic = detail_load(academiclist,acdata,AcademicForm, 'academic')
		career = detail_load(careerlist,cadata,CareerForm, 'career')
		license = detail_load(licenselist,lidata,LicenseForm, 'license')
		language = detail_load(languagelist,ladata,LanguageForm, 'lang')
		appoint = detail_load(appointlist,apdata,AppointmentForm, 'appoint')
		edu = detail_load(edulist,edudata,EduinfoForm, 'edu')
		edu2 = detail_load(edulist,edudata,EduinfoForm, 'edu2')
		rnp = detail_load(rnplist,rnpdata,RewardnpunishForm, 'rnp')
	elif request.method == "POST":
		insaform = InsaForm(request.POST, instance=infodata)
		if insaform.is_valid():
			update = insaform.save(commit=False)
			update.user = request.user
			update.save()
			
			fform = fformlist(request.POST,prefix='family',queryset=fadata)
			academic = academiclist(request.POST,prefix='academic',queryset=acdata)
			career = careerlist(request.POST,prefix='career',queryset=cadata)
			license = licenselist(request.POST,prefix='license',queryset=lidata)
			language = languagelist(request.POST,prefix='lang',queryset=ladata)
			appoint = appointlist(request.POST,prefix='appoint',queryset=apdata)
			edu = edulist(request.POST,prefix='edu',queryset=edudata)
			edu2 = edulist(request.POST,prefix='edu2',queryset=edudata)
			rnp = rnplist(request.POST,prefix='rnp',queryset=rnpdata)
			
			save_formset(fform, request, update, 'family')
			save_formset(academic, request, update, 'academic')
			save_formset(career, request, update, 'career')
			save_formset(license, request, update, 'license')
			save_formset(language, request, update, 'lang')
			save_formset(appoint, request, update, 'appoint')
			save_formset(edu, request, update, 'edu')
			save_formset(edu2, request, update, 'edu')
			save_formset(rnp, request, update, 'rnp')
			
			return render(request, 'insert/complete.html')
		else:
			return render(request, 'insert/error.html', {'errorform':insaform})
		return render(request, 'insert/index.html', {'myid' : detail_id,
													'insaform' : insaform})

	return render(request, 'insert/index.html', {'myid' : detail_id,
												'insaform' : insaform,
												'fform' : fform, 
												'academic':academic,
												'career':career,
												'license':license,
												'lang':language,
												'appoint':appoint,
												'edu':edu,
												'edu2':edu2,
												'rnp':rnp})

