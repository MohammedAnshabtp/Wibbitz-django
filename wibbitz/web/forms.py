from django import forms
from django.forms import ModelForm
from django.forms.widgets import EmailInput, Select, TextInput
from web.models import COMPANY_SIZE, COUNTRY, INDUSTRY, JOB_ROLE, Contact

EMPTY_COMPANY_SIZE = (("","Company Size"),) + COMPANY_SIZE
EMPTY_INDUSTRY = (("","Industry"),) + INDUSTRY
EMPTY_JOB_ROLE = (("","Job Role"),) + JOB_ROLE
EMPTY_COUNTRY = (("","Country"),) + COUNTRY

class ContactForm(ModelForm):
    company_size =forms.ChoiceField(choices=EMPTY_COMPANY_SIZE)
    industry = forms.ChoiceField(choices=EMPTY_INDUSTRY)
    job_role = forms.ChoiceField(choices=EMPTY_JOB_ROLE)
    country = forms.ChoiceField(choices=EMPTY_COUNTRY)

    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "email" : EmailInput(attrs={"placeholder":"Enter Your Email"}),
            "first_name" : TextInput(attrs={"placeholder":"Enter Your First Name"}),
            "last_name" : TextInput(attrs={"placeholder":"Enter Your Last Name"}),
            "company" : TextInput(attrs={"placeholder":"Enter Your Company"}),
            "company_size" : Select(),
            "industry" : Select(),
            "job_role" : Select(),
            "country" : Select(),
        }


