#A
total = 0
for i in range(2, 101, 2):
   total += i

print("total of even numbers from 2 to 100 is ", total)

#B
total = 0
for i in range(1, 11):
   total += i*i

print("total of 1 to 10 squared is ", total)

#C
total = 0
a = int(input("Enter lower: "))
b = int(input("Enter upper: "))
for i in range(a, b+1):
      if i % 2 != 0:
         total += i

print("odd numbers from ", a, " to " , b," added together is: ", total)        

#D
total = 0
num1 = input("enter a num: ")
for ch in num1:
   num2 = int(ch)
   if num2 % 2 == 1:
         total += num2

print("total of odd digits in ", num1, " is ", total)
   







