def calculate_progressive_tax(income: float, deductions=0) -> float:
    """
    Calculate the tax for a given income and deductions according to a set of progressive tax rates:

    - Up to $10,000 of income is tax-free
    - The next $25,000 is taxed at 15%
    - The next $45,000 is taxed at 25%
    - Any income over $130,000 is taxed at 30%

    The function also considers tax reductions due to deductions:
        - The first $1000 of deductions are subtracted at a 1:1 ratio from the taxable income
        - The next $2000 of deductions are subtracted at a 2:1 ratio from the taxable income
        - Any deduction over $3000 is subtracted at a 3:1 ratio from the taxable income

    It should return a float representing the amount of tax.

    Examples:
    >>> calculate_progressive_tax(12000, 500)
    225.0
    >>> calculate_progressive_tax(55000, 2500)
    7750.0
    >>> calculate_progressive_tax(120000, 5000)
    23700.0
    """
    taxable_income = income - deductions
    if taxable_income <= 10000:
        tax = 0
    elif taxable_income <= 35000:
        tax = (taxable_income - 10000) * 0.15
    elif taxable_income <= 80000:
        tax = 3750 + (taxable_income - 35000) * 0.25
    else:
        tax = 13125 + (taxable_income - 80000) * 0.3
    return tax