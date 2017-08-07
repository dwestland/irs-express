{% load func_helpers %}
{% load misc_helpers %}

-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page3.lawsuit_party.amount|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page1[0].#subform[6].p1_t34_6[0]
    FieldNameAlt: Line 6. Amount of Suit.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.beneficiary.amount|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page1[0].#subform[7].p1-t48_9[0]
    FieldNameAlt: Line 9a. Anticipated amount to be received.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.asset_transfer.value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page1[0].#subform[8].p3_t2_11[0]
    FieldNameAlt: Line 11. Value at Time of Transfer.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.title }}{% if form.page1.spouse %}, {{ form.page1.spouse.title }}{% endif %}
    FieldJustification: Left
    FieldMaxLength: 45
    FieldName: topmostSubform[0].Page1[0].Lines1a-b[0].p1-t4[0]
    FieldNameAlt: Section 1. Personal Information. Line 1a. Full Name of Taxpayer
        and Spouse (if applicable).
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page1.address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Lines1a-b[0].p1-t5[0]
    FieldNameAlt: Line 1b. Address (Street, City, State, ZIP code) (County of Residence).
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page1.married %}1{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 1FieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].Lines1c-2a[0].C1_01_2a[0]
    FieldNameAlt: Line 2a. Marital Status. Married.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page1.married %}Off{% else %}2{% endif %}
    FieldJustification: 'LeftFieldStateOption: 2FieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].Lines1c-2a[0].C1_01_2a[1]
    FieldNameAlt: Line 2a. Unmarried (Single, Divorced, Widowed).
    FieldType: Button
-   FieldFlags: 0
    value: {{ form.page1.phone_home|getphonecode }}
    FieldJustification: Center
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page1[0].Lines1c-2a[0].Line1c[0].p1-t6c[0]
    FieldNameAlt: Line 1c. Home Phone Number. 3 digit area code.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.phone_home|getphoneremain }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].Lines1c-2a[0].Line1c[0].p1-t7c[0]
    FieldNameAlt: Line 1c. Home Phone Number. 7 digits.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.phone_cell|getphonecode }}
    FieldJustification: Center
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page1[0].Lines1c-2a[0].Line1d[0].p1-t8d[0]
    FieldNameAlt: Line 1d. Cell Phone Number. 3 digit area code.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.phone_cell|getphoneremain }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].Lines1c-2a[0].Line1d[0].p1-t9d[0]
    FieldNameAlt: Line 1d. Cell Phone Number. 7 digits.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.phone_work|getphonecode }}
    FieldJustification: Center
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page1[0].Lines1c-2a[0].Line1e[0].p1-t10e[0]
    FieldNameAlt: Line 1e. Business Phone Number. 3 digit area code.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.phone_work|getphoneremain }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].Lines1c-2a[0].Line1e[0].p1-t11e[0]
    FieldNameAlt: Line 1e. Business Phone Number. 7 digits.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.phone_work_cell|getphonecode }}
    FieldJustification: Center
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page1[0].Lines1c-2a[0].Line1f[0].p1-t12f[0]
    FieldNameAlt: Line 1f. Business Cell Phone Number. 3 digit area code.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.phone_work_cell|getphoneremain }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].Lines1c-2a[0].Line1f[0].p1-t13f[0]
    FieldNameAlt: Line 1f. Business Cell Phone Number. 7 digits.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Spouse\
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page2.spouse_employment_info.phone_work|getphoneremain }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].#subform[0].p1-t25_5c[0]
    FieldNameAlt: Line 5c. Work Telephone Number. 7 digits.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page2.spouse_employment_info.phone_work|getphonecode }}
    FieldJustification: Center
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].#subform[0].p1_t24_5c[0]
    FieldNameAlt: Line 5c. Work Telephone Number. 3 digit area code.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page2.spouse_employment_info.long_work_years }}
    FieldJustification: Right
    FieldMaxLength: 2
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].Line5e[0].p1_t26_5e[0]
    FieldNameAlt: Line 5e. How long with this employer. Years.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page2.spouse_employment_info.long_work_month }}
    FieldJustification: Right
    FieldMaxLength: 2
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].Line5e[0].p1_t27_5e[0]
    FieldNameAlt: Line 5e. How long with this employer. Months.
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page2.spouse_employment_info.contact_at_work_allowed %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].c1_5d_[0]
    FieldNameAlt: Line 5d. Does employer allow contact at work. Yes.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page2.spouse_employment_info.contact_at_work_allowed %}Off{% else %}No{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].c1_5d_[1]
    FieldNameAlt: Line 5d. No.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page2.spouse_employment_info.pay_period == 'weekly' %}Weekly{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Weekly'
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].c1_5h_[0]
    FieldNameAlt: 'Line 5h. Pay Period: Weekly.'
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page2.spouse_employment_info.pay_period == 'monthly' %}Monthly{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: MonthlyFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].c1_5h_[1]
    FieldNameAlt: Line 5h. Monthly.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page2.spouse_employment_info.pay_period == 'bi-weekly' %}Bi-weekly{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: Bi-weeklyFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].c1_5h_[2]
    FieldNameAlt: Line 5h. Bi-Weekly.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page2.spouse_employment_info.pay_period == 'other' %}Other{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Other'
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].c1_5h_[3]
    FieldNameAlt: Line 5h. Other.
    FieldType: Button
-   FieldFlags: 0
    value: {{ form.page2.spouse_employment_info.employer_name }}
    FieldJustification: Left
    FieldMaxLength: 45
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].p1_t23_5a[0]
    FieldNameAlt: Line 5a. Spouse's Employer Name.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page2.spouse_employment_info.address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].p1_t24_5b[0]
    FieldNameAlt: Line 5b. Address (Street, city, state, and ZIP code).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page2.spouse_employment_info.occupation }}
    FieldJustification: Left
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].p1_t28_5f[0]
    FieldNameAlt: Line 5f. Occupation.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page2.spouse_employment_info.w4extemptions }}
    FieldJustification: Center
    FieldMaxLength: 10
    FieldName: topmostSubform[0].Page1[0].Spouse\.L5a-h[0].p1_t29_5g[0]
    FieldNameAlt: Line 5g. Number of withholding allowances claimed on Form W-4.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Table_Part4-Line5[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page1.ssn }}
    FieldJustification: Center
    FieldMaxLength: 11
    FieldName: topmostSubform[0].Page1[0].Table_Part4-Line5[0].Row1[0].F02_030_0_[0]
    FieldNameAlt: Line 3a. Taxpayer. Social Security Number (S S N).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.birthdate|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].Table_Part4-Line5[0].Row1[0].F02_031_0_[0]
    FieldNameAlt: Line 3a. Taxpayer. Date of Birth (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.driverlicense }}
    FieldJustification: Left
    FieldMaxLength: 60
    FieldName: topmostSubform[0].Page1[0].Table_Part4-Line5[0].Row1[0].F02_032_0_[0]
    FieldNameAlt: Line 3a. Taxpayer. Driver's License Number and State.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.spouse.ssn }}
    FieldJustification: Center
    FieldMaxLength: 11
    FieldName: topmostSubform[0].Page1[0].Table_Part4-Line5[0].Row2[0].F02_034_0_[0]
    FieldNameAlt: Line 3b. Spouse. Social Security Number (S S N).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.spouse.birthdate|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].Table_Part4-Line5[0].Row2[0].F02_035_0_[0]
    FieldNameAlt: Line 3b. Spouse. Date of Birth (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.spouse.driverlicense }}
    FieldJustification: Left
    FieldMaxLength: 60
    FieldName: topmostSubform[0].Page1[0].Table_Part4-Line5[0].Row2[0].F02_036_0_[0]
    FieldNameAlt: Line 3b. Spouse. Driver's License Number and State.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Taxpayer\
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page2.employment_info.phone_work|getphonecode }}
    FieldJustification: Center
    FieldMaxLength: 3
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].Line4cWork[0].p1-t17_4c[0]
    FieldNameAlt: Line 4c. Work Telephone Number. 3 digit area code.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page2.employment_info.phone_work|getphoneremain }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].Line4cWork[0].p1-t18_4c[0]
    FieldNameAlt: Line 4c. Work Telephone Number. 7 digits.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page2.employment_info.long_work_years }}
    FieldJustification: Right
    FieldMaxLength: 2
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].Line4e[0].p1_t19_4e[0]
    FieldNameAlt: Line 4e. How long with this employer. Years.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page2.employment_info.long_work_month }}
    FieldJustification: Right
    FieldMaxLength: 2
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].Line4e[0].p1_t20_4e[0]
    FieldNameAlt: Line 4e. Months.
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page2.employment_info.contact_at_work_allowed %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].c1_4d_[0]
    FieldNameAlt: Line 4d. Does employer allow contact at work. Yes.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page2.employment_info.contact_at_work_allowed %}Off{% else %}No{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].c1_4d_[1]
    FieldNameAlt: Line 4d. No.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page2.employment_info.pay_period == 'weekly' %}Weekly{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Weekly'
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].c1_4h_[0]
    FieldNameAlt: 'Line 4h. Pay Period: Weekly.'
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page2.employment_info.pay_period == 'monthly' %}Monthly{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: MonthlyFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].c1_4h_[1]
    FieldNameAlt: Line 4h. Monthly.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page2.employment_info.pay_period == 'bi-weekly' %}Bi-weekly{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: Bi-weeklyFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].c1_4h_[2]
    FieldNameAlt: Line 4h. Bi-Weekly.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page2.employment_info.pay_period == 'other' %}Other{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Other'
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].c1_4h_[3]
    FieldNameAlt: Line 4h. Other.
    FieldType: Button
