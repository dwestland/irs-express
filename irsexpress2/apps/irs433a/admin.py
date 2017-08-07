# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (Form433a,
                     F433aPage1, ClientDependent, ClientSpouse,
                     F433aPage2, EmploymentInfo,
                     F433aPage3, LawsuitPartyInfo, BankruptcyInfo, BeneficiaryInfo,
                     LiveAbroadDetails, TrusteeDetails, SafeDetails, AssetTransferDetails,
                     F433aPage4, BankAccountInfo, InvestmentInfo, CreditInfo, InsuranceInfo,
                     F433aPage5, RealPropertyInfo, VehicleInfo, PersonalAssetInfo,
                     F433aPage6,
                     F433aPage7, PaymentProcessorInfo, BusinessCreditCardInfo, BusinessBankAccountInfo,
                     AccountsReceivableInfo, BusinessAssetInfo,
                     F433aPage8,
                     )

# Register your models here.

admin.site.register((Form433a,
                     F433aPage1, ClientDependent, ClientSpouse,
                     F433aPage2, EmploymentInfo,
                     F433aPage3, LawsuitPartyInfo, BankruptcyInfo, BeneficiaryInfo,
                     LiveAbroadDetails, TrusteeDetails, SafeDetails, AssetTransferDetails,
                     F433aPage4, BankAccountInfo, InvestmentInfo, CreditInfo, InsuranceInfo,
                     F433aPage5, RealPropertyInfo, VehicleInfo, PersonalAssetInfo,
                     F433aPage6,
                     F433aPage7, PaymentProcessorInfo, BusinessCreditCardInfo, BusinessBankAccountInfo,
                     AccountsReceivableInfo, BusinessAssetInfo,
                     F433aPage8,
                     ))
