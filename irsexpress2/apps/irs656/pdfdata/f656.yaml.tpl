{% load func_helpers %}
{% load misc_helpers %}

-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0]
    FieldType: ''
-   FieldFlags: 65536
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Button1[0]
    FieldNameAlt: Click to go to the I R S web page.
    FieldType: Button
-   FieldFlags: 0
    value: {{ form.page1.ein|substr:0 }}
    FieldJustification: Center
    FieldMaxLength: 2
    FieldName: topmostSubform[0].F656_Page1[0].Section1A[0].EIN_1[0]
    FieldNameAlt: Employer Identification Number (E I N); First 2 digits
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.ein|substr:2 }}
    FieldJustification: Center
    FieldMaxLength: 7
    FieldName: topmostSubform[0].F656_Page1[0].Section1A[0].EIN_2[0]
    FieldNameAlt: (E I N) Last 7 digits
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.jointoffer.ssn|ssnpart:1 }}
    FieldJustification: Center
    FieldMaxLength: 3
    FieldName: topmostSubform[0].F656_Page1[0].Section1A[0].SpouseSSN[0].Spouse_SSN_1[0]
    FieldNameAlt: Spouse's Social Security Number (S S N)  (First 3 digits).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.jointoffer.ssn|ssnpart:2 }}
    FieldJustification: Center
    FieldMaxLength: 2
    FieldName: topmostSubform[0].F656_Page1[0].Section1A[0].SpouseSSN[0].Spouse_SSN_2[0]
    FieldNameAlt: Spouse's Social Security Number (S S N)  (Middle two digits).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.jointoffer.ssn|ssnpart:3}}
    FieldJustification: Center
    FieldMaxLength: 4
    FieldName: topmostSubform[0].F656_Page1[0].Section1A[0].SpouseSSN[0].Spouse_SSN_3[0]
    FieldNameAlt: Spouse's Social Security Number (S S N)  (Last four digits).
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.jointoffer.title }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section1A[0].Spouse_First_Middle_Last_Name[0]
    FieldNameAlt: If a Joint Offer, Spouse's First Name, Middle Initial, Last Name
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.ssn|ssnpart:1}}
    FieldJustification: Center
    FieldMaxLength: 3
    FieldName: topmostSubform[0].F656_Page1[0].Section1A[0].YourSSN[0].Your_SSN_1[0]
    FieldNameAlt: Social Security Number (S S N)  (First 3 digits).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.ssn|ssnpart:2}}
    FieldJustification: Center
    FieldMaxLength: 2
    FieldName: topmostSubform[0].F656_Page1[0].Section1A[0].YourSSN[0].Your_SSN_2[0]
    FieldNameAlt: Social Security Number (S S N)  (Middle two digits).
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.ssn|ssnpart:3}}
    FieldJustification: Center
    FieldMaxLength: 4
    FieldName: topmostSubform[0].F656_Page1[0].Section1A[0].YourSSN[0].Your_SSN_3[0]
    FieldNameAlt: Social Security Number (S S N)  (Last four digits).
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.title }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section1A[0].Your_First_Middle_Last_Name[0]
    FieldNameAlt: 'Section 1. Your Information. Section 1A. Individual Information
        (Form 1040 Filers). Your First Name, Middle Initial, Last Name '
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section1A[0].Your_Home_Address[0]
    FieldNameAlt: Your Physical Home Address (Street, City, State, ZIP Code)
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.get_mailing_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section1A[0].Your_Mailing_Address[0]
    FieldNameAlt: Mailing Address (if different from above or Post Office Box number)
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.businessinfo.ein|substr:0 }}
    FieldJustification: Center
    FieldMaxLength: 2
    FieldName: topmostSubform[0].F656_Page1[0].Section1B[0].BusinessEIN[0].Business_EIN_1[0]
    FieldNameAlt: Employer Identification Number (E I N); First 2 digits
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.businessinfo.ein|substr:2 }}
    FieldJustification: Center
    FieldMaxLength: 7
    FieldName: topmostSubform[0].F656_Page1[0].Section1B[0].BusinessEIN[0].Business_EIN_2[0]
    FieldNameAlt: (E I N) Last 7 digits
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.businessinfo.address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section1B[0].Business_Address[0]
    FieldNameAlt: Business Address (Street, City, State, ZIP Code)
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page1.businessinfo.name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section1B[0].Business_Name[0]
    FieldNameAlt: Section 1. Your Information. Section 1B. Business Information (Form
        1120, 1065, etcetera, filers). Business Name.
    FieldType: Text
