# find number of uppercase letter

string=str(input("Enter a word/ sentence:"))
count1=0

for i in string:
      if(i.isupper()):
            count1=count1+1
print("The number of uppercase characters is:", count1)

