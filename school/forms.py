import phonenumbers
from django import forms

from school.models import Teachers, Subject


class SubjectForm(forms.ModelForm):
    teachers = forms.ModelMultipleChoiceField(
        queryset=Teachers.objects.all(), required=False, widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Subject
        fields = ["name", "description", "score"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name == "math":
            raise forms.ValidationError("You can't use this name")
        if len(name) > 50:
            raise forms.ValidationError("Name is too long")
        return name


class TeacherForm(forms.ModelForm):
    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone:
            raise forms.ValidationError("Phone cannot be empty.")
        try:
            parsed = phonenumbers.parse(phone, None)
        except phonenumbers.NumberParseException as e:
            raise forms.ValidationError(e.args[0])
        return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

    class Meta:
        model = Teachers
        fields = ["first_name", "phone", "photo", "subjects"]
