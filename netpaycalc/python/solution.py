def net_pay_cal(gross_pay):
    nssf = compute_nssf(gross_pay)
    paye = compute_paye(gross_pay)
    return gross_pay - nssf['employee'] - paye

def compute_paye(gross_pay):
    second_tax_bracket_rate = 0.1
    third_tax_bracket_rate = 0.2
    fourth_tax_bracket_rate = 0.3
    over_ten_million = 0.1
    paye = 0

    if gross_pay < 235000:
        paye = 0
    elif 235000 <= gross_pay and gross_pay <= 335000:
        paye = second_tax_bracket_rate * gross_pay
    elif 335000 <= gross_pay and gross_pay <= 410000:
        paye = 10000 + third_tax_bracket_rate * (gross_pay - 335000)
    elif 410000 <= gross_pay and gross_pay <= 10000000:
        paye = 25000 + fourth_tax_bracket_rate * (gross_pay - 410000)
    else:
        paye = 25000 + (fourth_tax_bracket_rate * (gross_pay - 410000)) + (over_ten_million * (gross_pay - 10000000))
    return paye
        

def compute_nssf(gross_pay):
    employee_rate = 0.05
    employer_rate = 0.1
    employee_contribution = employee_rate * gross_pay
    employer_contribution = employer_rate * gross_pay
    total_contribution = employee_contribution + employer_contribution
    result = {}
    result['total'] = total_contribution
    result['employer'] = employer_contribution
    result['employee'] = employee_contribution
    return result

if __name__ == "__main__":
    print net_pay_cal(10740000)