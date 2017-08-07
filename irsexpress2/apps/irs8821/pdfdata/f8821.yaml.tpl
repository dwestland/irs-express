{% load func_helpers %}
{% load misc_helpers %}

-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0]
    FieldType: ''
-   FieldFlags: 8388608
    value: {{ form.page1.title }}
    desc: Signature
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].#subform[2].f1_27[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: --empty--
    desc: date
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].#subform[2].f1_28[0]
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line3Table[0]
    FieldType: ''
-   FieldFlags: 8388608
    value: {{ form.page2.tax_info_1.tax_information_type }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line3Table[0].BodyRow1[0].f1_15[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.tax_info_1.tax_form_number }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].Line3Table[0].BodyRow1[0].f1_16[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.tax_info_1.years }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line3Table[0].BodyRow1[0].f1_17[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.tax_info_1.details }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line3Table[0].BodyRow1[0].f1_18[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.tax_info_2.tax_information_type }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line3Table[0].BodyRow2[0].f1_19[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.tax_info_2.tax_form_number }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].Line3Table[0].BodyRow2[0].f1_20[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.tax_info_2.years }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line3Table[0].BodyRow2[0].f1_21[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.tax_info_2.details }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line3Table[0].BodyRow2[0].f1_22[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.tax_info_3.tax_information_type }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line3Table[0].BodyRow3[0].f1_23[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.tax_info_3.tax_form_number }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].Line3Table[0].BodyRow3[0].f1_24[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.tax_info_3.years }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line3Table[0].BodyRow3[0].f1_25[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.tax_info_3.details }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line3Table[0].BodyRow3[0].f1_26[0]
    FieldType: Text
-   FieldFlags: 1
    value: --empty--
    desc: IRS Use Only
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Pg1Header[0].f1_1[0]
    FieldType: Text
-   FieldFlags: 1
    value: --empty--
    desc: IRS Use Only
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Pg1Header[0].f1_2[0]
    FieldNameAlt: 'Name '
    FieldType: Text
-   FieldFlags: 1
    value: --empty--
    desc: IRS Use Only
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Pg1Header[0].f1_3[0]
    FieldNameAlt: Telephone
    FieldType: Text
-   FieldFlags: 1
    value: --empty--
    desc: IRS Use Only
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Pg1Header[0].f1_4[0]
    FieldNameAlt: Function
    FieldType: Text
-   FieldFlags: 1
    value: --empty--
    desc: IRS Use Only
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Pg1Header[0].f1_5[0]
    FieldNameAlt: Date
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page1.additional_appointees %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].c1_1[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page1.appointee.addr_new %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].c1_2[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page1.appointee.phone_new %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].c1_3[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page1.appointee.fax_new %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].c1_4[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page1.specific_use_caf_recorded %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].c1_5[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page1.specific_use_details.copies %}1{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 1FieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].c1_6[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page1 and not form.page1.specific_use_details.copies %}2{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 2FieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].c1_6[1]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page1 and not form.page1.specific_use_details.revocation %}2{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 2FieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].c1_7[0]
    FieldType: Button
-   FieldFlags: 8392704
    value: {{ form.page1.appointee.name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].f1_10[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {%if form.page1.appointee.caf %}R{{ form.page1.appointee.caf }}{% endif %}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].f1_11[0]
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.appointee.ptin }}
    FieldJustification: Center
    FieldMaxLength: 11
    FieldName: topmostSubform[0].Page1[0].f1_12[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.appointee.phone }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].f1_13[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.appointee.fax }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].f1_14[0]
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page1.name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].f1_6[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.ssn }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].f1_7[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.get_phone }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].f1_8[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.plan_number }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].f1_9[0]
    FieldType: Text
