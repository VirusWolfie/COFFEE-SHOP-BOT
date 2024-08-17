print("Welcome to Autochef")
name = input("What is your name? \n")
print("hello " + name + " which oil company would you prefer\n")
company = "TOTAL, ZIC, SHELL, ADDINOL, HONDA, TOYOTA, MOTUL, PERFORMA, KIXX"
print("Here are the available oil company \n" + company)
order = input()
print("\nNow which grade of " + order + " would you select from? \n")
grade = "0w20, 5w30, 10w40, 20w50"
print(grade + "?")
select = input()
print("Thank you sir for your purchase, we will prepare your " + order + " " + select + " right now")