-   FieldFlags: 0
    value: {{ form.page2.employment_info.employer_name }}
    FieldJustification: Left
    FieldMaxLength: 45
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].p1_t15_4a[0]
    FieldNameAlt: Section 2. Employment Information for Wage Earners. Line 4a. Taxpayer's
        Employer Name.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page2.employment_info.address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].p1_t16_4b[0]
    FieldNameAlt: Line 4b. Address (Street, city, state, and ZIP code).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page2.employment_info.occupation }}
    FieldJustification: Left
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].p1_t21_4f[0]
    FieldNameAlt: Line 4f. Occupation
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page2.employment_info.w4extemptions }}
    FieldJustification: Center
    FieldMaxLength: 10
    FieldName: topmostSubform[0].Page1[0].Taxpayer\.L4a-h[0].p1_t22_4g[0]
    FieldNameAlt: Line 4g. Number of withholding allowances claimed on Form W-4.
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page3.safe %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].c1_10_[0]
    FieldNameAlt: Line 10. Do you have a safe deposit box (business or personal)?
        (If yes, answer the following.) Yes.
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page3.safe %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].c1_10_[1]
    FieldNameAlt: Line 10. No.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page3.asset_transfer %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].c1_11_[0]
    FieldNameAlt: Line 11. In the past 10 years, have you transferred any assets for
        less than their full value? (If yes, answer the following.) Yes.
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page3.asset_transfer %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].c1_11_[1]
    FieldNameAlt: 'Line 11. No. '
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page3.lawsuit_party %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].c1_6_[0]
    FieldNameAlt: Section 3. Line 6. Other Financial Information (Attach copies of
        applicable documentation.). Are you a party to a lawsuit (If yes, answer the
        following). Yes.
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page3.lawsuit_party %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].c1_6_[1]
    FieldNameAlt: Line 6. No.
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page3.lawsuit_party.is_defendant %}Plaintiff{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Plaintiff'
    FieldName: topmostSubform[0].Page1[0].c1_6a_[0]
    FieldNameAlt: Line 6. Plaintiff.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page3.lawsuit_party.is_defendant %}Defendant{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: DefendantFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].c1_6a_[1]
    FieldNameAlt: Line 6. Defendant.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page3.bankruptcy %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].c1_7_[0]
    FieldNameAlt: Line 7. Have you ever filed bankruptcy (If yes, answer the following).
        Yes.
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page3.bankruptcy %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].c1_7_[1]
    FieldNameAlt: Line 7. No.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page3.liveabroad %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].c1_8_[0]
    FieldNameAlt: Line 8. In the past 10 years, have you lived outside of the U. S.
        for 6 months or longer (If yes, answer the following). Yes.
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page3.liveabroad %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].c1_8_[1]
    FieldNameAlt: Line 8. No.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page3.beneficiary %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].c1_9a_[0]
    FieldNameAlt: Line 9a. Are you the beneficiary of a trust, estate, or life insurance
        policy? (If yes, answer the following.) Yes.
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page3.beneficiary %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].c1_9a_[1]
    FieldNameAlt: Line 9a. No.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page3.trustee %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page1[0].c1_9b_[0]
    FieldNameAlt: Line 9b. Are you a trustee, fiduciary or contributor of trust? Yes.
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page3.trustee %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page1[0].c1_9b_[1]
    FieldNameAlt: Line 9b. No.
    FieldType: Button
-   FieldFlags: 0
    value: {{ form.page3.trustee.ein|substr:2 }}
    FieldJustification: Left
    FieldMaxLength: 7
    FieldName: topmostSubform[0].Page1[0].p1-t01_9b[0]
    FieldNameAlt: Line 9b. EIN. Last 7 digits.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.trustee.ein|substr:0 }}
    FieldJustification: Left
    FieldMaxLength: 2
    FieldName: topmostSubform[0].Page1[0].p1-t02_9b[0]
    FieldNameAlt: Line 9b. EIN. First 2 digits.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page1.dependents_str }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1-t14b_2b[0]
    FieldNameAlt: Line 2b. Name, Age, and Relationship of dependent (or dependents).
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.title }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1-t1[0]
    FieldNameAlt: Page 1. Name on Internal Revenue Service (I R S) Account.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.ssn }}
    FieldJustification: Center
    FieldMaxLength: 11
    FieldName: topmostSubform[0].Page1[0].p1-t2[0]
    FieldNameAlt: Page 1. Social Security Number S S N on I R S Account.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.ein }}
    FieldJustification: Center
    FieldMaxLength: 10
    FieldName: topmostSubform[0].Page1[0].p1-t3[0]
    FieldNameAlt: Page 1. Employer identification Number E I N.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.safe.value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page1[0].p1-t42_10[0]
    FieldNameAlt: Line 10. Value.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page3.safe.contents }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1-t43_10[0]
    FieldNameAlt: Line 10. Contents.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.beneficiary.ein|substr:0 }}
    FieldJustification: Left
    FieldMaxLength: 2
    FieldName: topmostSubform[0].Page1[0].p1-t45_9[0]
    FieldNameAlt: Line 9a. EIN. First 2 digits.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.beneficiary.ein|substr:2 }}
    FieldJustification: Left
    FieldMaxLength: 7
    FieldName: topmostSubform[0].Page1[0].p1-t46_9[0]
    FieldNameAlt: Line 9a. EIN. Last 8 digits.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.beneficiary.name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1-t47_9[0]
    FieldNameAlt: Line 9a. Name of the trust, estate, or policy.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.beneficiary.whenreceive }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1-t49_9[0]
    FieldNameAlt: Line 9a. When will the amount be received.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.lawsuit_party.location }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1_t30_6[0]
    FieldNameAlt: Line 6. Location of Filing.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.lawsuit_party.representer }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1_t31_6[0]
    FieldNameAlt: Line 6. Represented by.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.lawsuit_party.case_number }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1_t32_6[0]
    FieldNameAlt: Line 6. Docket / Case Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.lawsuit_party.completion_date|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].p1_t35_6[0]
    FieldNameAlt: Line 6. Possible Completion Date (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.lawsuit_party.subject }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1_t36_6[0]
    FieldNameAlt: Line 6. Subject of Suit.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.bankruptcy.filed|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].p1_t37_7[0]
    FieldNameAlt: Line 7. Date Filed (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.bankruptcy.dismissed|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].p1_t38_7[0]
    FieldNameAlt: Line 7. Date Dismissed (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.bankruptcy.discharged|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].p1_t38_7[1]
    FieldNameAlt: Line 7. Date Discharged (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.bankruptcy.petition_number }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1_t39_7[0]
    FieldNameAlt: Line 7. Petition Number.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.bankruptcy.location }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1_t40_7[0]
    FieldNameAlt: Line 7. Location Filed.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page3.safe.location }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1_t41_10[0]
    FieldNameAlt: Line 10. Location (Name, Address and box number).
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.beneficiary.place }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p1_t44_9[0]
    FieldNameAlt: Line 9a. Place where recorded.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page3.trustee.name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p2_t00_9b[0]
    FieldNameAlt: Line 9b. Name of the trust.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.liveabroad.date_from|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].p2_t50_8[0]
    FieldNameAlt: 'Line 8. Dates lived abroad: from (m m d d y y y y).'
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.liveabroad.date_to|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].p2_t51_8[0]
    FieldNameAlt: 'Line 8. Dates lived abroad: to (m m d d y y y y).'
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page3.asset_transfer.assetlist }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p3_t1_11[0]
    FieldNameAlt: Line 11. List Asset (or Assets).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page3.asset_transfer.date|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page1[0].p3_t3_11[0]
    FieldNameAlt: Line 11. Date Transferred (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page3.asset_transfer.recipient }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page1[0].p3_t4_11[0]
    FieldNameAlt: Line 11. To Whom or Where was it Transferred.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0]
    FieldType: ''
