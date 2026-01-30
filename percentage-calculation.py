#take marks as input from user
print("Enter Marks Obtained in 4 Subjects:")
math = int(input("Maths :"))
english = int(input("English:"))
science = int(input("Science:"))
Bangla = int(input("Bangla:"))
ict = int(input("ICT:"))

#lets calculate the percentage of marks
sum = math+english+science+Bangla+ict
print("sum of Math,English,Science,Bangla,ICT is, sum")

percentage = (sum/500)*100
print("percentage mark =",percentage)