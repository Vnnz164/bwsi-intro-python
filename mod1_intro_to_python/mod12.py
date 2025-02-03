#1
one = "hello world"
two = 1
three = 1.1
four = [1,2]
five = (1,2)
six = False

#2
patient_names = ["John","Karl","Ashley","Cameron","Steve"]
patient_ages = [26,29,40,25,30]

#3
a = 2.8
b = 9
c = 66
x = 2
result = a*x**b+x/b-c
print(result)

#setup
grades = [99, 81, 95, 97, 81, 92, 98, 89, 95, 86]
#4
# The first element of the list?
print(f"The first element is: {grades[0]}")

# The 4-6th elements of the list?
print(f"The 4-6th elements in the list are: {grades[4:7]}")


# The 3rd element from the end of the list?
print(f"The 3rd element from the end of the list is: {grades[-3]}")

#4
indexed_grades = grades[2:4]+grades[7:10]
print(f"The indexed grades from the list are: {  indexed_grades  }")
