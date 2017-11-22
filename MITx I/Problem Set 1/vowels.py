vowels = 0
s = str(input("Enter a string: "))
for falchion in s:
    if falchion == 'a' or falchion == 'e' or falchion == 'i' or falchion == 'o' or falchion == 'u':
        vowels += 1
else: 
    vowels += 0
    print("Number of vowels: " , vowels)
