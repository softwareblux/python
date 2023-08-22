

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return
#     fff = f_name.title()
# #     lll= l_name.title()
# #     return f"{fff} {lll}"

# # fn = format_name(f_name=input("first name? "), l_name=input("last name? "))
# # print(fn)

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   if month > 12 or month<1:
#     return "invalid month"
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap(year) and month == 2:
#     return 29
#   return month_days[month - 1]
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
import sys, os
import dag10art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1/n2

def multi(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "/": div,
    "*": multi
}



def calculator():
  
  print(dag10art.logo)
  
  num1 = float(input("Whats the first number?: "))


  for operation in operations:
      print(operation)

  should_continue = True

  while should_continue:

    operation_symbol = input("pick another operation: ")

    num2 = float(input("Whats the next number?: "))

    calc_fun =  operations[operation_symbol]

    answer = calc_fun(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    oui = input(f"type 'y' to continue calculating with {answer} or type 'n' to start a new calculation.: ")

    if oui == "y":
      num1 = answer
      os.system('cls')
    elif oui == "n":
      should_continue = False
      calculator()
    else:
       should_continue = False
  
calculator()