-   FieldFlags: 8392704 
    value: {{ form.page1.businessinfo.primary_contact }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section1B[0].Name_Title_Primary_Contact[0]
    FieldNameAlt: 'Name and title of primary contact. '
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.businessinfo.phone|getphonecode }}
    FieldJustification: Center
    FieldMaxLength: 3
    FieldName: topmostSubform[0].F656_Page1[0].Section1B[0].Phone[0].Area_Code[0]
    FieldNameAlt: Phone (Area Code)
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.businessinfo.phone|getphonemiddle }}
    FieldJustification: Center
    FieldMaxLength: 3
    FieldName: topmostSubform[0].F656_Page1[0].Section1B[0].Phone[0].Phone1[0]
    FieldNameAlt: Phone (Prefix)
    FieldType: Text
-   FieldFlags: 0
    value: {{ form.page1.businessinfo.phone|getphonelast }}
    FieldJustification: Center
    FieldMaxLength: 4
    FieldName: topmostSubform[0].F656_Page1[0].Section1B[0].Phone[0].Phone2[0]
    FieldNameAlt: Phone (Last four digits)
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page2.attachment_date|date:"d-m-Y" }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0].Attachment_Date[0]
    FieldNameAlt: 'Note:  If you need more space, use attachment and title it "Attachment
        to Form 656 dated [enter date]." Make sure to sign and date the  attachment. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.is_other_taxes %}{{ form.page2.othertaxes_types_periods|getline:"0:50" }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0].Other_Federal_Taxes_1[0]
    FieldNameAlt: 'Other Federal Tax(es) [specify type(s) and period(s)]. Line 1 of
        2. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.is_other_taxes %}{{ form.page2.othertaxes_types_periods|getline:"50:1000" }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0].Other_Federal_Taxes_2[0]
    FieldNameAlt: 'Other Federal Tax(es) [specify type(s) and period(s)]. Line 2 of
        2. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.is_trustfund_recovery_penalty %}{{ form.page2.trustfund_person }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0].Trust_Fund_Recovery_Penalty_Corp_Name[0]
    FieldNameAlt: 'Trust Fund Recovery Penalty as a responsible person of (enter corporation
        name) '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.is_trustfund_recovery_penalty %}{{ form.page2.trustfund_periods }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0].Trust_Fund_Recovery_Penalty_Period_Ending_1[0]
    FieldNameAlt: 'for failure to pay withholding and Federal Insurance Contributions
        Act taxes (Social Security taxes), for period(s) ending. Line 1 of 2. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.is_1040_incometax %}{{ form.page2.years_1040 }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0]._1040_Income_Tax_Years[0]
    FieldNameAlt: '1040 Income Tax-Year(s) (specify). '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.is_940_afuta %}{{ form.page2.years_940|getline:"0:35" }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0]._940_Years_1[0]
    FieldNameAlt: '940 Employer''s Annual Federal Unemployment (F U T A) Tax Return
        - Year(s). Line 1 of 2. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.is_940_afuta %}{{ form.page2.years_940|getline:"35:1000" }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0]._940_Years_2[0]
    FieldNameAlt: '940 Employer''s Annual Federal Unemployment (F U T A) Tax Return
        - Year(s). Line 2 of 2. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.is_941_qtaxreturn %}{{ form.page2.qtaxreturn_941_periods|getline:"0:40" }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0]._941_Quarterly_Periods_1[0]
    FieldNameAlt: '941 Employer''s Quarterly Federal Tax Return - Quarterly period(s).  Line
        1 of 2. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.is_941_qtaxreturn %}{{ form.page2.qtaxreturn_941_periods|getline:"40:1000" }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0]._941_Quarterly_Periods_2[0]
    FieldNameAlt: '941 Employer''s Quarterly Federal Tax Return - Quarterly period(s).
        Line 2 of 2. '
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page2.is_1040_incometax %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0].cB_03[0]
    FieldNameAlt: 'Section 2; Tax Periods. Section 2A. If Your Offer is for Individual
        Tax Debt Only. Complete this Section only if you completed Section 1A. 1040
        Income Tax-Year(s) '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {% if form.page2.is_941_qtaxreturn %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0].cB_05[0]
    FieldNameAlt: '941 Employer''s Quarterly Federal Tax Return '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {% if form.page2.is_940_afuta %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0].cB_06[0]
    FieldNameAlt: 940 Employer's Annual Federal Unemployment (F U T A) Tax Return
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {% if form.page2.is_trustfund_recovery_penalty %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0].cB_07[0]
    FieldNameAlt: 'Trust Fund Recovery Penalty as a responsible person '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {% if form.page2.is_other_taxes %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page1[0].Section2A[0].cB_08[0]
    FieldNameAlt: 'Other Federal Tax(es) '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    FieldJustification: 'LeftFieldStateOption: 1FieldStateOption: Off'
    FieldName: topmostSubform[0].F656_Page1[0].cB1_01[0]
    FieldNameAlt: Page 1. Did you use the Pre-Qualifier tool located on our website
        at w w w . i r s . gov prior to filling out this form? Yes
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    FieldJustification: 'LeftFieldStateOption: 1FieldStateOption: Off'
    FieldName: topmostSubform[0].F656_Page1[0].cB1_02[0]
    FieldNameAlt: Did you use the Pre-Qualifier tool located on our website at w w
        w . i r s . gov prior to filling out this form? No
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page2[0]
    FieldType: ''
-   FieldFlags: 8388608
    value: {% if form.page2.businesstaxdebt %}{{ form.page2.attachment_date|date:"d-m-Y" }}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page2[0].Section2B[0].Attachment_Date[0]
    FieldNameAlt: 'Note:  If you need more space, use attachment and title it "Attachment
        to Form 656 dated [enter date]." Make sure to sign and date the  attachment. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.businesstaxdebt and form.page2.businesstaxdebt.is_other_taxes_bus %}{{ form.page2.businesstaxdebt.othertaxes_types_periods_bus|getline:"0:50" }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page2[0].Section2B[0].Other_Federal_Taxes_1[0]
    FieldNameAlt: 'Other Federal Tax(es) [specify type(s) and period(s)]. Line 1 of
        2. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.businesstaxdebt and form.page2.businesstaxdebt.is_other_taxes_bus %}{{ form.page2.businesstaxdebt.othertaxes_types_periods_bus|getline:"50:1000" }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page2[0].Section2B[0].Other_Federal_Taxes_2[0]
    FieldNameAlt: 'Other Federal Tax(es) [specify type(s) and period(s)]. Line 2 of
        2. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.businesstaxdebt and form.page2.businesstaxdebt.is_1120_incometax %}{{ form.page2.businesstaxdebt.years_1120 }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page2[0].Section2B[0]._1120_Income_Tax_Years[0]
    FieldNameAlt: '1120 Income Tax-Year(s)  (specify). '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.businesstaxdebt and form.page2.businesstaxdebt.is_940_afuta_bus %}{{ form.page2.businesstaxdebt.years_940_bus|getline:"0:35" }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page2[0].Section2B[0]._940_Years_1[0]
    FieldNameAlt: '940 Employer''s Annual Federal Unemployment (F U T A) Tax Return
        - Year(s). Line 1 of 2. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.businesstaxdebt and form.page2.businesstaxdebt.is_940_afuta_bus %}{{ form.page2.businesstaxdebt.years_940_bus|getline:"35:1000" }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page2[0].Section2B[0]._940_Years_2[0]
    FieldNameAlt: '940 Employer''s Annual Federal Unemployment (F U T A) Tax Return
        - Year(s). Line 2 of 2. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.businesstaxdebt and form.page2.businesstaxdebt.is_941_qtaxreturn_bus %}{{ form.page2.businesstaxdebt.qtaxreturn_941_periods_bus|getline:"0:40" }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page2[0].Section2B[0]._941_Quarterly_Periods_1[0]
    FieldNameAlt: '941 Employer''s Quarterly Federal Tax Return - Quarterly period(s).  Line
        1 of 2. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page2.businesstaxdebt and form.page2.businesstaxdebt.is_941_qtaxreturn_bus %}{{ form.page2.businesstaxdebt.qtaxreturn_941_periods_bus|getline:"40:1000" }}{% else %}--empty--{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page2[0].Section2B[0]._941_Quarterly_Periods_2[0]
    FieldNameAlt: '941 Employer''s Quarterly Federal Tax Return - Quarterly period(s).
        Line 2 of 2. '
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page2.businesstaxdebt and form.page2.businesstaxdebt.is_1120_incometax %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page2[0].Section2B[0].cB2_01[0]
    FieldNameAlt: 'Page 2. Section 2 (continued). Tax Periods. Section 2B. If your
        Offer is for Business Tax Debt. Complete this Section only if you completed
        Section 1B. 1120 Income Tax Year(s). '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {% if form.page2.businesstaxdebt and form.page2.businesstaxdebt.is_941_qtaxreturn_bus %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page2[0].Section2B[0].cB2_02[0]
    FieldNameAlt: '941 Employer''s Quarterly Federal Tax Return '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {% if form.page2.businesstaxdebt and form.page2.businesstaxdebt.is_940_afuta_bus %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page2[0].Section2B[0].cB2_03[0]
    FieldNameAlt: 940 Employer's Annual Federal Unemployment (F U T A) Tax Return
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {% if form.page2.businesstaxdebt and form.page2.businesstaxdebt.is_other_taxes_bus %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page2[0].Section2B[0].cB2_04[0]
    FieldNameAlt: 'Other Federal Tax(es) '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 8392704
    value: {{ form.page3.circumstances }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page2[0].Section3[0].Explanation_Of_Circumstances[0]
    FieldNameAlt: 'Explanation of Circumstances (Add additional pages, if needed);
        The IRS understands that there are unplanned events or special circumstances,
        such as serious illness, where paying the full amount or the minimum  offer
        amount might impair your ability to provide for yourself and your family.  If
        this is the case and you can provide documentation to prove your  situation,
        then your offer may be accepted despite your financial profile. Describe your
        situation below and attach appropriate documents to this offer  application. '
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page3.doubt_collectibility %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page2[0].Section3[0].cB2_05[0]
    FieldNameAlt: 'Section 3. Reason for Offer; Doubt as to Collectibility - I have
        insufficient assets and income to pay the full amount.  '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {% if form.page3.exceptional_circumstances %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page2[0].Section3[0].cB2_06[0]
    FieldNameAlt: 'Exceptional Circumstances (Effective Tax Administration) - I owe
        this amount and have sufficient assets to pay the full amount, but due to
        my exceptional circumstances, requiring full payment would cause an economic
        hardship or would be unfair and inequitable.  I am submitting a written narrative
        explaining my circumstances. '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {% if form.page4.low_income_qualify %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page2[0].Section4[0].cB2_07[0]
    FieldNameAlt: 'Section 4. Low Income Certification (Individuals and Sole Proprietors
        Only); Do you qualify for Low-Income Certification?  You qualify if your gross
        monthly household income is less than or equal to the amount shown in the  chart
        below based on your family size and where you live. If you qualify, you are
        not required to submit any payments during the consideration of your offer.
        Businesses other than sole proprietorships do not qualify for the low income
        waiver.  Check here if you qualify for Low Income Certification based on the
        monthly income guidelines below. '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0]
    FieldType: ''
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].AmountOfPayments[0]
    FieldType: ''
-   FieldFlags: 0
    value: {% if form.page5.lump_sum_cash %}{{ form.page5.payment_1|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Right
    FieldMaxLength: 20
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].AmountOfPayments[0].Row1[0].Amount_Payment_1[0]
    FieldNameAlt: You may pay the remaining balance in one payment after acceptance
        of the offer or up to five payments, but cannot exceed 5 months. Amount of
        payment.
    FieldType: Text
-   FieldFlags: 1
    value: 1
    FieldJustification: Center
    FieldMaxLength: 12
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].AmountOfPayments[0].Row1[0].Payable_Within_1[0]
    FieldNameAlt: payable within 1 (Month after acceptance)
    FieldType: Text
    FieldValueDefault: '1'
-   FieldFlags: 0
    value: {% if form.page5.lump_sum_cash %}{{ form.page5.payment_2|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Right
    FieldMaxLength: 20
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].AmountOfPayments[0].Row2[0].Amount_Payment_2[0]
    FieldNameAlt: Amount of payment.
    FieldType: Text
-   FieldFlags: 1
    value: 2
    FieldJustification: Center
    FieldMaxLength: 12
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].AmountOfPayments[0].Row2[0].Payable_Within_2[0]
    FieldNameAlt: payable within 2 (Months after acceptance)
    FieldType: Text
    FieldValueDefault: '2'
-   FieldFlags: 0
    value: {% if form.page5.lump_sum_cash %}{{ form.page5.payment_3|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Right
    FieldMaxLength: 20
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].AmountOfPayments[0].Row3[0].Amount_Payment_3[0]
    FieldNameAlt: Amount of payment.
    FieldType: Text
-   FieldFlags: 1
    value: 3
    FieldJustification: Center
    FieldMaxLength: 12
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].AmountOfPayments[0].Row3[0].Payable_Within_3[0]
    FieldNameAlt: payable within 3 (Months after acceptance)
    FieldType: Text
    FieldValueDefault: '3'
-   FieldFlags: 0
    value: {% if form.page5.lump_sum_cash %}{{ form.page5.payment_4|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Right
    FieldMaxLength: 20
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].AmountOfPayments[0].Row4[0].Amount_Payment_4[0]
    FieldNameAlt: Amount of payment.
    FieldType: Text
-   FieldFlags: 1
    value: 4
    FieldJustification: Center
    FieldMaxLength: 12
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].AmountOfPayments[0].Row4[0].Payable_Within_4[0]
    FieldNameAlt: payable within 4 (Months after acceptance)
    FieldType: Text
    FieldValueDefault: '4'
-   FieldFlags: 0
    value: {% if form.page5.lump_sum_cash %}{{ form.page5.payment_5|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Right
    FieldMaxLength: 20
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].AmountOfPayments[0].Row5[0].Amount_Payment_5[0]
    FieldNameAlt: Amount of payment.
    FieldType: Text
-   FieldFlags: 1
    value: 5
    FieldJustification: Center
    FieldMaxLength: 12
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].AmountOfPayments[0].Row5[0].Payable_Within_5[0]
    FieldNameAlt: payable within 5 (Months after acceptance)
    FieldType: Text
    FieldValueDefault: '5'
-   FieldFlags: 8388609
    value: --empty--
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].IRSUseOnly[0].Addendum_Dated[0]
    FieldNameAlt: IRS Use Only. Attached is an addendum dated [Insert date] setting
        forth the amended offer amount and payment terms.
    FieldType: Text
-   FieldFlags: 1
    FieldJustification: 'LeftFieldStateOption: 1FieldStateOption: Off'
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].IRSUseOnly[0].cB3_03[0]
    FieldNameAlt: IRS Use Only. Attached is an addendum dated [date] setting forth
        the amended offer amount and payment terms.
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 8388608
    value: {% if form.page5.periodic_payment %}{{ form.page5.offer_included|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].Installment_Payment_1[0]
    FieldNameAlt: 'Note: The total amount must equal all of the proposed payments
        including the first and last payments. Enclose a check for the first month''s
        installment. $[Enter dollar amount] is included with this offer then $[dollar
        amount] will be sent in on the [day] of each month thereafter for a total
        of [number of months] months with a final payment of $[dollar amount] to be
        paid on the  [day] of the [number of months] month. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page5.periodic_payment %}{{ form.page5.monthly_payment|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].Installment_Payment_2[0]
    FieldNameAlt: $[dollar amount] is included with this offer then $[Enter dollar
        amount] will be sent in on the [day] of each month thereafter for a total
        of [number of months] months with a final payment of $[dollar amount] to be
        paid on the  [day] of the [number of months] month.
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page5.periodic_payment %}{{ form.page5.final_payment|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].Installment_Payment_2[1]
    FieldNameAlt: $[dollar amount] is included with this offer then $[dollar amount]
        will be sent in on the [day] of each month thereafter for a total of [number
        of months] months with a final payment of $[Enter dollar amount] to be paid
        on the  [day] of the [number of months] month.
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page5.periodic_payment %}{{ form.page5.final_pay_month }}{% else %}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].Installment_Payment_2[2]
    FieldNameAlt: '$[dollar amount] is included with this offer then $[dollar amount]
        will be sent in on the [day] of each month thereafter for a total of [number
        of months] months with a final payment of $[dollar amount] to be paid on the  [day]
        of the [Enter number of months] month. Note: The total months may not exceed
        a total of 24 months, including the initial payment. Your initial payment
        is considered to be month 1; therefore, the remainder of the payments must
        be made within 23 months for a total of 24.You must continue to make these
        monthly payments while the IRS is considering the offer (waived if you are
        an individual or sole proprietorship and met the requirements for Low Income
        Certification). Failure to make regular monthly payments will cause your offer
        to be returned with no appeal rights. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page5.periodic_payment %}{{ form.page5.payment_day }}{% else %}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].Installment_Payment_Day[0]
    FieldNameAlt: $[dollar amount] is included with this offer then $[dollar amount]
        will be sent in on the [Enter day] of each month thereafter for a total of
        [number of months] months with a final payment of $[dollar amount] to be paid
        on the  [day] of the [number of months] month.
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page5.periodic_payment %}{{ form.page5.final_payment_day }}{% else %}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].Installment_Payment_Day[1]
    FieldNameAlt: $[dollar amount] is included with this offer then $[dollar amount]
        will be sent in on the [day] of each month thereafter for a total of [number
        of months] months with a final payment of $[dollar amount] to be paid on the  [Enter
        day] of the [number of months] month.
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page5.periodic_payment %}{{ form.page5.offer_amount_period|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].Periodic_Payment_Amount_Of_Offer[0]
    FieldNameAlt: Periodic Payment. Enter the amount of your offer.
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].Table1[0]
    FieldType: ''
