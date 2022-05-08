# Prime Cheack
count = 0
number = int(input('Enter number:'))

for i in range(1, number+1):
    if number%i == 0:
        count = count + 1
if count == 2 :
    print('Is prime')
else:
    print('Is not prime')

