#  Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%


salary = float(input("Entert Salalry: "))


if salary <= 500000:
    salary_deduction= salary-(0.10*salary+0.05*salary+0.03*salary)
    print("Salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction: ",salary_deduction)
elif salary in range (500000 , 1000000):
    salary_deduction= salary-(0.10*salary+0.05*salary+0.03*salary+0.10*salary)
    print("Salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction: ",salary_deduction)
elif salary in range (1000000 , 2000000):
    salary_deduction= salary-(0.10*salary+0.05*salary+0.03*salary+0.20*salary)
    print("Salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction: ",salary_deduction)
elif salary >= 2000000:
    salary_deduction= salary-(0.10*salary+0.05*salary+0.03*salary+0.30*salary)
    print("Salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction: ",salary_deduction)
