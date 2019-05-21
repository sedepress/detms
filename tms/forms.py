from django import forms
from tms.models import Line, Area

class LineForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False)
    ori_province = forms.IntegerField()
    ori_province_name = forms.CharField(max_length=50, required=False)
    ori_city = forms.IntegerField()
    ori_city_name = forms.CharField(max_length=50, required=False)
    ori_area = forms.IntegerField()
    ori_area_name = forms.CharField(max_length=50, required=False)
    des_province = forms.IntegerField()
    des_province_name = forms.CharField(max_length=50, required=False)
    des_city = forms.IntegerField()
    des_city_name = forms.CharField(max_length=50, required=False)
    des_area = forms.IntegerField()
    des_area_name = forms.CharField(max_length=50, required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        ori_province = cleaned_data.get('ori_province')
        ori_province_name = Area.objects.get(part_id=ori_province)
        cleaned_data['ori_province_name'] = ori_province_name
        ori_city = cleaned_data.get('ori_city')
        ori_city_name = Area.objects.get(part_id=ori_city)
        cleaned_data['ori_city_name'] = ori_city_name
        ori_area = cleaned_data.get('ori_area')
        ori_area_name = Area.objects.get(part_id=ori_area)
        cleaned_data['ori_area_name'] = ori_area_name
        des_province = cleaned_data.get('des_province')
        des_province_name = Area.objects.get(part_id=des_province)
        cleaned_data['des_province_name'] = des_province_name
        des_city = cleaned_data.get('des_city')
        des_city_name = Area.objects.get(part_id=des_city)
        cleaned_data['des_city_name'] = des_city_name
        des_area = cleaned_data.get('des_area')
        des_area_name = Area.objects.get(part_id=des_area)
        cleaned_data['des_area_name'] = des_area_name

        return cleaned_data

    class Meta:
        model = Line
        exclude = ('name',)