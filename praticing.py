even_odd = dict()
numbers = input('enter list of numbers:')
even_numbers = []
odd_numbers = []

list_num = list(numbers)
list_num2=[]

for num in list_num:
    num = int(num)
    list_num2.append(num)

for num in list_num2:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)    

even_odd['even'] = even_numbers
even_odd['odd'] = odd_numbers        

print(even_odd['even'])
print(even_odd['odd'])