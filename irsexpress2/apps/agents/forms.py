
from django import forms

from .models import BaseAgent, Appointee, Preparer
from utils.forms import ImprovedForm


class AgentEditForm(ImprovedForm, forms.ModelForm):

    class Meta:
        model = BaseAgent
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_widget_class('zipcode', 'zip-field')
        self.set_widget_class('caf', 'caf-field')
        self.set_widget_class('ptin', 'ptin-field')


class AppointeeEditform(AgentEditForm):
    class Meta(AgentEditForm.Meta):
        model = Appointee


class PreparerEditform(AgentEditForm):
    class Meta(AgentEditForm.Meta):
        model = Preparer
