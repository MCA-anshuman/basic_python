#WAP to check if a number entered by the user is odd or even.
no = int(input("Enter any no="))
r = no%2
if(r == 0):
    print("even")
else:
    print("odd")