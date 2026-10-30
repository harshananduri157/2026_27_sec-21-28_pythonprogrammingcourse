p=float(input("enter the principle amount:"))
r=float(input("enter the annual intrest rate:"))
t=float(input("enteer the time in yeras:"))
a=p*(1+r/100)**t
compound_intrest=a-p
print("the compound intrest is:",compound_intrest)
print("the total amount after",t,"years is",a)
      
