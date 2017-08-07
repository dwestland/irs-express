
"""
    This module contains a class intended to link all IRS forms of the same client together.
    It can provide data filled in one form to another.
    For example, if we starting to fill up the form 9465 and we need to get initial value for the first_name field,
    it will look up for the value in the following order:
    * form 433a
    * form 656
    * form 9465 (in this abstaction layer we do not care where the request comes from)
    * form 8821
    * client model

    We assume that data entered in the form has higher priority than in
    client's model as they were entered later (maybe)
"""

from clients.models import Client

DATA_SOURCES = {
    'first_name':
        ['form433a.page1.first_name', 'form656.page1.first_name', 'form9465.page1.first_name',
         'form8821.page1.first_name', 'client.first_name',
         ],
    'middle_name':
        ['form433a.page1.middle_name', 'form656.page1.middle_name', 'form9465.page1.middle_name',
         'form8821.page1.middle_name', 'client.middle_name',
         ],
    'last_name':
        ['form433a.page1.last_name', 'form656.page1.last_name', 'form9465.page1.last_name',
         'form8821.page1.last_name', 'client.last_name',
         ],
    'ssn': ['form433a.page1.ssn', 'form656.page1.ssn', 'form9465.page1.ssn', 'form8821.page1.ssn', ],
    'family_size': ['form433a.page1.get_family_size', ],
    'street':
        ['form433a.page1.street', 'form656.page1.street', 'form9465.page1.street',
         'form8821.page1.street', 'client.street',
         ],
    'apt':
        ['form433a.page1.apt', 'form656.page1.apt', 'form9465.page1.apt',
         'form8821.page1.apt', 'client.apt',
         ],
    'city':
        ['form433a.page1.city', 'form656.page1.city', 'form9465.page1.city',
         'form8821.page1.city', 'client.city',
         ],
    'county':
        ['form433a.page1.county', 'form656.page1.county', 'form9465.page1.county',
         'form8821.page1.county', 'client.county',
         ],
    'state_name':
        ['form433a.page1.state_name', 'form656.page1.state_name', 'form9465.page1.state_name',
         'form8821.page1.state_name', 'client.state_name',
         ],
    'zipcode':
        ['form433a.page1.zipcode', 'form656.page1.zipcode', 'form9465.page1.zipcode',
         'form8821.page1.zipcode', 'client.zipcode',
         ],
    'phone_cell':
        ['form433a.page1.phone_cell', 'client.phone_cell',
         ],
    'phone_home':
        ['form433a.page1.phone_home', 'form656.page1.phone_home',
         'form9465.page2.phone_home', 'form8821.page1.phone', 'client.phone_home',
         ],
    'phone_home_bttc':
        ['form433a.page1.phone_home_bttc', 'form9465.page2.phone_home_bttc', ],
    'phone_work':
        ['form433a.page1.phone_work', 'form656.page1.phone_work', 'form656.page1.businessinfo.phone',
         'form9465.page2.phone_work', 'client.phone_work', ],
    'phone_work_ext':
        ['form433a.page1.phone_work_ext', 'form9465.page2.phone_work_ext', ],
    'phone_work_bttc':
        ['form433a.page1.phone_work_bttc', 'form9465.page2.phone_work_bttc', ],
    'ein':
        ['form433a.page1.ein', 'form433a.page7.ein', 'form656.page1.ein', 'form9465.page2.ein',
         'form656.page1.businessinfo.ein'],

    'married':
        ['form433a.page1.married', 'form656.page1.jointoffer.?', 'form9465.page1.jointoffer.?',
         ],
    'jointoffer':
        ['form433a.page1.spouse.return_with', 'form656.page1.jointoffer.?', 'form9465.page1.jointoffer.?',
         ],
    'spouse_first_name':
        ['form433a.page1.spouse.first_name', 'form656.page1.jointoffer.first_name',
         'form9465.page1.jointoffer.first_name', 'form8821spouse.page1.first_name',
         ],
    'spouse_middle_name':
        ['form433a.page1.spouse.middle_name', 'form656.page1.jointoffer.middle_name',
         'form9465.page1.jointoffer.middle_name', 'form8821spouse.page1.middle_name',
         ],
    'spouse_last_name':
        ['form433a.page1.spouse.last_name', 'form656.page1.jointoffer.last_name',
         'form9465.page1.jointoffer.last_name', 'form8821spouse.page1.last_name',
         ],
    'spouse_ssn':
        ['form433a.page1.spouse.ssn', 'form656.page1.jointoffer.ssn', 'form9465.page1.jointoffer.ssn',
         'form8821spouse.page1.ssn', ],

    'business_name': ['form433a.page7.business_name', 'form9465.page2.business_name',
                      'form656.page1.businessinfo.name'],
    'business_street': ['form433a.page7.business_street', 'form656.page1.businessinfo.street'],
    'business_city': ['form433a.page7.business_city', 'form656.page1.businessinfo.city'],
    'business_state_name': ['form433a.page7.business_state_name', 'form656.page1.businessinfo.state_name'],
    'business_zipcode': ['form433a.page7.business_zipcode', 'form656.page1.businessinfo.zipcode'],

    'employer_name': ['form433a.page2.employment_info.employer_name', 'form9465.page2.employer_name'],
    'employer_street': ['form433a.page2.employment_info.street', 'form9465.page2.employer_street'],
    'employer_city': ['form433a.page2.employment_info.city', 'form9465.page2.employer_city'],
    'employer_state_name': ['form433a.page2.employment_info.state_name', 'form9465.page2.employer_state_name'],
    'employer_zipcode': ['form433a.page2.employment_info.zipcode', 'form9465.page2.employer_zipcode'],
    'pay_period': ['form433a.page2.employment_info.pay_period', 'form9465.page4.pay_period'],
    'spouse_pay_period': ['form433a.page2.spouse_employment_info.pay_period', 'form9465.page4.spouse_pay_period'],
    'vehicles_count': ['form433a.page5.get_vehicles_count', 'form9465.page4.vehicles'],
    'health_insurance': ['form433a.page6.health', ],
    'total_income': ['form433a.page6.total_income', ],
    'net_difference': ['form433a.page6.net_difference', ],
    'debt_total': ['form656.page5.debt_total', ],
    'monthly_income': ['form656.page5.monthly_income', ],
    'assessed_date': ['form656.page5.assessed_date', ],
    'offer_amount': ['form656.page5.offer_amount_lumpsum', ],
}


