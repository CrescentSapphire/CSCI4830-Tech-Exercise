from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from .models import Boardgame

class BoardgameForm(forms.ModelForm):
    class Meta:
        model = Boardgame
        fields = ("name", "type", "owner",)
        exclude = ("date_added",)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('owner', css_class='form-group col-md-6 mb-0'),
                Column('type', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )
        self.helper.add_input(Submit('submit', 'Submit'))