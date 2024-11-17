from django import forms
from .models import *

class ProcessSelectionForm(forms.Form):
    process = forms.ModelChoiceField(queryset=Process.objects.all(), label="Select Process")
    process_code = forms.ModelChoiceField(queryset=ProcessCode.objects.none(), label="Select Process Code")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'process' in self.data:
            try:
                process_id = int(self.data.get('process'))
                self.fields['process_code'].queryset = ProcessCode.objects.filter(process_id=process_id)
            except (ValueError, TypeError):
                pass

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
        
class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ['name']
        labels = {'name': 'Process Name'}

class ProcessCodeForm(forms.ModelForm):
    class Meta:
        model = ProcessCode
        fields = ['process', 'code_name']
        labels = {'process': 'Select Process', 'code_name': 'Process Code Name'}
        
    def clean_code_name(self):
        code_name = self.cleaned_data.get('code_name')
        if ProcessCode.objects.filter(code_name=code_name).exists():
            raise forms.ValidationError(f"The Process Code '{code_name}' already exists.")
        return code_name

class ApproverForm(forms.ModelForm):
    class Meta:
        model = Approver
        fields = ['name']
        labels = {'name': 'Approver Name'}

class ApprovalLevelForm(forms.ModelForm):
    class Meta:
        model = ApprovalLevel
        fields = ['process_code', 'level_number', 'approver']
        labels = {
            'process_code': 'Select Process Code',
            'level_number': 'Approval Level Number',
            'approver': 'Select Approver'
        }