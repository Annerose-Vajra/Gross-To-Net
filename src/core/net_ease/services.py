from .constants import INSURANCE_RATES

def calculate_insurance(gross: float) -> float:
    return gross * sum(INSURANCE_RATES.values())

def calculate_tax(taxable_income: float) -> float:
    if taxable_income <= 0:
        return 0
    if taxable_income <= 5000000:
        return taxable_income * 0.05
    elif taxable_income <= 10000000:
        return 250000 + (taxable_income - 5000000) * 0.1
    return 750000 + (taxable_income - 10000000) * 0.2

def gross_to_net(gross: float, region: str) -> dict:
    insurance = calculate_insurance(gross)
    taxable_income = gross - insurance - 11000000
    tax = calculate_tax(taxable_income)
    total_deduction = insurance + tax
    net = gross - total_deduction
    return {
        'net_salary': round(net, 2),
        'insurance': round(insurance, 2),
        'personal_income_tax': round(tax, 2),
        'total_deductions': round(total_deduction, 2)
    }
