#Grade student based on marks.

print("WELLCOME")
print("BRABU")
paper1 = float(input("Enter paper1 marks ="))
paper2 = float(input("Enter paper2 marks ="))
paper3 = float(input("Enter paper3 marks ="))
paper4 = float(input("Enter paper4 marks ="))
paper5 = float(input("Enter paper5 marks ="))
paper6 = float(input("Enter paper6 marks ="))

print("get result")

if(paper1 >= 90):
    print("Grade A")
elif(paper1 >= 80 and paper1 < 90):
    print("Grade B")
elif(paper1 >= 70 and paper1 < 80):
    print("Grade C")
elif(paper1 >= 60 and paper1 < 70):
    print("Grade D")
else:
    print("permoted paper1")


if(paper2 >= 90):
    print("Grade A")
elif(paper2 >= 80 and paper2 < 90):
    print("Grade B")
elif(paper2 >= 70 and paper2 < 80):
    print("Grade C")
elif(paper2 >= 60 and paper2 < 70):
    print("Grade D")
else:
    print("permoted paper2")


if(paper3 >= 90):
    print("Grade A")
elif(paper3 >= 80 and paper3 < 90):
    print("Grade B")
elif(paper3 >= 70 and paper3 < 80):
    print("Grade C")
elif(paper3 >= 60 and paper3 < 70):
    print("Grade D")
else:
    print("permoted paper3")


if(paper4 >= 90):
    print("Grade A")
elif(paper4 >= 80 and paper4 < 90):
    print("Grade B")
elif(paper4 >= 70 and paper4 < 80):
    print("Grade C")
elif(paper4 >= 60 and paper4 < 70):
    print("Grade D")
else:
    print("permoted paper4")


if(paper5 >= 90):
    print("Grade A")
elif(paper5 >= 80 and paper5 < 90):
    print("Grade B")
elif(paper5 >= 70 and paper5 < 80):
    print("Grade C")
elif(paper5 >= 60 and paper5 < 70):
    print("Grade D")
else:
    print("permoted paper5")

if(paper6 >= 90):
    print("Grade A")
elif(paper6 >= 80 and paper6 < 90):
    print("Grade B")
elif(paper6 >= 70 and paper6 < 80):
    print("Grade C")
elif(paper6 >= 60 and paper6 < 70):
    print("Grade D")
else:
    print("permoted paper6")

final = (paper1+paper2+paper3+paper4+paper5+paper6)/6
print("%",final)
if(final >= 60):
    print("First")
elif(final >= 45 and final < 60):
    print("Second")
elif(final >= 30 and final < 45):
    print("Third")
else:
    print("fail.")
