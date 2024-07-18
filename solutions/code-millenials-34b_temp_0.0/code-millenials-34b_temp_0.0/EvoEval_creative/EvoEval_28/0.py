def calculate_progressive_tax(income: float, deductions=0) -> float:
    tax_brackets = [10000, 35000, 80000, float('inf')]
    tax_rates = [0.0, 0.15, 0.25, 0.3]
    deduction_brackets = [1000, 3000, float('inf')]
    deduction_ratios = [1, 2, 3]
    taxable_income = income - deductions
    tax = 0.0
    for i in range(len(tax_brackets)):
        if taxable_income > tax_brackets[i]:
            tax += tax_rates[i] * (taxable_income - tax_brackets[i - 1])
            taxable_income -= tax_brackets[i]
        else:
            tax += tax_rates[i] * taxable_income
            break
    return tax