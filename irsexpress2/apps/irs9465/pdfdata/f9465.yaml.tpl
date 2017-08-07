{% load func_helpers %}
{% load misc_helpers %}

-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0]
    FieldType: ''
-   FieldFlags: 0
    value: {% if form.page3.pay_payroll %}1{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 1FieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].CheckBox1[0]
    FieldNameAlt: CheckBox1
    FieldType: Button
-   FieldFlags: 8388608
    value: {{ form.page1.country }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].LINE1A[0].f1_011[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.foreign_county }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].LINE1A[0].f1_012[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.foreign_zip }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].LINE1A[0].f1_013[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.street }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].LINE1A[0].p1-t11[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.apt }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].LINE1A[0].p1-t12[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.city_state_zip }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].LINE1A[0].p1-t13[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.first_name }} {{ form.page1.middle_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].LINE1A[0].p1-t1[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.last_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].LINE1A[0].p1-t2[0]
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.ssn }}
    FieldJustification: Center
    FieldMaxLength: 11
    FieldName: topmostSubform[0].Page1[0].LINE1A[0].p1-t3[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.jointoffer.first_name }} {{ form.page1.jointoffer.middle_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].LINE1A[0].p1-t6[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.jointoffer.last_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].LINE1A[0].p1-t7[0]
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.jointoffer.ssn }}
    FieldJustification: Center
    FieldMaxLength: 11
    FieldName: topmostSubform[0].Page1[0].LINE1A[0].p1-t8[0]
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page1.address_new %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].LINE1B[0].p1-cb1[0]
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {{ form.page2.ein }}
    FieldJustification: Center
    FieldMaxLength: 10
    FieldName: topmostSubform[0].Page1[0].Line2[0].f1_001[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.business_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line2[0].f1_002[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.phone_home }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].Line3[0].p1-t14[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.phone_home_bttc }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line3[0].p1-t16[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.phone_work }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].Line4[0].p1-t17[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.phone_work_ext }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].Line4[0].p1-t19[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.phone_work_bttc }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line4[0].p1-t20[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.bank_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line5[0].p1-t21[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.bank_street }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line5[0].p1-t22[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.bank_city_state_zip }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line5[0].p1-t23[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.employer_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line6[0].p1-t24[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.employer_street }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line6[0].p1-t25[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.employer_city_state_zip }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Line6[0].p1-t26[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.request_for_form }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].p1-t27[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.request_for_years }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].p1-t28[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.amount_owed|stringformat:"d"|intcomma_force }}
    FieldJustification: Right
    FieldName: topmostSubform[0].Page1[0].p1-t29[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.amount_owed|floatfract }}
    FieldJustification: Right
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page1[0].p1-t30[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.amount_paid|stringformat:"d"|intcomma_force }}
    FieldJustification: Right
    FieldName: topmostSubform[0].Page1[0].p1-t31[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.amount_difference|stringformat:"d"|intcomma_force }}
    FieldJustification: Right
    FieldName: topmostSubform[0].Page1[0].p1-t31[1]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.auto_can_pay|stringformat:"d"|intcomma_force }}
    FieldJustification: Right
    FieldName: topmostSubform[0].Page1[0].p1-t31[2]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.amount_paid|floatfract }}
    FieldJustification: Right
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page1[0].p1-t32[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.amount_difference|floatfract }}
    FieldJustification: Right
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page1[0].p1-t32[1]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.auto_can_pay|floatfract }}
    FieldJustification: Right
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page1[0].p1-t32[2]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.can_pay|stringformat:"d"|intcomma_force }}
    FieldJustification: Right
    FieldName: topmostSubform[0].Page1[0].p1-t33[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.can_pay|floatfract }}
    FieldJustification: Right
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page1[0].p1-t34[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.payment_day }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page1[0].p1-t35[0]
    FieldType: Text
-   FieldFlags: 25165824
    value: {{ form.page3.routing_number }}
    FieldJustification: Left
    FieldMaxLength: 9
    FieldName: topmostSubform[0].Page1[0].p1-t62a[0]
    FieldType: Text
