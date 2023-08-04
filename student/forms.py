from student.models import Student,Employee,GenderChoices
from django import forms


class ContactForm(forms.Form):
        fullname = forms.CharField(max_length=125,widget=forms.TextInput(attrs={"class":"form-control"}),help_text="Inter your fullname "),
        message = forms.CharField(max_length=500),
        phone_number = forms.CharField(max_length=13)
        # type = forms.ChoiceField(choices=type_choices)
        type = forms.ChoiceField(choices=GenderChoices.choices)

        def clean(self):
            super(ContactForm,self).clean()
            phone_number = self.cleaned_data.get("phone_number")
            if not str(phone_number).startswith("+998"):
                self._errors["phone_number"] = self.error_class(
                    ["Invalid phone number! It should start with +998!"]
                )
            return self.cleaned_data

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            "firstname": forms.TextInput(attrs={"class": "form-control"}),
            "lastname": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }




# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = "__all__"
#         widgets = {
#             "firstname": forms.TextInput(attrs={"class": "form-control"}),
#             "lastname": forms.TextInput(attrs={"class": "form-control"}),
#             "phone_number": forms.TextInput(attrs={"class": "form-control"}),
#             "age": forms.NumberInput(attrs={"class": "form-control"}),
#             'group': forms.Select(attrs={'class': 'form-control'}),
#             'gender': forms.Select(attrs={'class': 'form-control'}),
#         }
