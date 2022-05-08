#Tpye 5 unique number
list_1 = []
while len(list_1) < 5:
    string = input('Enter str :')
    if string in list_1:
        pass
    else:
        list_1.append(string)
print(list_1)