-   FieldFlags: 8392704
    value: {{ form.page4.insurance_info_1.name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column1[0].p2_t30_16[0]
    FieldNameAlt: Line 16b. Name and Address of Insurance Company (or Companies).
        Name and Address of Insurance Company. First Company.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.insurance_info_1.policy_number }}
    FieldJustification: Left
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column1[0].p2_t33_16c[0]
    FieldNameAlt: Line 16c. Policy Number (or Numbers). First Company.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page4.insurance_info_1.policy_owner }}
    FieldJustification: Left
    FieldMaxLength: 20
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column1[0].p2_t36_16d[0]
    FieldNameAlt: Line 16d. Owner of Policy. First Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.insurance_info_1.cash_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column1[0].p2_t39_16e[0]
    FieldNameAlt: Line 16e. Current Cash Value. First Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.insurance_info_1.loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column1[0].p2_t42_16f[0]
    FieldNameAlt: Line 16f. Outstanding Loan Balance. First Company.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page4.insurance_info_2.name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column2[0].p2_t31_16[0]
    FieldNameAlt: Line 16b. Name and Address of Insurance Company. Second Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.insurance_info_2.policy_number }}
    FieldJustification: Left
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column2[0].p2_t34_16c[0]
    FieldNameAlt: Line 16c. Policy Number (or Numbers). Second Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.insurance_info_2.policy_owner }}
    FieldJustification: Left
    FieldMaxLength: 20
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column2[0].p2_t37_16d[0]
    FieldNameAlt: Line 16d. Owner of Policy. Second Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.insurance_info_2.cash_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column2[0].p2_t40_16e[0]
    FieldNameAlt: Line 16e. Current Cash Value. Second Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.insurance_info_2.loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column2[0].p2_t43_16f[0]
    FieldNameAlt: Line 16f. Outstanding Loan Balance. Second Company.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page4.insurance_info_3.name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column3[0].p2_t32_16[0]
    FieldNameAlt: Line 16b. Name and Address of Insurance Company. Third Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.insurance_info_3.policy_number }}
    FieldJustification: Left
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column3[0].p2_t35_16c[0]
    FieldNameAlt: Line 16c. Policy Number (or Numbers). Third Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.insurance_info_3.policy_owner }}
    FieldJustification: Left
    FieldMaxLength: 20
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column3[0].p2_t38_16d[0]
    FieldNameAlt: Line 16d. Owner of Policy. Third Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.insurance_info_3.cash_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column3[0].p2_t41_16e[0]
    FieldNameAlt: Line 16e. Current Cash Value. Third Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.insurance_info_3.loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Lines16b-f[0].Lines16b-f_Column3[0].p2_t44_16f[0]
    FieldNameAlt: Line 16f. Outstanding Loan Balance. Third Company.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0]
    FieldType: ''
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page4.bank_balance_date|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12[0].AcctBal12[0].F02_001_11[0]
    FieldNameAlt: PERSONAL BANK ACCOUNTS  Include all checking, online and mobile
        (for example, PayPal) accounts, money market accounts, savings accounts, and
        stored value cards (for example, payroll cards, government benefit cards,
        etcetera). Account Balance as of (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.bank_account_info_1.account_type }}
    FieldJustification: Left
    FieldMaxLength: 18
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12a[0].Line12A[0]
    FieldNameAlt: Line 13a. Type of Account.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page4.bank_account_info_1.name_address }}
    FieldJustification: Left
    FieldMaxLength: 86
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12a[0].p2-t2_12[0]
    FieldNameAlt: Line 13a. Full Name and Address (Street, City, State, ZIP code)
        of Bank, Savings and Loan, Credit Union, or Financial Institution.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.bank_account_info_1.account_number }}
    FieldJustification: Left
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12a[0].p2-t3_12[0]
    FieldNameAlt: Line 13a. Account Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.bank_account_info_1.account_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12a[0].p2-t4_12[0]
    FieldNameAlt: 'Line 13a. Account Balance. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.bank_account_info_2.account_type }}
    FieldJustification: Left
    FieldMaxLength: 18
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12b[0].Line12B[0]
    FieldNameAlt: Line 13b. Type of Account.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page4.bank_account_info_2.name_address }}
    FieldJustification: Left
    FieldMaxLength: 86
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12b[0].p2-t5_12[0]
    FieldNameAlt: Line 13b. Full Name and Address (Street, City, State, ZIP code)
        of Bank, Savings and Loan, Credit Union, or Financial Institution.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.bank_account_info_2.account_number }}
    FieldJustification: Left
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12b[0].p2-t6_12[0]
    FieldNameAlt: Line 13b. Account Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.bank_account_info_2.account_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12b[0].p2-t7_12[0]
    FieldNameAlt: 'Line 13b. Account Balance. '
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page4.bank_account_info_3.name_address }}
    FieldJustification: Left
    FieldMaxLength: 86
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12b[1].p2-t5_13c2[0]
    FieldNameAlt: Line 13c. Full Name and Address (Street, City, State, ZIP code)
        of Bank, Savings and Loan, Credit Union, or Financial Institution.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.bank_account_info_3.account_number }}
    FieldJustification: Left
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12b[1].p2-t5_13c3[0]
    FieldNameAlt: Line 13c. Account Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.bank_account_info_3.account_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12b[1].p2-t5_13c4[0]
    FieldNameAlt: 'Line 13c. Account Balance. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.bank_account_info_3.account_type }}
    FieldJustification: Left
    FieldMaxLength: 18
    FieldName: topmostSubform[0].Page2[0].Table_Line13[0].Line12b[1].p2-t5_13c[0]
    FieldNameAlt: Line 13c. Type of Account.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0]
    FieldType: ''
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].HeaderRow[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page4.loan_balance_date|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].HeaderRow[0].LoanBal[0].p2-t9_13[0]
    FieldNameAlt: Section 4. INVESTMENTS. Include stocks, bonds, mutual funds, stock
        options, certificates of deposit, and retirement assets such as IRAs, Keogh,
        and 401(k) plans. Include all corporations, partnerships, limited liability
        companies, or other business entities in which you are an officer, director,
        owner, member, or otherwise have a financial interest. Loan Balance (if applicable)
        As of (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page4.investment_info_1.name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13a[0].#subform[0].p2-t61_13a[0]
    FieldNameAlt: Line 14a. Full Name and Address (Street, City, State, ZIP code)
        of Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.investment_info_1.phone }}
    FieldJustification: Left
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13a[0].#subform[0].p2_t10_13a[0]
    FieldNameAlt: Line 14a. Phone.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page4.investment_info_1.investment_type }}
    FieldJustification: Left
    FieldMaxLength: 54
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13a[0].Line13A[0]
    FieldNameAlt: Line 14a. Type of Investment or Financial Interest.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.investment_info_1.equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13a[0].p2_t11_13a[0]
    FieldNameAlt: Line 14a. Equity. Value minus Loan.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.investment_info_1.loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13a[0].p2_t12_13a[0]
    FieldNameAlt: 'Line 14a. Loan Balance (if applicable). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.investment_info_1.current_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13a[0].p2_t13_13a[0]
    FieldNameAlt: Line 14a. Current Value.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page4.investment_info_2.name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13b[0].#subform[0].p2-t62_13b[0]
    FieldNameAlt: Line 14b. Full Name and Address (Street, City, State, ZIP code)
        of Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.investment_info_2.phone }}
    FieldJustification: Left
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13b[0].#subform[0].p2_t14_13b[0]
    FieldNameAlt: Line 14b. Phone.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page4.investment_info_2.investment_type }}
    FieldJustification: Left
    FieldMaxLength: 54
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13b[0].Line13B[0]
    FieldNameAlt: Line 14b. Type of Investment or Financial Interest.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.investment_info_2.equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13b[0].p2_t15_13b[0]
    FieldNameAlt: Line 14b. Equity. Value minus Loan.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.investment_info_2.loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13b[0].p2_t16_13b[0]
    FieldNameAlt: Line 14b. Loan Balance (if applicable).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.investment_info_2.current_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13b[0].p2_t17_13b[0]
    FieldNameAlt: Line 14b. Current Value.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page4.investment_info_3.name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13c[0].#subform[0].p2-t63_13c[0]
    FieldNameAlt: Line 14c. Full Name and Address (Street, City, State, ZIP code)
        of Company.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.investment_info_3.phone }}
    FieldJustification: Left
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13c[0].#subform[0].p2_t18_13c[0]
    FieldNameAlt: Line 14c. Phone.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page4.investment_info_3.investment_type }}
    FieldJustification: Left
    FieldMaxLength: 54
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13c[0].Line13C[0]
    FieldNameAlt: Line 14c. Type of Investment or Financial Interest.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.investment_info_3.equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13c[0].p2_t19_13c[0]
    FieldNameAlt: Line 14c. Equity. Value minus Loan.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.investment_info_3.loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13c[0].p2_t20_13c[0]
    FieldNameAlt: 'Line 14c. Loan Balance (if applicable). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.investment_info_3.current_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line14[0].Row13c[0].p2_t21_13c[0]
    FieldNameAlt: Line 14c. Current Value.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0]
    FieldType: ''
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].HeaderRow14[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page4.cc_amount_owed_date|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].HeaderRow14[0].Column3_14[0].F02_001_14[0]
    FieldNameAlt: Section 4. AVAILABLE CREDIT. Include all lines of credit and bank
        issued credit cards. Full Name and Address (Street, City, State, ZIP code)
        of Credit Institution. Amount owed as of (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.cc_available_credit_date|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].HeaderRow14[0].Column4_14[0].F02_002_14[0]
    FieldNameAlt: Available credit as of (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.credit_info_2.account_number }}
    FieldJustification: Left
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].Line14b[0].Line14b[0].Line14B[0]
    FieldNameAlt: Line 15b. Account Number.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page4.credit_info_2.name_address }}
    FieldJustification: Left
    FieldMaxLength: 189
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].Line14b[0].Line14b[0].p2-t73_14b[0]
    FieldNameAlt: Line 15b. Full Name and Address (Street, City, State, ZIP code)
        of Credit Institution.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.credit_info_2.credit_limit|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].Line14b[0].p2_t26_14b[0]
    FieldNameAlt: Line 15b. Credit Limit.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.credit_info_2.amount_owed|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].Line14b[0].p2_t27_14b[0]
    FieldNameAlt: Line 15b. Amount owed.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.credit_info_2.available_credit|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].Line14b[0].p2_t28_14b[0]
    FieldNameAlt: Line 15b. Available credit.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.credit_info_1.account_number }}
    FieldJustification: Left
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].Lines14a[0].Line14a[0].AcctNo14A[0]
    FieldNameAlt: Line 15a. Account Number.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page4.credit_info_1.name_address }}
    FieldJustification: Left
    FieldMaxLength: 189
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].Lines14a[0].Line14a[0].p2-t72_14a[0]
    FieldNameAlt: Line 15a. Full Name and Address (Street, City, State, ZIP code)
        of Credit Institution.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.credit_info_1.credit_limit|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].Lines14a[0].p2_t23_14a[0]
    FieldNameAlt: Line 15a. Credit Limit.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.credit_info_1.amount_owed|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].Lines14a[0].p2_t24_14a[0]
    FieldNameAlt: Line 15a. Amount owed.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.credit_info_1.available_credit|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].Table_Line15[0].Lines14a[0].p2_t25_14a[0]
    FieldNameAlt: Line 15a. Available credit.
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page4.insurances.count > 0 %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page2[0].c1_07_0_[0]
    FieldNameAlt: 'Line 16a. Life Insurance: Do you own or have any interest in any
        life insurance policies with cash value (Term Life insurance does not have
        a cash value). Yes. If yes, complete blocks 16b through 16f for each policy.'
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page4.insurances.count == 0 %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page2[0].c1_07_0_[1]
    FieldNameAlt: Line 16a. No.
    FieldType: Button
