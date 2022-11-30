# from django import forms
# from bankingapp.models import Member, Branches


# class UserCreationForm(forms.ModelForm):
#     class Meta:
#         fields="__all__"
#     def __int__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.fields['branches'].queryset=Branches.objects.none()
#         if 'district' in self.data:
#             try:
#                 district_id=int(self.data.get('district'))
#                 self.fields['branches'].queryset=Branches.objects.filter(district_id=district_id).order_by('name')
#             except(ValueError,TypeError):
#                 pass
#         elif self.instance.pk:
#             self.fields['branches'].queryset=self.instance.district.branches_set.order_by('name')






