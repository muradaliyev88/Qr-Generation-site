from django import forms
from polls.models import QR
from django.contrib import admin



class QR_Form(forms.ModelForm):
	
	class Meta:
		model = QR
		fields = '__all__'

admin.site.register(QR)







