# -*- coding: utf-8 -*-

from utils.templatetags.misc_helpers import intcomma_force
from irs_common.datasync import DataSync
from repository.const import STATE_CODE2NAME

"""
    MAX_INCOME: see form 656 section 4 (Low-Income Certification)
    Section 4: take the Gross Income from Section 5 of the 433-A form (#34 Total Income (add lines 20-33))
    and the size of the family and the state.
    Format: (family_size: (48 contiguous states and D.C., Hawaii, Alaska))
"""
MAX_INCOME = {
    1: (2431, 2796, 3038),
    2: (3277, 3769, 4096),
    3: (4123, 4742, 5154),
    4: (4969, 5715, 6213),
    5: (5815, 6688, 7271),
    6: (6660, 7660, 8329),
    7: (7506, 8633, 9388),
    8: (8352, 9606, 10446),
    0: (846, 973, 1058),
}

LOW_INCOME_SUGGEST_TPL = """<p class="suggestion">
Total income is <span class="sugg_source">${total_income}</span>
with a family of <span class="sugg_source">{family_size}</span>
in the state: <span class="sugg_source">{state_name}</span>
and <span class="decision">{decision}</span> qualify for Low Income Certification</p>
"""


def get_low_income_suggestion(client):
    dsync = DataSync(client)
    state_name = dsync.get('state_name')
    total_income = dsync.get('total_income', lambda: 0)()
    family_size = dsync.get('family_size', lambda: 0)()
    usestate = 0
    maxincome = 0
    if state_name == 'HI':  # Hawaii
        usestate = 1
    elif state_name == 'AK':  # Alaska
        usestate = 2
    if family_size <= 8:
        maxincome = MAX_INCOME[family_size][usestate]
    else:
        maxincome = MAX_INCOME[8][usestate] + MAX_INCOME[0][usestate] * (family_size - 8)
    decision = 'DO NOT'
    if total_income < maxincome:
        decision = 'DO'
    return decision, LOW_INCOME_SUGGEST_TPL.format(total_income=intcomma_force(total_income), family_size=family_size,
                                                   state_name=STATE_CODE2NAME[state_name], decision=decision)
