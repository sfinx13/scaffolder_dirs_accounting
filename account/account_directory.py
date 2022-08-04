import enum


class AccountDirectory(enum.Enum):
    transportation_costs = '1-frais-transport'
    meal_costs = '2-frais-repas'
    common_charges = '3-charges-communes'
    purchase_cost = '4-frais-achats'
    donation = '5-dons'
