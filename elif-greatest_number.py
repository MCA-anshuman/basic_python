#WAP input three number & check greatest number.

no1 = float(input("Enter first no:"))
no2 = float(input("Enter Second no:"))
no3 = float(input("Enter third no:"))
if(no1>=no2 and no1>=no3):
    print(no1 ,"Greatest number")
elif(no2>=no3):
    print(no2,"Greatest number")
else:
    print(no3,"Greatest number")