-   FieldFlags: 0
    value: {{ form.page4.cash_on_hand|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page2[0].p2-t1_11[0]
    FieldNameAlt: Page 2. Section 4. Personal Asset Information for All Individuals.
        Line 12. Cash on Hand. Include cash that is not in a blank. Total Cash on
        Hand.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.total_cash|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page2[0].p2-t8_12c[0]
    FieldNameAlt: Line 13d. Total Cash (Add lines 13a through 13c, and amounts from
        any attachments).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.total_equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page2[0].p2_t22_13d[0]
    FieldNameAlt: Line 14d. Total Equity (Add lines 14a through 14c and amounts from
        any attachments).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.total_credit|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page2[0].p2_t29_14c[0]
    FieldNameAlt: Line 15c. Total Available Credit (Add lines 15a, 15b and amounts
        from any attachments).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page4.total_available_cash|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page2[0].p2_t45_15g[0]
    FieldNameAlt: Line 16g. Total Available Cash. (Subtract amounts on line 16f from
        line 16e and include amounts from any attachments).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_1.lender_phone }}
    FieldJustification: Left
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].#subform[1].p2_t18_13c[0]
    FieldNameAlt: Line 17a. Phone.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page5.realproperty_info_1.lender_name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].#subform[1].p3_t12_17a[0]
    FieldNameAlt: Line 17a. Lender / Contract Holder Name, Address, (Street, City,
        State, ZIP code) and Phone.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_2.lender_phone }}
    FieldJustification: Left
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].#subform[3].p2_t18_13c[1]
    FieldNameAlt: Line 17b. Phone.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page5.realproperty_info_2.lender_name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].#subform[3].p3_t19_17b[0]
    FieldNameAlt: Line 17b. Lender / Contract Holder Name, Address, (Street, City,
        State, ZIP code) and Phone.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_1.monthly_payment|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].AmountPayment[0].p3_t26_18a[0]
    FieldNameAlt: Line 18a. Amount of Monthly Payment.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_1.market_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].CurrentFMV[0].p3_t24_18a[0]
    FieldNameAlt: Line 18a. Current Fair Market Value (F M V).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_1.current_loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].CurrentLoan[0].p3_t25_18a[0]
    FieldNameAlt: Line 18a. Current Loan Balance.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_1.final_payment_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page3[0].DateFinal[0].p3_t27_18a[0]
    FieldNameAlt: Line 18a. Date of Final Payment (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_1.equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Equity[0].p3_t28_18a[0]
    FieldNameAlt: Line 18a. Equity. F M V Minus Loan.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_2.lender_phone }}
    FieldJustification: Left
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Lender-phone18b[0].p2_t18_13c[0]
    FieldNameAlt: Line 18b. Phone.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page5.vehicle_info_2.lender_name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].Lender-phone18b[0].p3_t39_18bLLN[0]
    FieldNameAlt: Line 18b. Lender / Lessor Name, Address, (Street, City, State, ZIP
        code) and Phone.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_1.lender_phone }}
    FieldJustification: Left
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Lender-phone3[0].p2_t18_13c[0]
    FieldNameAlt: Line 19a. Phone.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page5.personalasset_info_1.lender_name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].Lender-phone3[0].p3_t55_19bLLNA[0]
    FieldNameAlt: Line 19a. Lender/Lessor Name, Address, (Street, City, State, ZIP
        code) and Phone.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_2.lender_phone }}
    FieldJustification: Left
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Lender-phone4[0].p2_t18_13c[0]
    FieldNameAlt: Line 19b. Phone.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page5.personalasset_info_2.lender_name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].Lender-phone4[0].p3_t48_19aLLNAS[0]
    FieldNameAlt: Line 19b. Lender/Lessor Name, Address, (Street, City, State, ZIP
        code) and Phone.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_1.lender_phone }}
    FieldJustification: Left
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Lender-phone[0].p2_t18_13c[0]
    FieldNameAlt: Line 18a. Phone.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page5.vehicle_info_1.lender_name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].Lender-phone[0].p3_t30_18a[0]
    FieldNameAlt: Line 18a. Lender / Lessor Name, Address, (Street, City, State, ZIP
        code) and Phone.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_1.mileage }}
    FieldJustification: Left
    FieldMaxLength: 7
    FieldName: topmostSubform[0].Page3[0].Line18a[0].Line18aMKMDL[0]
    FieldNameAlt: Line 18a. Mileage.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_1.year }}
    FieldJustification: Left
    FieldMaxLength: 4
    FieldName: topmostSubform[0].Page3[0].Line18a[0].p3_t21_18aYR[0]
    FieldNameAlt: Section 4. Personal Vehicles Leased or Purchased. Include boats,
        R V's, motorcycles, all-terrain and off-road vehicles, trailers, etcetera.
        Line 18a. Description (Year, Mileage, Make/Model, Tag Number, Vehicle Identification
        Number). Year.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_1.get_make_model }}
    FieldJustification: Left
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page3[0].Line18a[0].p3_t22_18aMILE[0]
    FieldNameAlt: Line 18a. Make / Model.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_1.license_number }}
    FieldJustification: Left
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page3[0].Line18a[0].p3_t29_18aTGNUM[0]
    FieldNameAlt: Line 18a. License / Tag Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_1.vin }}
    FieldJustification: Left
    FieldMaxLength: 32
    FieldName: topmostSubform[0].Page3[0].Line18a[0].p3_t29_18aVIN[0]
    FieldNameAlt: Line 18a. Vehicle Identification Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_2.mileage }}
    FieldJustification: Left
    FieldMaxLength: 7
    FieldName: topmostSubform[0].Page3[0].Line18b[0].Line18b[0]
    FieldNameAlt: Line 18b. Mileage.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_2.year }}
    FieldJustification: Left
    FieldMaxLength: 4
    FieldName: topmostSubform[0].Page3[0].Line18b[0].p3_t00_18bYR[0]
    FieldNameAlt: Line 18b. Year.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_2.vin }}
    FieldJustification: Left
    FieldMaxLength: 32
    FieldName: topmostSubform[0].Page3[0].Line18b[0].p3_t29_18bVIN[0]
    FieldNameAlt: Line 18b. Vehicle Identification Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_2.get_make_model }}
    FieldJustification: Left
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page3[0].Line18b[0].p3_t31_18bMILE[0]
    FieldNameAlt: Line 18b. Make / Model.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_2.license_number }}
    FieldJustification: Left
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page3[0].Line18b[0].p3_t38_18b[0]
    FieldNameAlt: Line 18b. License / Tag Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_1.purchase_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page3[0].Purchase[0].p3_t23_18a[0]
    FieldNameAlt: Line 18a. Purchase/Lease Date (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].Table_Line17a[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_1.description }}
    FieldJustification: Left
    FieldMaxLength: 45
    FieldName: topmostSubform[0].Page3[0].Table_Line17a[0].Line17a[0].Line17[0]
    FieldNameAlt: Page 3. Section 4. Personal Asset Information for All Individuals.  Real
        Property. Include all real property owned or being purchased. Line 17a. Property
        Description.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_1.equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line17a[0].Line17a[0].p3_t10_17a[0]
    FieldNameAlt: Line 17a. Equity. F M V Minus Loan.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_1.purchase_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page3[0].Table_Line17a[0].Line17a[0].p3_t5_17a[0]
    FieldNameAlt: Line 17a. Purchase Date (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_1.market_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line17a[0].Line17a[0].p3_t6_17a[0]
    FieldNameAlt: Line 17a. Current Fair Market Value (F M V).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_1.current_loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line17a[0].Line17a[0].p3_t7_17a[0]
    FieldNameAlt: Line 17a. Current Loan Balance.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_1.monthly_payment|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line17a[0].Line17a[0].p3_t8_17a[0]
    FieldNameAlt: Line 17a. Amount of Monthly Payment.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_1.final_payment_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page3[0].Table_Line17a[0].Line17a[0].p3_t9_17a[0]
    FieldNameAlt: Line 17a. Date of Final Payment (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].Table_Line17b[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_2.description }}
    FieldJustification: Left
    FieldMaxLength: 36
    FieldName: topmostSubform[0].Page3[0].Table_Line17b[0].Line17b[0].Line17b[0]
    FieldNameAlt: Line 17b. Property Description.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_2.purchase_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page3[0].Table_Line17b[0].Line17b[0].p3_t13_17b[0]
    FieldNameAlt: Line 17b. Purchase Date (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_2.market_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line17b[0].Line17b[0].p3_t14_17b[0]
    FieldNameAlt: Line 17b. Current Fair Market Value (F M V).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_2.current_loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line17b[0].Line17b[0].p3_t15_17b[0]
    FieldNameAlt: Line 17b. Current Loan Balance.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_2.monthly_payment|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line17b[0].Line17b[0].p3_t16_17b[0]
    FieldNameAlt: Line 17b. Amount of Monthly Payment.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_2.final_payment_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page3[0].Table_Line17b[0].Line17b[0].p3_t17_17b[0]
    FieldNameAlt: Line 17b. Date of Final Payment (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.realproperty_info_2.equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line17b[0].Line17b[0].p3_t18_17b[0]
    FieldNameAlt: Line 17b. Equity. F M V Minus Loan.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].Table_Line19a[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_1.description }}
    FieldJustification: Left
    FieldMaxLength: 36
    FieldName: topmostSubform[0].Page3[0].Table_Line19a[0].Row1[0].Line19a[0]
    FieldNameAlt: Section 4. Personal Assets. Include all furniture, personal effects,
        artwork, jewelry, collections (coins, guns, etcetera), antiques or other assets.
        Include intangible assets such as licenses, domain names, patents, copyrights,
        mining claims, etcetera. Line 19a. Property Description.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_1.purchase_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page3[0].Table_Line19a[0].Row1[0].p3_t41_19a[0]
    FieldNameAlt: Line 19a. Purchase/Lease Date (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_1.market_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line19a[0].Row1[0].p3_t42_19a[0]
    FieldNameAlt: Line 19a. Current Fair Market Value (F M V).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_1.current_loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line19a[0].Row1[0].p3_t43_19a[0]
    FieldNameAlt: Line 19a. Current Loan Balance.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_1.monthly_payment|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line19a[0].Row1[0].p3_t44_19a[0]
    FieldNameAlt: Line 19a. Amount of Monthly Payment.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_1.final_payment_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page3[0].Table_Line19a[0].Row1[0].p3_t45_19a[0]
    FieldNameAlt: Line 19a. Date of Final Payment (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_1.equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line19a[0].Row1[0].p3_t46_19a[0]
    FieldNameAlt: Line 19a. Equity. F M V Minus Loan.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].Table_Line19b[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_2.description }}
    FieldJustification: Left
    FieldMaxLength: 36
    FieldName: topmostSubform[0].Page3[0].Table_Line19b[0].Line19b[0].Line19b[0]
    FieldNameAlt: Line 19b. Property Description.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_2.purchase_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page3[0].Table_Line19b[0].Line19b[0].p3_t49_19b[0]
    FieldNameAlt: Line 19b. Purchase/Lease Date (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_2.market_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line19b[0].Line19b[0].p3_t50_19b[0]
    FieldNameAlt: Line 19b. Current Fair Market Value (F M V).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_2.current_loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line19b[0].Line19b[0].p3_t51_19b[0]
    FieldNameAlt: Line 19b. Current Loan Balance.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_2.monthly_payment|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line19b[0].Line19b[0].p3_t52_19b[0]
    FieldNameAlt: Line 19b. Amount of Monthly Payment.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_2.final_payment_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page3[0].Table_Line19b[0].Line19b[0].p3_t53_19b[0]
    FieldNameAlt: Line 19b. Date of Final Payment (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personalasset_info_2.equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].Table_Line19b[0].Line19b[0].p3_t54_19b[0]
    FieldNameAlt: Line 19b. Equity. F M V Minus Loan.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page5.realproperty_info_1.location_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].p3_t11_17a[0]
    FieldNameAlt: Line 17a. Location (Street, City, State, ZIP code) and County.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page5.realproperty_info_2.location_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].p3_t18_17b[0]
    FieldNameAlt: Line 17b. Location (Street, City, State, ZIP code) and County.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.real_property_total_equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page3[0].p3_t20_17c[0]
    FieldNameAlt: Line 17c. Total Equity (Add lines 17a, 17b and amounts from any
        attachments).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_2.purchase_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page3[0].p3_t32_18b[0]
    FieldNameAlt: Line 18b. Purchase/Lease Date (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_2.market_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].p3_t33_18b[0]
    FieldNameAlt: Line 18b. Current Fair Market Value (F M V).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_2.current_loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].p3_t34_18b[0]
    FieldNameAlt: Line 18b. Current Loan Balance.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_2.monthly_payment|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].p3_t35_18b[0]
    FieldNameAlt: Line 18b. Amount of Monthly Payment.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_2.final_payment_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page3[0].p3_t36_18b[0]
    FieldNameAlt: Line 18b. Date of Final Payment (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicle_info_2.equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page3[0].p3_t37_18b[0]
    FieldNameAlt: Line 18b. Equity. F M V Minus Loan.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.vehicles_total_equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page3[0].p3_t40_18c[0]
    FieldNameAlt: Line 18c. Total Equity (Add lines 18a, 18b and amounts from any
        attachments).
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page5.personalasset_info_2.location_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].p3_t47_19a[0]
    FieldNameAlt: Line 19b. Location (Street, City, State, ZIP code) and County.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page5.personalasset_info_1.location_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page3[0].p3_t55_19b[0]
    FieldNameAlt: Line 19a. Location (Street, City, State, ZIP code) and County.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page5.personal_assets_total_equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page3[0].p3_t56_19c[0]
    FieldNameAlt: Line 19c. Total Equity (Add lines 19a, 19b and amounts from any
        attachments).
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page4[0]
    FieldType: ''
