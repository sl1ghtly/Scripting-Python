value = int(input("enter a num: "))  
  
for num in range(1, value + 1):  
    if num > 1:  
        for i in range(2, num):  
            if (num % i) == 0:  
                break  
            else:  
                print(num)