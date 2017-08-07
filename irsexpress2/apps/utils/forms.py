
from django import forms
from django.template.loader import render_to_string

from utils.widgets import (CheckboxToggleWidget, BTSInputWidget, BTSNumInputWidget, USPhoneNumberField,
                           BTSTextArea, BTSSelectWidget, BTSSelectDateWidget)


class ImprovedForm(object):

    def __init__(self, *args, **kwargs):
        super(ImprovedForm, self).__init__(*args, **kwargs)
        self.reinit_widgets()

    def add_class(self, field_name, newclass):
        # get css class from the given widget and returns the string with new class
        classes = list(c for c in self.fields[field_name].widget.attrs.get('class', '').split(' ') if c)
        return ' '.join(set(classes + newclass.split(' ')))

    def set_widget_class(self, field_name, newclass):
        # adds CSS class for the field's widget
        self.fields[field_name].widget.attrs['class'] = self.add_class(field_name, newclass)

    def unset_widget_class(self, field_name, classname):
        self.fields[field_name].widget.unset_class(classname)

    def reinit_widgets(self):
        for fname in self.fields:
            if isinstance(self.fields[fname].widget, forms.HiddenInput):
                continue
            is_textarea = isinstance(self.fields[fname].widget, forms.Textarea)
            prev_widget_args = self.fields[fname].widget.attrs
            widget_args = {'attrs': prev_widget_args}
            # print(fname, type(self.fields[fname]))
            if isinstance(self.fields[fname], forms.fields.BooleanField):
                widget_args.update({
                    #
                })
                self.fields[fname].required = False  # to allow False values to be accepted
                self.fields[fname].widget = CheckboxToggleWidget(**widget_args)
            elif isinstance(self.fields[fname], (forms.fields.CharField, forms.fields.IntegerField,
                                                 forms.fields.ChoiceField,
                                                 USPhoneNumberField)):
                placeholder = "This field is required" if self.fields[fname].required else self.fields[fname].help_text
                css_class = ""
                widget_args.update({
                    'placeholder': placeholder, 'css_class': css_class,
                    'error_messages': placeholder
                })
                # print(fname, type(self.fields[fname].widget))
                if isinstance(self.fields[fname], USPhoneNumberField):
                    widget_args['attrs'].update({'type': 'tel'})
                    self.fields[fname].widget = BTSInputWidget(**widget_args)
                elif isinstance(self.fields[fname], forms.fields.ChoiceField):
                    widget_args['choices'] = self.fields[fname].widget.choices
                    self.fields[fname].widget = BTSSelectWidget(**widget_args)
                elif isinstance(self.fields[fname], forms.fields.FloatField):
                    # widget_args['attrs'].update({'type': 'number'})
                    widget_class = "float-field"
                    if self.fields[fname].min_value and self.fields[fname].min_value >= 0:
                        widget_class += ' positive-number'
                    else:
                        widget_class += ' allow-negative'
                    widget_args['attrs'].update({'class': self.add_class(fname, widget_class)})
                    widget_args.update({'numtype': 'float'})
                    self.fields[fname].widget = BTSNumInputWidget(**widget_args)
                elif isinstance(self.fields[fname], forms.fields.IntegerField):
                    # widget_args['attrs'].update({'type': 'number'})
                    widget_class = "number-field"
                    if self.fields[fname].min_value and self.fields[fname].min_value >= 0:
                        widget_class += ' positive-number'
                    else:
                        widget_class += ' allow-negative'
                    widget_args['attrs'].update({'class': self.add_class(fname, widget_class)})
                    widget_args.update({'numtype': 'int'})
                    self.fields[fname].widget = BTSNumInputWidget(**widget_args)
                elif isinstance(self.fields[fname], forms.fields.CharField):
                    widget_args['max_length'] = self.fields[fname].max_length
                    if is_textarea:
                        self.fields[fname].widget = BTSTextArea(**widget_args)
                    else:
                        self.fields[fname].widget = BTSInputWidget(**widget_args)
            elif isinstance(self.fields[fname], forms.fields.DateField):
                allyears = range(2060, 1900, -1)
                widget_args['attrs'].update({'class': self.add_class(fname, 'date-field')})
                self.fields[fname].widget = BTSSelectDateWidget(years=allyears, **widget_args)

    def as_div(self):
        form_style = 'inline'
        context = {'form': self, 'style': form_style}
        result = render_to_string('utils/form_div.html', context)
        return result

    def as_table(self):
        form_style = 'table'
        context = {'form': self, 'style': form_style}
        result = render_to_string('utils/form_table.html', context)
        return result