-   FieldFlags: 8388608
    value: {{ form.page6.other_1_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].Blank32[0]
    FieldNameAlt: 'Line 32. Other Income (Specify below). Footnote 5. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page6.other_2_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].Blank33[0]
    FieldNameAlt: Line 33. Other Income.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.wages|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t57_20[0]
    FieldNameAlt: 'Page 4. Section 5: Monthly Income and Expenses. Monthly Income
        / Expense Statement (For additional information, refer to Publication 1854.).
        Total income. Line 20. Source. Wages (Taxpayer) (Footnote 1). Gross Monthly.'
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.wages_spouse|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t59_21[0]
    FieldNameAlt: Line 21. Wages (Spouse) (Footnote 1).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.interest|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t61_22[0]
    FieldNameAlt: Line 22. Interest - Dividends.
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page6.net_business_income > 0 %}{{ form.page6.net_business_income|intcomma_force }}{% else %}0{% endif %}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t63_23[0]
    FieldNameAlt: Line 23. Net Business Income. (Footnote 2).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.net_rental_income|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t65_24[0]
    FieldNameAlt: Line 24. Net Rental Income. (Footnote 3).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.distributions|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t67_25[0]
    FieldNameAlt: Line 25. Distributions (K-1, IRA, etcetera). (Footnote 4).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.pension|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t69_26[0]
    FieldNameAlt: 'Line 26. Pension (Taxpayer). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.pension_spouse|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t71_27[0]
    FieldNameAlt: 'Line 27. Pension (Spouse). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.social_security|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t73_28[0]
    FieldNameAlt: 'Line 28. Social Security (Taxpayer). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.social_security_spouse|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t75_29[0]
    FieldNameAlt: 'Line 29. Social Security (Spouse). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.child_support|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t79_30[0]
    FieldNameAlt: 'Line 30. Child Support. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.alimony|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t81_31[0]
    FieldNameAlt: 'Line 31. Alimony. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.other_1|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t81_32[0]
    FieldNameAlt: Line 32. Other Income.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.other_2|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t81_33[0]
    FieldNameAlt: Line 33. Other Income.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.total_income|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalIncome[0].p3_t81_34[0]
    FieldNameAlt: 'Line 34. Total Income (add lines 20 through 33). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.food_clothing|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t58_35[0]
    FieldNameAlt: Section 5. Total Living Expenses. Line 35. Expense Items. (footnote
        6). Food, Clothing and Miscellaneous (Footnote 7). Actual Monthly.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.housing|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t60_36[0]
    FieldNameAlt: 'Line 36. Housing and Utilities (Footnote 8). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.vehicle_own|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t62_37[0]
    FieldNameAlt: 'Line 37. Vehicle Ownership Costs (Footnote 9). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.vehicle_oper|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t64_38[0]
    FieldNameAlt: 'Line 38. Vehicle Operating Costs (Footnote 10). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.pub_transport|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t66_39[0]
    FieldNameAlt: 'Line 39. Public Transportation (Footnote 11). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.health|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t68_40[0]
    FieldNameAlt: Line 40. Health Insurance.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.oop_healthcare|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t70_41[0]
    FieldNameAlt: 'Line 41. Out of Pocket Health Care Costs (Footnote 12). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.court|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t72_42[0]
    FieldNameAlt: 'Line 42. Court Ordered Payments. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.child_care|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t74_43[0]
    FieldNameAlt: 'Line 43. Child / Dependent Care. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.life_insurance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t76_44[0]
    FieldNameAlt: 'Line 44. Life Insurance. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.taxes|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t78_45[0]
    FieldNameAlt: Line 45. Current year taxes (Income / F I C A) (footnote 13).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.secured_debts|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t80_46[0]
    FieldNameAlt: 'Line 46. Secured Debts (Attach list). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.local_taxes|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t82_47[0]
    FieldNameAlt: Line 47. Delinquent State or Local Taxes.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.other_expenses|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t83_48[0]
    FieldNameAlt: 'Line 48. Other Expenses (Attach list). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.total_expenses|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t84_49[0]
    FieldNameAlt: 'Line 49. Total Living Expenses (add lines 35 through 48). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page6.net_difference|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page4[0].TotalLivingExpenses[0].p3_t85_50[0]
    FieldNameAlt: 'Line 50. Net difference (Line 34 minus 49). '
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page7 %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page5[0].#subform[0].p5_0_51[0]
    FieldNameAlt: Page 5. Section 6. Business Information. Line 51. Is the business
        a sole proprietorship (filing Schedule C). Yes, Continue with Sections 6 and
        7. All other business entities, including limited liability companies, partnerships
        or corporations, must complete Form 433-B.
    FieldType: Button
