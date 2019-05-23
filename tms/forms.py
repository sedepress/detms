from django import forms
from tms.models import Line, Area
from django.http import JsonResponse

class LineForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    ori_province = forms.IntegerField()
    ori_province_name = forms.CharField(max_length=50)
    ori_city = forms.IntegerField()
    ori_city_name = forms.CharField(max_length=50)
    ori_area = forms.IntegerField()
    ori_area_name = forms.CharField(max_length=50)
    des_province = forms.IntegerField()
    des_province_name = forms.CharField(max_length=50)
    des_city = forms.IntegerField()
    des_city_name = forms.CharField(max_length=50)
    des_area = forms.IntegerField()
    des_area_name = forms.CharField(max_length=50)

    class Meta:
        model = Line
        fields = '__all__'