-   FieldFlags: 0
    value: {% if form.page5.lump_sum_cash %}{{ form.page5.initial_payment|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Right
    FieldMaxLength: 22
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].Table1[0].Row1[0].Initial_Payment[0]
    FieldNameAlt: 20 percent Initial Payment
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page5.lump_sum_cash %}{{ form.page5.remaining_balance|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Right
    FieldMaxLength: 22
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].Table1[0].Row1[0].Remaining_Balance[0]
    FieldNameAlt: Total Offer Amount minus 20 percent Initial Payment equals Remaining
        Balance
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page5.lump_sum_cash %}{{ form.page5.offer_amount_lumpsum|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Right
    FieldMaxLength: 22
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].Table1[0].Row1[0].Total_Offer_Amount[0]
    FieldNameAlt: Total Offer Amount. Your offer must be more than zero ($0) and in
        whole dollars. Do not include cents.
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page5.periodic_payment %}{{ form.page5.pay_months }}{% else %}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].Total_Installment_Payments[0]
    FieldNameAlt: $[dollar amount] is included with this offer then $[dollar amount]
        will be sent in on the [day] of each month thereafter for a total of [Enter
        number of months] months with a final payment of $[dollar amount] to be paid
        on the  [day] of the [number of months] month.
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page5.lump_sum_cash %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].cB3_01[0]
    FieldNameAlt: 'Page 3. Section 5. Payment Terms; Check one of the payment options
        below to indicate how long it will take you to pay your offer in full. You
        must offer more than $0. The offer amount should be in whole dollars only.
        Lump Sum Cash. Check here if you will pay your offer in 5 or fewer payments
        in 5 or fewer months from the date of acceptance. Enclose a check for 20 percent
        of the offer amount (waived if you are an individual or sole proprietorship
        and met the requirements for Low Income Certification) and fill in the amount(s)
        and date(s) of your future payment(s). '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {% if form.page5.periodic_payment %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page3[0].Section5[0].cB3_02[0]
    FieldNameAlt: 'Check here if you will pay your offer in full in 6 to 24 months.  Enclose
        a check for one month''s installment '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 8388608
    value: {% if form.page6.has_deposit %}{{ form.page6.deposit_payment|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section6[0].Additional_Payment[0]
    FieldNameAlt: 'My payment of [dollar amount] includes the $186 application fee
        and $ [dollar amount] for my initial offer payment. I am requesting the additional
        payment of $ [Enter dollar amount] be held as a deposit. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page6.has_deposit %}{{ form.page6.initial_payment|intcomma_force }}{% else %}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section6[0].Initial_Offer_Payment[0]
    FieldNameAlt: 'My payment of [dollar amount] includes the $186 application fee
        and $ [Enter dollar amount] for my initial offer payment. I am requesting
        the additional payment of $ [dollar amount] be held as a deposit. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page6.has_deposit %}{{ form.page6.total_payment }}{% else %}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page3[0].Section6[0].Initial_Payment[0]
    FieldNameAlt: 'My payment of [Enter dollar amount] includes the $186 application
        fee and $ [dollar amount] for my initial offer payment. I am requesting the
        additional payment of $ [dollar amount] be held as a deposit. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page6.tax_form }}
    FieldJustification: Center
    FieldName: topmostSubform[0].F656_Page3[0].Section6[0].Tax_Form[0]
    FieldNameAlt: 'Section 6; Designation of Down Payment and Deposit. If you want
        your payment to be applied to a specific tax year and a specific tax debt,
        please tell us the tax form [enter form number] and tax year/quarter. '
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page6.tax_year }}
    FieldJustification: Center
    FieldName: topmostSubform[0].F656_Page3[0].Section6[0].Tax_Year_Quarter[0]
    FieldNameAlt: 'If you want your payment to be applied to a specific tax year and
        a specific tax debt, please tell us the tax form and [enter tax year/quarter]. '
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page6.has_deposit %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page3[0].Section6[0].cB3_04[0]
    FieldNameAlt: 'My payment of [dollar amount] includes the $186 application fee
        and $ [dollar amount] for my initial offer payment. I am requesting the additional
        payment of $ [dollar amount] be held as a deposit. '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page4[0]
    FieldType: ''
