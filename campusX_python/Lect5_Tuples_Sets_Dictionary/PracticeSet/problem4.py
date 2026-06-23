# Q4`: Count no of tuples, list and set from a list
# list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

# Output:
# List-2
# Set-2
# Tuples-1

list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

List=0
Set=0
Tuples=0

for i in list1:
    if i == tuple(i):
        Tuples+=1
    if i == set(i):
        Set+=1
    if i == list(i):
        List+=1

print(f'lists - {List}')
print(f'sets - {Set}')
print(f'tuples - {Tuples}')


