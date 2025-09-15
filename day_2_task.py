# task 1
amount=int(input("enter your amount :"))
is_member=bool(input("true/false :"))
result=amount
if amount >=5000 and is_member == True:
    result=amount*(20/100)
elif amount >= 3000 and is_member == True:
    result=amount*(10/100)
elif amount < 3000 :
    result=0
final_amount=amount-result
print("total discount :",result)
print("The final amount to pay :",final_amount)
 
#task 2
marks=float(input("enter marks :"))
attendance=int(input("enter your attendance :"))

if (marks>=80 and attendance>=75) or marks>=90 :
    print("eligible")
else:
    ("not eligible")



#task 3
num_1=[1,2,3,4]
num_2=[1,2,3,4]
num_3=num_1

print(num_1 is num_2)
print(num_1 is num_3)
print(3 in num_2)
