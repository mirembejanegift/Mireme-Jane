#write down steps with code examples that you can use in calculating someone's net pay after tax. 
# Net income is the income that is received after all deductions have begin made
def salary():
    gross_income = 3000000
    return gross_income
print(salary())

#print(salary())just enables us to run the function and show output
# The gross income is the salary that one gets befor any deductions
# so initially this person gets 3000000
def tax():
    return salary()* 0.10
print(tax())

# here i have told python to go to the salary and then calculate 10% of it and 
# to make it the tax

# Calculate the net_income
# net_income = gross_income-tax
def net_income():
    return salary()- tax()
print(net_income())

