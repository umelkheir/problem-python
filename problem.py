def convert_dollars(dollars):
    message_one =" Dollars are "
    message_two = " Euros"
    ##One of the errors is this result line below 
    result = int((dollars/1.06))
    return str((dollars))  + message_one + str(result) + message_two

user_input = input("How many dollars would you like to convert: ")
##The error was in this dollars_result line below 
dollars_result = int(convert_dollars(user_input)) 

if float(user_input) > 50:
    print("Wow that is a lot of money")

print(dollars_result)