-   FieldFlags: 0
    value: value: {% if not form.page7 %}no{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page5[0].#subform[0].p5_0_51[1]
    FieldNameAlt: Line 51.  No, Complete Form 433-B.
    FieldType: Button
-   FieldFlags: 8388608
    value: {{ form.page7.business_name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page5[0].#subform[0].p5_t1_52[0]
    FieldNameAlt: Line 52. Business Name and Address (if different than 1b).
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page5[0].AB61[0]
    FieldType: ''
-   FieldFlags: 4096
    value: {{ form.page7.paymentprocessor_info_1.name_address }}
    FieldJustification: Left
    FieldMaxLength: 172
    FieldName: topmostSubform[0].Page5[0].AB61[0].a61[0].p5_t8_61a[0]
    FieldNameAlt: Line 61a. Payment Processor (for example, PayPal, Authorize.net,
        Google Checkout, etcetera) Name and Address (Street, City, State, ZIP code).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.paymentprocessor_info_1.account_number }}
    FieldJustification: Center
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page5[0].AB61[0].a61[0].p5_t9_61a[0]
    FieldNameAlt: Line 61a. Payment Processor Account Number.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.paymentprocessor_info_2.name_address }}
    FieldJustification: Left
    FieldMaxLength: 172
    FieldName: topmostSubform[0].Page5[0].AB61[0].b61[0].p5_t10_61b[0]
    FieldNameAlt: Line 61b. Name and Address (Street, City, State, ZIP code).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.paymentprocessor_info_2.account_number }}
    FieldJustification: Center
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page5[0].AB61[0].b61[0].p5_t11_61b[0]
    FieldNameAlt: Line 61b. Payment Processor Account Number.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page5[0].Table62[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page7.businesscc_info_1.credit_card }}
    FieldJustification: Center
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page5[0].Table62[0].#subform[1].p5_t12_62a[0]
    FieldNameAlt: Line 62a. Credit Cards Accepted by the Business. Credit Card.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businesscc_info_1.merchant_account_number }}
    FieldJustification: Center
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page5[0].Table62[0].#subform[1].p5_t13_62a[0]
    FieldNameAlt: Line 62a. Merchant Account Number.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.businesscc_info_1.bank_name_address }}
    FieldJustification: Left
    FieldMaxLength: 134
    FieldName: topmostSubform[0].Page5[0].Table62[0].#subform[1].p5_t14_62a[0]
    FieldNameAlt: Line 62a. Issuing Bank Name and Address (Street, City, State, ZIP
        code).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businesscc_info_2.credit_card }}
    FieldJustification: Center
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page5[0].Table62[0].#subform[2].p5_t15_62b[0]
    FieldNameAlt: Line 62b. Credit Card.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businesscc_info_2.merchant_account_number }}
    FieldJustification: Center
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page5[0].Table62[0].#subform[2].p5_t16_62b[0]
    FieldNameAlt: Line 62b. Merchant Account Number.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.businesscc_info_2.bank_name_address }}
    FieldJustification: Left
    FieldMaxLength: 134
    FieldName: topmostSubform[0].Page5[0].Table62[0].#subform[2].p5_t17_62b[0]
    FieldNameAlt: Line 62b. Issuing Bank Name and Address (Street, City, State, ZIP
        code).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businesscc_info_3.credit_card }}
    FieldJustification: Center
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page5[0].Table62[0].L62C[0].p5_t18_62c[0]
    FieldNameAlt: Line 62c. Credit Card.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businesscc_info_3.merchant_account_number }}
    FieldJustification: Center
    FieldMaxLength: 24
    FieldName: topmostSubform[0].Page5[0].Table62[0].L62C[0].p5_t19_62c[0]
    FieldNameAlt: Line 62c. Merchant Account Number.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.businesscc_info_3.bank_name_address }}
    FieldJustification: Left
    FieldMaxLength: 134
    FieldName: topmostSubform[0].Page5[0].Table62[0].L62C[0].p5_t20_62c[0]
    FieldNameAlt: Line 62c. Issuing Bank Name and Address (Street, City, State, ZIP
        code).
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page5[0].Table64[0]
    FieldType: ''
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page5[0].Table64[0].#subform[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page7.bank_balance_date|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page5[0].Table64[0].#subform[0].#subform[1].p5_t22_64[0]
    FieldNameAlt: Section 5. BUSINESS BANK ACCOUNTS. Include checking accounts, online
        and mobile (for example, PayPal) accounts, money market accounts, savings
        accounts, and stored value cards (for example, payroll cards, government benefit
        cards, etcetera). Report Personal Accounts in Section 4.  Account Balance
        as of (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.businessbankacc_info_1.account_type }}
    FieldJustification: Left
    FieldMaxLength: 25
    FieldName: topmostSubform[0].Page5[0].Table64[0].#subform[2].p5_t23_64a[0]
    FieldNameAlt: Line 64a. Type of Account.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.businessbankacc_info_1.name_address }}
    FieldJustification: Left
    FieldMaxLength: 104
    FieldName: topmostSubform[0].Page5[0].Table64[0].#subform[2].p5_t24_64a[0]
    FieldNameAlt: Line 64a. Full name and Address (Street, City, State, ZIP code)
        of Bank, Savings and Loan, Credit Union or Financial Institution.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessbankacc_info_1.account_number }}
    FieldJustification: Center
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page5[0].Table64[0].#subform[2].p5_t25_64a[0]
    FieldNameAlt: Line 64a. Account Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessbankacc_info_1.account_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page5[0].Table64[0].#subform[2].p5_t26_64a[0]
    FieldNameAlt: Line 64a. Account Balance.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.businessbankacc_info_2.account_type }}
    FieldJustification: Left
    FieldMaxLength: 25
    FieldName: topmostSubform[0].Page5[0].Table64[0].#subform[3].p5_t27_64b[0]
    FieldNameAlt: Line 64b. Type of Account.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.businessbankacc_info_2.name_address }}
    FieldJustification: Left
    FieldMaxLength: 104
    FieldName: topmostSubform[0].Page5[0].Table64[0].#subform[3].p5_t28_64b[0]
    FieldNameAlt: Line 64b. Full name and Address (Street, City, State, ZIP code)
        of Bank, Savings and Loan, Credit Union or Financial Institution.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessbankacc_info_2.name_address }}
    FieldJustification: Center
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page5[0].Table64[0].#subform[3].p5_t29_64b[0]
    FieldNameAlt: Line 64b. Account Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessbankacc_info_2.account_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page5[0].Table64[0].#subform[3].p5_t30_64b[0]
    FieldNameAlt: Line 64b. Account Balance.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page5[0].Table64[1]
    FieldType: ''
