weight=int(input("Enter any weight:-")) 
unit=input("(l)bs or (k)gs:-")
if unit.upper() =="L":
   converted=int(weight)*0.45
   print(f"your weight is {converted}kilos")
else:
   converted=int(weight)/0.45
   print(f"your weight is {converted}pounds")