class DataSync(object):

    def __init__(self,
                 client: 'client_id or Client instance',
                 ignore: 'list: names of the forms to ignore (i.e. form433a)' = None,
                 ):
        self.client = client
        if isinstance(client, int):
            self.client = Client.objects.get(pk=client)
        self.sources = {
            'form433a': self.client.get_form_433a(create=False),
            'form656': self.client.get_form_656(create=False),
            'form9465': self.client.get_form_9465(create=False),
            'form8821': self.client.get_form_8821(create=False),
            'form8821spouse': self.client.get_form_8821spouse(create=False),
            'client': self.client,
        }
        if ignore:
            if not isinstance(ignore, (list, tuple, set)):
                ignore = [ignore]
            for i in ignore:
                if i in self.sources:
                    del self.sources[i]

    def get_obj_data(self,
                     path: 'string like "form433a.page1.first_name"'):
        """
            Accept paths like:
            * form433a.page1.first_name - returns first_name or None
            * form433a.page1.first_name.? - returns True if first_name exists or None otherwise
        """
        # divide path by dots
        pathes = path.split('.')
        # first element - should be in sources
        obj = self.sources.get(pathes[0])
        if not obj:
            return None
        for pathpart in pathes[1:]:
            if pathpart == '?':
                return True
            obj = getattr(obj, pathpart, None)
            if obj is None:
                return None
        return obj

    def get(self, attrname, default=''):
        if attrname not in DATA_SOURCES:
            return default
        locations = DATA_SOURCES[attrname]
        for l in locations:
            value = self.get_obj_data(l)
            if value is not None:
                return value
        return default
