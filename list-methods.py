student = [4,1,3]
student.append(6)
print(student)

student.sort()
print(student)

student.sort(reverse='True')
print(student)

student.reverse()
print(student)

student.insert(1,4)
print(student)

student.remove(6)         #remove first occurrence of element.
print(student)

student.pop(3)            #remove element at idx.
print(student)