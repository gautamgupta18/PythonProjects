marks = []
for i in range(5):
  mark = int(input("Enter Your marks:"))
  marks.append(mark)
print("Marks = " , marks)
avg = sum(marks)/5
print("Total = ", sum(marks))
print("Average = ", avg)
print("Highest Marks = ", max(marks))
print("Lowest Marks = ", min(marks))
if avg >= 90:
  print("Grade : A+")
elif avg >= 75:
  print("Grade : A")
elif avg >= 60:
  print("Grade : B")
elif avg >= 45:
  print("Grade : C")
elif avg >= 33:
  print("Grade : D")
else:
  print("Fail")