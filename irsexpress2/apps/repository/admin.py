from django.contrib import admin

from .models import (County,
                     HousingUtilitiesStandard, FoodClothingStandard, OutOfPocketHealthCare, TransportationStandard,
                     DocumentStatus)
# Register your models here.

admin.site.register((County,
                    HousingUtilitiesStandard, FoodClothingStandard, OutOfPocketHealthCare, TransportationStandard,
                    DocumentStatus))