-   FieldFlags: 4096
    value: {{ form.page7.accountsreceivable_info_1.name_address }}
    FieldJustification: Left
    FieldMaxLength: 100
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65a[0].p5_t32_65a[0]
    FieldNameAlt: Section 6. ACCOUNTS / NOTES RECEIVABLE. Include e-payment accounts
        receivable and factoring companies, and any bartering or online auction accounts.
        (List all contracts separately, including contracts awarded, but not started.
        Include Federal, state and local government grants and contracts. Line 65a.
        Accounts / Notes Receivable and Address (Street, City, State, ZIP code).
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.accountsreceivable_info_1.status }}
    FieldJustification: Left
    FieldMaxLength: 26
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65a[0].p5_t33_65a[0]
    FieldNameAlt: Line 65a. Status (for example, age, factored, other).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_1.date_due|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65a[0].p5_t34_65a[0]
    FieldNameAlt: Line 65a. Date Due (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_1.contract_number }}
    FieldJustification: Center
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65a[0].p5_t35_65a[0]
    FieldNameAlt: Line 65a. Invoice Number or Government Grant or Contract Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_1.amount_due|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65a[0].p5_t36_65a[0]
    FieldNameAlt: Line 65a. Amount Due.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.accountsreceivable_info_2.name_address }}
    FieldJustification: Left
    FieldMaxLength: 100
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65b[0].p5_t37_65b[0]
    FieldNameAlt: Line 65b. Accounts / Notes Receivable and Address (Street, City,
        State, ZIP code).
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.accountsreceivable_info_2.status }}
    FieldJustification: Left
    FieldMaxLength: 26
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65b[0].p5_t38_65b[0]
    FieldNameAlt: Line 65b. Status.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_2.date_due|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65b[0].p5_t39_65b[0]
    FieldNameAlt: Line 65b. Date Due (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_2.contract_number }}
    FieldJustification: Center
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65b[0].p5_t40_65b[0]
    FieldNameAlt: Line 65b. Invoice Number or Government Grant or Contract Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_2.amount_due|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65b[0].p5_t41_65b[0]
    FieldNameAlt: Line 65b. Amount Due.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.accountsreceivable_info_3.name_address }}
    FieldJustification: Left
    FieldMaxLength: 100
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65c[0].p5_t42_65c[0]
    FieldNameAlt: Line 65c. Accounts / Notes Receivable and Address (Street, City,
        State, ZIP code).
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.accountsreceivable_info_3.status }}
    FieldJustification: Left
    FieldMaxLength: 26
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65c[0].p5_t43_65c[0]
    FieldNameAlt: Line 65c. Status.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_3.date_due|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65c[0].p5_t44_65c[0]
    FieldNameAlt: Line 65c. Date Due (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_3.contract_number }}
    FieldJustification: Center
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65c[0].p5_t45_65c[0]
    FieldNameAlt: Line 65c. Invoice Number or Government Grant or Contract Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_3.amount_due|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65c[0].p5_t46_65c[0]
    FieldNameAlt: Line 65c. Amount Due.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.accountsreceivable_info_4.name_address }}
    FieldJustification: Left
    FieldMaxLength: 100
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65d[0].p5_t47_65d[0]
    FieldNameAlt: Line 65d. Accounts / Notes Receivable and Address (Street, City,
        State, ZIP code).
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.accountsreceivable_info_4.status }}
    FieldJustification: Left
    FieldMaxLength: 26
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65d[0].p5_t48_65d[0]
    FieldNameAlt: Line 65d. Status.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_4.date_due|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65d[0].p5_t49_65d[0]
    FieldNameAlt: Line 65d. Date Due (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_4.contract_number }}
    FieldJustification: Center
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65d[0].p5_t50_65d[0]
    FieldNameAlt: Line 65d. Invoice Number or Government Grant or Contract Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_4.amount_due|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65d[0].p5_t51_65d[0]
    FieldNameAlt: Line 65d. Amount Due.
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.accountsreceivable_info_5.name_address }}
    FieldJustification: Left
    FieldMaxLength: 100
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65d[1].#field[0]
    FieldNameAlt: Line 65e. Accounts / Notes Receivable and Address (Street, City,
        State, ZIP code).
    FieldType: Text
-   FieldFlags: 4096
    value: {{ form.page7.accountsreceivable_info_5.status }}
    FieldJustification: Left
    FieldMaxLength: 26
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65d[1].#field[1]
    FieldNameAlt: Line 65e. Status.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_5.date_due|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65d[1].#field[2]
    FieldNameAlt: Line 65e. Date Due (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_5.contract_number }}
    FieldJustification: Center
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65d[1].#field[3]
    FieldNameAlt: Line 65e. Invoice Number or Government Grant or Contract Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.accountsreceivable_info_5.amount_due|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page5[0].Table64[1].Line65d[1].#field[4]
    FieldNameAlt: Line 65e. Amount Due.
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page7.fed_contractor %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page5[0].p5_0_55[0]
    FieldNameAlt: Line 55. Is the business a Federal Contractor? Yes.
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page7.fed_contractor %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page5[0].p5_0_55[1]
    FieldNameAlt: Line 55. No.
    FieldType: Button
