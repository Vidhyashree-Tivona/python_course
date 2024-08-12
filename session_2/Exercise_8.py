"""Module to calculate the professional tax applicable for the employee based
on the salary of employee

This module has function to calculate the professional tax for the employee's
Salary based on the
income.
"""


def cal_salary(salary):
    """Calculate the professional tax for the employees
    Parameter:
    salary- To check if professional tax is applicable
    Result:
    The professional tax is calculated"""
    if salary < 10000:
        return None
    else:
        professional_tax = salary * 0.0025
        return professional_tax


name = input("Enter the employee name: ")
salary = eval(input("Enter your salary: "))
print("Name of the employee = ", name)
print(f"The salary of the employee {name} = ", salary)
print("The professional tax applicable = ", cal_salary(salary))
