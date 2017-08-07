
US_STATES = [
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
]

STATES_EXTENDED = US_STATES + [
    ('PUER', 'Puerto Rico'),
]

STATE_NAMES = ((sn, sn) for sn in sorted(dict(STATES_EXTENDED).values()))
STATE_CODE2NAME = dict(STATES_EXTENDED)

CLIENT_STATUS = (
    ('active', 'Active'),
    ('onhold', 'On Hold'),
    ('closed', 'Closed'),
)

TRANSPORTATION_TAX_TYPE = (
    ('publictrans', 'Public Transportation'),
    ('ownership', 'Ownership Costs'),
    ('operating', 'Operating Costs'),
)

# used in form 433a
PAYPERIODS = (
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('bi-weekly', 'Bi-Weekly'),
    ('other', 'Other'),
)

# for form 9465
PAYPERIODS2 = (
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('bi-weekly', 'Bi-Weekly'),
    ('twice-a-month', 'Twice a Month'),
)
