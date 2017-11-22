bobtext = 0
s = input("Enter a string with bob: ")
for i in range (len(s)):
    if s[i : i + 3] == 'bob':
      bobtext += 1
else:
      bobtext += 0
      print("Number of times BOB occurs: ", bobtext)