-   FieldFlags: 25165824
    value: {{ form.page3.account_number }}
    FieldJustification: Left
    FieldMaxLength: 17
    FieldName: topmostSubform[0].Page1[0].p1-t63a[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.county.as_str }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].TextField22[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.dependents_cnt }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page2[0].p1-t31[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.has_older65 }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page2[0].p1-t31[1]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.net_income_day|stringformat:"d"|intcomma_force }}
    FieldJustification: Right
    FieldName: topmostSubform[0].Page2[0].p1-t31[2]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.spouse_net_income_day|stringformat:"d"|intcomma_force }}
    FieldJustification: Right
    FieldName: topmostSubform[0].Page2[0].p1-t31[3]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.vehicles }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page2[0].p1-t31[4]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.car_payments }}
    FieldJustification: Center
    FieldName: topmostSubform[0].Page2[0].p1-t31[5]
    FieldType: Text
-   FieldFlags: 8388608
    {% if form.page4.has_health_insurance and not form.page4.premiums_deducted %}
    value: {{ form.page4.premiums|stringformat:"d"|intcomma_force }}
    {% else %}
    value: N/A
    {% endif %}
    FieldJustification: Right
    FieldName: topmostSubform[0].Page2[0].p1-t31[6]
    FieldType: Text
-   FieldFlags: 8388608
    {% if form.page4.has_court_payments and not form.page4.court_payments_deducted %}
    value: {{ form.page4.court_payments|stringformat:"d"|intcomma_force }}
    {% else %}
    value: N/A
    {% endif %}
    FieldJustification: Right
    FieldName: topmostSubform[0].Page2[0].p1-t31[7]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.child_care|stringformat:"d"|intcomma_force }}
    FieldJustification: Right
    FieldName: topmostSubform[0].Page2[0].p1-t31[8]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.net_income_day|floatfract }}
    FieldJustification: Right
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page2[0].p1-t32[0]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.spouse_net_income_day|floatfract }}
    FieldJustification: Right
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page2[0].p1-t32[1]
    FieldType: Text
-   FieldFlags: 8388608
    {% if form.page4.has_health_insurance and not form.page4.premiums_deducted %}
    value: {{ form.page4.premiums|floatfract }}
    {% else %}
    value: N/A
    {% endif %}
    FieldJustification: Right
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page2[0].p1-t32[2]
    FieldType: Text
-   FieldFlags: 8388608
    {% if form.page4.has_court_payments and not form.page4.court_payments_deducted %}
    value: {{ form.page4.court_payments|floatfract }}
    {% else %}
    value: N/A
    {% endif %}
    FieldJustification: Right
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page2[0].p1-t32[3]
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.child_care|floatfract }}
    FieldJustification: Right
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page2[0].p1-t32[4]
    FieldType: Text
-   FieldFlags: 0
    value: {% if not form.page4.married %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page2[0].p2-cb1[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.married %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb1[1]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.married and form.page4.expenses_shared %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page2[0].p2-cb2[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.married and not form.page4.expenses_shared %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb2[1]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.pay_period == 'weekly' %}1{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 1FieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb3[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.pay_period == 'bi-weekly' %}2{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 2FieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb3[1]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.pay_period == 'monthly' %}3{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 3FieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb3[2]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.pay_period == 'twice-a-month' %}4{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 4FieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb3[3]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.spouse_pay_period == 'weekly' %}1{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 1FieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb4[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.spouse_pay_period == 'bi-weekly' %}2{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 2FieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb4[1]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.spouse_pay_period == 'monthly' %}3{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 3FieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb4[2]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.spouse_pay_period == 'twice-a-month' %}4{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 4FieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb4[3]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.has_health_insurance %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page2[0].p2-cb5[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page4.has_health_insurance %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb5[1]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.has_health_insurance and form.page4.premiums_deducted %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page2[0].p2-cb6[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.has_health_insurance and not form.page4.premiums_deducted %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb6[1]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.has_court_payments %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page2[0].p2-cb7[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page4.has_court_payments %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb7[1]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.has_court_payments and form.page4.court_payments_deducted %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page2[0].p2-cb8[0]
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.has_court_payments and not form.page4.court_payments_deducted %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].p2-cb8[1]
    FieldType: Button
