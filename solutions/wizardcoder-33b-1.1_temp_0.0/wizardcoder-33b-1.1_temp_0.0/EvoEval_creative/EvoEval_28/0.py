def calculate_progressive_tax(income: float, deductions=0) -> float:
    taxable_income = income - deductions
    tax = 0
    if taxable_income > 130000:
        tax += (taxable_income - 130000) * 0.3
        taxable_income = 130000
    if taxable_income > 85000:
        tax += (taxable_income - 85000) * 0.25
        taxable_income = 85000
    if taxable_income > 35000:
        tax += (taxable_income - 35000) * 0.15
        taxable_income = 35000
    if taxable_income > 10000:
        tax += (taxable_income - 10000) * 0.0
        taxable_income = 10000
    return tax