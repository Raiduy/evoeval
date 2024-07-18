def calculate_progressive_tax(income: float, deductions=0) -> float:
    tax_free_income = 10000
    tax_brackets = [(25000, 0.15), (45000, 0.25), (float('inf'), 0.3)]
    taxable_income = income - tax_free_income
    tax = 0
    for bracket in tax_brackets:
        if taxable_income <= 0:
            break
        if taxable_income <= bracket[0]:
            tax += taxable_income * bracket[1]
            taxable_income = 0
        else:
            tax += bracket[0] * bracket[1]
            taxable_income -= bracket[0]
    deductions_ratios = [(1000, 1), (2000, 2), (float('inf'), 3)]
    for ratio in deductions_ratios:
        if deductions <= 0:
            break
        if deductions <= ratio[0]:
            tax -= deductions * ratio[1]
            deductions = 0
        else:
            tax -= ratio[0] * ratio[1]
            deductions -= ratio[0]
    return tax