-   FieldFlags: 0
    value: {% if form.page7.paymentprocessors %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page5[0].p5_0_60[0]
    FieldNameAlt: Line 60. Does the business engage in e-Commerce (Internet sales).
        If yes, complete lines 61a and 61b. Yes.
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page7.paymentprocessors %}Not{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page5[0].p5_0_60[1]
    FieldNameAlt: Line 60.  No.
    FieldType: Button
-   FieldFlags: 0
    value: {{ form.page7.total_cash_on_hand|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page5[0].p5_t21_63[0]
    FieldNameAlt: Line 63. Business Cash on Hand. Include cash that is not in a bank.
        Total Cash on Hand.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.ein }}
    FieldJustification: Left
    FieldMaxLength: 10
    FieldName: topmostSubform[0].Page5[0].p5_t2_53[0]
    FieldNameAlt: Line 53. Employer Identification Number.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.total_cash_in_banks|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page5[0].p5_t31_64c[0]
    FieldNameAlt: Line 64c. Total Cash in Banks (Add lines 64a, 64b and amounts from
        any attachments).
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page7.business_type }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page5[0].p5_t3_54[0]
    FieldNameAlt: Line 54. Type of Business.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page7.business_web }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page5[0].p5_t4_56[0]
    FieldNameAlt: Line 56. Business Website (web address).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.outstanding_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page5[0].p5_t52_65e[0]
    FieldNameAlt: Line 65f. Total Outstanding Balance (Add lines 65a through 65e and
        amounts from any attachments).
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page7.num_employees }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page5[0].p5_t5_57[0]
    FieldNameAlt: Line 57. Total Number of Employees.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page7.average_gross_monthly_payroll|intcomma_force }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page5[0].p5_t6_58a[0]
    FieldNameAlt: Line 58. Average Gross Monthly Payroll.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page7.tax_deposit_freq }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page5[0].p5_t7_59b[0]
    FieldNameAlt: Line 59. Frequency of Tax Deposits.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_2.lender_phone }}
    FieldJustification: Left
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page6[0].Lender-Phone2[0].p2_t18_13c[0]
    FieldNameAlt: Line 66b. Phone.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page7.businessasset_info_2.lender_name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page6[0].Lender-Phone2[0].p6_t18_66b[0]
    FieldNameAlt: Line 66b. Lender / Lessor / Landlord Name, Address (Street, City,
        State, ZIP code) and Phone.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_1.lender_phone }}
    FieldJustification: Left
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page6[0].Lender-Phone[0].p2_t18_13c[0]
    FieldNameAlt: Line 66a. Phone.
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page7.businessasset_info_1.lender_name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page6[0].Lender-Phone[0].p6_t9_66a[0]
    FieldNameAlt: Line 66a. Lender / Lessor / Landlord Name, Address (Street, City,
        State, ZIP code) and Phone.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page6[0].Line59b[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_2.description }}
    FieldJustification: Left
    FieldMaxLength: 45
    FieldName: topmostSubform[0].Page6[0].Line59b[0].Line66b[0].p6_t10_66b[0]
    FieldNameAlt: Line 66b. Property Description.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_2.purchase_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page6[0].Line59b[0].Line66b[0].p6_t11_66b[0]
    FieldNameAlt: Line 66b. Purchase / Lease Date (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_2.market_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page6[0].Line59b[0].Line66b[0].p6_t12_66b[0]
    FieldNameAlt: Line 66b. Current Fair Market Value (F M V).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_2.current_loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page6[0].Line59b[0].Line66b[0].p6_t13_66b[0]
    FieldNameAlt: Line 66b. Current Loan Balance.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_2.monthly_payment|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page6[0].Line59b[0].Line66b[0].p6_t14_66b[0]
    FieldNameAlt: Line 66b. Amount of Monthly Payment.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_2.final_payment_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page6[0].Line59b[0].Line66b[0].p6_t15_66b[0]
    FieldNameAlt: Line 66b. Date of Final Payment (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_2.equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page6[0].Line59b[0].Line66b[0].p6_t16_66b[0]
    FieldNameAlt: Line 66b. Equity. F M V Minus Loan.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].Page6[0].Table_Line66a[0]
    FieldType: ''
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_1.description }}
    FieldJustification: Left
    FieldMaxLength: 34
    FieldName: topmostSubform[0].Page6[0].Table_Line66a[0].Line66a[0].p6_t1_66a[0]
    FieldNameAlt: Page 6. Section 6. Business Information. Business Assets. Include
        all tools, books, machinery, equipment, inventory or other assets used in
        trade or business. Include a list and show the value of all intangible assets
        such as licenses, patents, domain names, copyrights, trademarks, mining claims,
        etcetera. Line 66a. Property Description.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_1.purchase_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page6[0].Table_Line66a[0].Line66a[0].p6_t2_66a[0]
    FieldNameAlt: Line 66a. Purchase / Lease Date (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_1.market_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page6[0].Table_Line66a[0].Line66a[0].p6_t3_66a[0]
    FieldNameAlt: Line 66a. Current Fair Market Value (F M V).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_1.current_loan_balance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page6[0].Table_Line66a[0].Line66a[0].p6_t4_66a[0]
    FieldNameAlt: Line 66a. Current Loan Balance.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_1.monthly_payment|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page6[0].Table_Line66a[0].Line66a[0].p6_t5_66a[0]
    FieldNameAlt: Line 66a. Amount of Monthly Payment.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_1.final_payment_date|date:"mdY" }}
    FieldJustification: Center
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page6[0].Table_Line66a[0].Line66a[0].p6_t6_66a[0]
    FieldNameAlt: Line 66a. Date of Final Payment (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.businessasset_info_1.equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 12
    FieldName: topmostSubform[0].Page6[0].Table_Line66a[0].Line66a[0].p6_t7_66a[0]
    FieldNameAlt: Line 66a. Equity. F M V Minus Loan.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.materials }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t23_S6t[0]
    FieldNameAlt: Section 7. Total Monthly Business Expenses (use attachments as needed).
        Line 77. Expense Items. Materials Purchased (Footnote 1). Actual Monthly.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.inventory|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t25_S6t[0]
    FieldNameAlt: Line 78. Inventory Purchased (Footnote 2).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.gross_wages_and_salaries|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t27_S6t[0]
    FieldNameAlt: Line 79. Gross Wages and Salaries.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.rent|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t29_S6t[0]
    FieldNameAlt: 'Line 80. Rent. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.supplies|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t31_S6t[0]
    FieldNameAlt: Line 81. Supplies (Footnote 3).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.utilities_telephone|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t32_S6t[0]
    FieldNameAlt: 'Line 82. Utilities / Telephone (Footnote 4). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.vehicle_suppl|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t34_S6t[0]
    FieldNameAlt: Line 83.  Vehicle Gasoline / Oil.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.maintenance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t36_S6t[0]
    FieldNameAlt: Line 84. Repairs and Maintenance.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.insurance|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t38_S6t[0]
    FieldNameAlt: 'Line 85. Insurance. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.taxes|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t40_S6t[0]
    FieldNameAlt: 'Line 86. Current Taxes (Footnote 5). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.other_expenses|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t42_S6t[0]
    FieldNameAlt: 'Line 87. Other Expenses, including installment payments (Specify). '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.total_expenses|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 18
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t44_S6t[0]
    FieldNameAlt: Line 88. Total Expenses (Add lines 77 through 87).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.net_business_income|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 18
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyExpenses[0].p6_t45_S6t[0]
    FieldNameAlt: 'Line 89. Net Business Income (Line 76 minus 88) (Footnote 6). '
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page8.other_1_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].Blank72[0]
    FieldNameAlt: Line 72. Other Income (Specify below).
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page8.other_2_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].Blank73[0]
    FieldNameAlt: Line 73. Other Income.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page8.other_3_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].Blank74[0]
    FieldNameAlt: Line 74. Other Income.
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page8.other_4_name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].Blank75[0]
    FieldNameAlt: Line 75. Other Income.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.gross_receipts|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].p6_t22_S6t[0]
    FieldNameAlt: Section 7. Total Monthly Business Income. Line 67. Source. Gross
        Receipts. Gross Monthly.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.gross_rental_income|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].p6_t24_S6t[0]
    FieldNameAlt: 'Line 68. Gross Rental Income. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.interest|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].p6_t26_S6t[0]
    FieldNameAlt: 'Line 69. Interest. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.dividends|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].p6_t28_S6t[0]
    FieldNameAlt: 'Line 70. Dividends. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.cash_receipts_other|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].p6_t30_S6t[0]
    FieldNameAlt: Line 71. Cash Receipts not included in line 67 through 70.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.other_1_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].p6_t33_S6t[0]
    FieldNameAlt: Line 72. Gross Monthly Income.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.other_2_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].p6_t35_S6t[0]
    FieldNameAlt: Line 73. Gross Monthly Income.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.other_3_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].p6_t37_S6t[0]
    FieldNameAlt: Line 74. Gross Monthly Income.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.other_4_value|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].p6_t39_S6t[0]
    FieldNameAlt: Line 75. Gross Monthly Income.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.total_income|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 16
    FieldName: topmostSubform[0].Page6[0].TotalMonthlyIncome[0].p6_t43_S6t[0]
    FieldNameAlt: 'Line 76. Total Income (Add lines 67 through 75). '
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page8.accounting_method %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].Page6[0].p6_0_7[0]
    FieldNameAlt: 'Section 7: Sole Proprietorship Information (lines 67 through 87
        should reconcile with business Profit and Loss Statement). Accounting Method
        Used: Cash.'
    FieldType: Button
-   FieldFlags: 0
    value: {% if not form.page8.accounting_method %}No{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: NoFieldStateOption: Off'
    FieldName: topmostSubform[0].Page6[0].p6_0_7[1]
    FieldNameAlt: 'Section 7. Accounting Method Used: Accrual.'
    FieldType: Button
-   FieldFlags: 8392704
    value: {{ form.page7.businessasset_info_2.location_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page6[0].p6_t17_66b[0]
    FieldNameAlt: Line 66b. Location (Street, City, State, ZIP code) and Country.
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page7.total_equity|intcomma_force }}
    FieldJustification: Right
    FieldMaxLength: 14
    FieldName: topmostSubform[0].Page6[0].p6_t19_66c[0]
    FieldNameAlt: Line 66c. Total Equity (Add lines 66a, 66b and amounts from any
        attachments).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.period_start|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page6[0].p6_t20_S6[0]
    FieldNameAlt: Section 7. Income and Expenses during the period (enter date m m
        d d y y y y) to (m m d d y y y y).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page8.period_end|date:"mdY" }}
    FieldJustification: Left
    FieldMaxLength: 8
    FieldName: topmostSubform[0].Page6[0].p6_t21_S6[0]
    FieldNameAlt: Section 7. Income and Expenses during the period (m m d d y y y
        y) to (enter date  m m d d y y y y).
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page7.businessasset_info_1.location_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].Page6[0].p6_t8_66a[0]
    FieldNameAlt: Line 66a. Location (Street, City, State, ZIP code) and Country.
    FieldType: Text
