"""Gross salary = Basic salary + dear allowance +house rent
house rent is 40% of basic salary
dearness allowance """""
basic_salary = float(input('Enter the basic salary of the person : '))
hra = ((basic_salary/100)*40)
da = ((basic_salary/100)*50)
gross_salary = basic_salary+hra+da
print(f'Gross salary of the basic Pay {basic_salary} will be : ',gross_salary)
