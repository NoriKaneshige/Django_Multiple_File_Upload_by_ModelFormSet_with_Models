from django import forms
from .models import UploadFile


class SingleUploadModelForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = '__all__'

UploadModelFormSet = forms.modelformset_factory(
    UploadFile, form=SingleUploadModelForm,
    extra=3
)