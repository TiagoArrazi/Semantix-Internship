def divide(num1, num2):
        if num1 < num2:
            return 0
        elif num1 == num2:
            return 1
        else:
            result = 0
            counter = 0
            while True:
                result+=num2 #result = Addition.add(result, num2)
                if result < num1:
                    counter+=1 #counter = Addtion.add(counter, 1)
                else:
                    break
            
            return counter
        
print(divide(2,3))
print(divide(2,2))
print(divide(10,4))
