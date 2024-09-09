#Create two Variables 
left_number = input ("Enter an interger: ")
right_number = input ("Enter an interger: ")

#create variable symbol
symbol = input ("Enter mathamatical operation ( +, -, * or /: ")

#Create the Result 
result = 0 

#Vailidate numbers are intergers
if not left_number.isnumeric or not right_number.isnumeric:
    print("Error both numbers must be intergers")
else:
    left_number = int(left_number)
    right_number = int(right_number)

# Perform Operations1


    match symbol:
        case "+":
            result = left_number + right_number
        case "-":
            result = left_number - right_number
        case "*":
            result = left_number * right_number
        case "/":
            if right_number == 0:
                print("Error - cannot divide by 0")
            else: result = left_number / right_number

        case _:
            print("Error: Invaild operation symbol")
# Print answer
print(result)



