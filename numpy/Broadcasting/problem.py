prices=[100,200,300]

discount=10

final_price=[]

for cost in prices:
    cost=cost-cost*discount/100
    final_price.append(cost)

print(final_price)


# loops are slow we can use broadcasting instead of this 
# its a numpy way we can perform operation on diff shapes arrays
# without using loops
# Fast in execution 