-   FieldFlags: 8388608
    value: {% if form.page6.noreturn_for %}{{form.page6.noreturn_for_years}}{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page4[0].Section7[0].Not_Required_To_File_Years[0]
    FieldNameAlt: 'I certify that I was not required to file a tax return for the
        following years: Enter Years. '
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page6.funds_source }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page4[0].Section7[0].Source_Of_Funds[0]
    FieldNameAlt: 'Page 4. Section 7. Source of Funds, Making Your Payment, and Filing
        Requirements. Source of Funds. Tell us where you will obtain the funds to
        pay your offer.  You may consider borrowing from friends and/or family, taking
        out a loan, or selling assets. '
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page6.all_taxreturns_filed %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page4[0].Section7[0].cB4_01[0]
    FieldNameAlt: 'Section 7. Source of Funds, Making Your Payment, and Filing Requirements.
        Filing Requirements. I certify that I have filed all required tax returns. '
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {% if form.page6.noreturn_for %}Yes{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: OffFieldStateOption: Yes'
    FieldName: topmostSubform[0].F656_Page4[0].Section7[0].cB4_02[0]
    FieldNameAlt: 'I certify that I was not required to file a tax return for the
        following years:'
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page5[0]
    FieldType: ''
-   FieldFlags: 8388608
    value: --empty--
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page5[0].Section9[0].Date_1[0]
    FieldNameAlt: Date (2 digit month, 2 digit day, 4 digit year)
    FieldType: Text
-   FieldFlags: 8388608
    value: --empty--
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page5[0].Section9[0].Date_2[0]
    FieldNameAlt: Date (2 digit month, 2 digit day, 4 digit year)
    FieldType: Text
-   FieldFlags: 8388608
    value: --empty--
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page5[0].Section9[0].Phone_Number_1[0]
    FieldNameAlt: Page 5. Section 9; Signatures; Under penalties of perjury, I declare
        that I have examined this offer, including accompanying schedules and statements,
        and to the best of my knowledge and belief, it is true, correct and complete.
        Signature of Taxpayer/Corporation Name; Phone Number.
    FieldType: Text
-   FieldFlags: 8388608
    value: --empty--
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page5[0].Section9[0].Phone_Number_2[0]
    FieldNameAlt: Signature of Taxpayer/Authorized Corporate Officer; Phone Number
    FieldType: Text
-   FieldFlags: 0
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page6[0]
    FieldType: ''
-   FieldFlags: 8388608
    value: {{ form.page7.preparer_date|date:"m/d/Y" }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page6[0].Section10[0].Date_Preparer_Signed[0]
    FieldNameAlt: Date (2 digit month, 2 digit day, 4 digit year)
    FieldType: Text
-   FieldFlags: 8392704
    value: {{ form.page7.preparer.get_firm_name_address }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page6[0].Section10[0].Firm_Name_Address[0]
    FieldNameAlt: Firm's Name (or yours if self-employed), Address, and ZIP Code (Include
        a valid, signed Form 2848 or 8821 with this application, if one is not on
        file.)
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page7.preparer.name }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page6[0].Section10[0].Name_Paid_Preparer[0]
    FieldNameAlt: Name of Paid Preparer
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page7.preparer.get_caf_or_ptin }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page6[0].Section10[0].Preparer_CAF_PTIN[0]
    FieldNameAlt: Preparer's C A F number or P T I N
    FieldType: Text
