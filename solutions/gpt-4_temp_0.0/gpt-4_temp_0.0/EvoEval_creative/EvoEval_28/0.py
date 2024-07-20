def calculate_progressive_tax(income: float, deductions=0) -> float:
    if deductions <= 1000:
        income -= deductions
    elif deductions <= 3000:
        income -= 1000 + (deductions - 1000) * 2
    else:
        income -= 1000 + 2000 * 2 + (deductions - 3000) * 3
    if income <= 10000:
        tax = 0
    elif income <= 35000:
        tax = (income - 10000) * 0.15
    elif income <= 80000:
        tax = 25000 * 0.15 + (income - 35000) * 0.25
    else:
        tax = 25000 * 0.15 + 45000 * 0.25 + (income - 80000) * 0.3
    return tax