-   FieldFlags: 8388608
    value: {{ form.page7.preparer.phone }}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page6[0].Section10[0].Preparer_Phone[0]
    FieldNameAlt: 'Page 6. Section 10; Paid Preparer Use Only; Signature of Preparer;
        Phone Number '
    FieldType: Text
-   FieldFlags: 8388608
    value: --empty--
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page6[0].Section11[0].Date_Authorized_IRS_Official_Signed[0]
    FieldNameAlt: Date (2 digit month, 2 digit day, 4 digit year)
    FieldType: Text
-   FieldFlags: 8388608
    value: {% if form.page7.allow_designee %}{{ form.page7.designee_name }}{% else %}Off{% endif %}
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page6[0].Section11[0].Designee_Name[0]
    FieldNameAlt: If yes, provide designee's name
    FieldType: Text
-   FieldFlags: 8392704
    value: --empty--
    FieldJustification: Left
    FieldName: topmostSubform[0].F656_Page6[0].Section11[0].IRS_Title[0]
    FieldNameAlt: 'I R S Use Only; I accept the waiver of the statutory period of
        limitations on assessment for the Internal Revenue Service, as described in
        Section 8 (k). Signature of Authorized Internal Revenue Service Official;
        Title '
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page7.allow_designee %}{{ form.page7.designee_phone|getphonecode }}{% else %}Off{% endif %}
    FieldJustification: Center
    FieldMaxLength: 3
    FieldName: topmostSubform[0].F656_Page6[0].Section11[0].Phone[0].Area_Code[0]
    FieldNameAlt: Phone (Area Code)
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page7.allow_designee %}{{ form.page7.designee_phone|getphonemiddle }}{% else %}Off{% endif %}
    FieldJustification: Center
    FieldMaxLength: 3
    FieldName: topmostSubform[0].F656_Page6[0].Section11[0].Phone[0].Phone1[0]
    FieldNameAlt: Phone (Prefix)
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page7.allow_designee %}{{ form.page7.designee_phone|getphonelast }}{% else %}Off{% endif %}
    FieldJustification: Center
    FieldMaxLength: 4
    FieldName: topmostSubform[0].F656_Page6[0].Section11[0].Phone[0].Phone2[0]
    FieldNameAlt: Phone (Last four digits)
    FieldType: Text
-   FieldFlags: 0
    value: {% if form.page7.allow_designee %}1{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 1FieldStateOption: Off'
    FieldName: topmostSubform[0].F656_Page6[0].Section11[0].cB6_01[0]
    FieldNameAlt: Section 11. Third Party Designee; Do you want to allow another person
        to discuss this offer with the I R S? Yes
    FieldType: Button
    FieldValue: 'Off'
-   FieldFlags: 0
    value: {% if not form.page7.allow_designee %}1{% else %}Off{% endif %}
    FieldJustification: 'LeftFieldStateOption: 1FieldStateOption: Off'
    FieldName: topmostSubform[0].F656_Page6[0].Section11[0].cB6_02[0]
    FieldNameAlt: 'No'
    FieldType: Button
    FieldValue: 'Off'
