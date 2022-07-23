print("KALYAN JWELLERS")
firstname = input("First Name : ")
lastname = input("Last Name : ")
PA = int(input("Purchase Amount : "))
gender = input("Gender : ")
age = int(input("Age : "))
Vaccination = (input("Vaccination Status : "))
discountA = 0
if PA >= 100000 and PA <= 200000:
    MakingC = 0.08*PA
    Making = PA + (0.08*PA)
    print("Making Charge:", MakingC )
    print("Purchase Amount With Making Charge :", Making)
elif PA > 200000 and PA < 300000:
    MakingC = 0.12*PA
    Making = PA + (0.12*PA)
    print("Making Charges:", Making)
elif PA >=300000:
    MakingC = 0.16*PA
    Making = PA + (0.16*PA)
    print("Making Charge:", Making) 
else:
    pass
if age>=60:
    print("Senior Citizen:", gender)
    if gender == "Male":
        if PA >= 100000 and PA < 200000:
            discountA = 0.15*PA
            Discount = PA - (0.15*PA)
            print("Discount Amount:", Discount)
            print("Senior Citizen Male")
        elif PA >= 200000 and PA < 300000:
            discountA = 0.25*PA
            Discount = PA - (0.25*PA)
            print("Discount Amount:", Discount)
        elif PA >= 300000:
            discountA = 0.35*PA
            Discount = PA - (0.35*PA)
            print("Discount Amount:", Discount)
    else:
        if PA >= 100000 and PA < 200000:
            discountA = 0.20*PA
            Discount = PA - (0.20*PA)
            print("Discount Amount:", Discount)
        elif PA >= 200000 and PA < 300000:
            discountA = 0.30*PA
            Discount = PA - (0.30*PA)
            print("Discount Amount:", Discount)
        elif PA >= 300000:
            discountA = 0.40*PA
            Discount = PA - (0.40*PA)
            print("Discount Amount:", Discount)
        else:
            pass
else:
    pass

if age <= 60:
    print("Citizen:", gender)
    if gender == "Male":
        if PA >= 100000 and PA < 200000:
            discountA = 0.10*PA
            Discount = PA - (0.10*PA)
            print("Discount Amount:", Discount)
        elif PA >= 200000 and PA < 300000:
            discountA = 0.20*PA
            Discount = PA - (0.20*PA)
            print("Discount Amount:", Discount)
        elif PA >= 300000:
            discountA = 0.30*PA
            Discount = PA - (0.30*PA)
            print("Discount Amount:", Discount)
    else:
        if PA >= 100000 and PA < 200000:
            discountA = 0.15*PA
            Discount = PA - (0.15*PA)
            print("Discount Amount:", Discount)
        elif PA >= 200000 and PA < 300000:
            discountA = 0.25*PA
            Discount = PA - (0.25*PA)
            print("Discount Amount:", Discount)
        elif PA >= 300000:
            discountA = 0.35*PA
            Discount = PA - (0.35*PA)
            print("Discount Amount:", Discount)
        else:
            pass
else:
    pass

netamount = PA + MakingC - discountA

print("Purchase :", PA)
print("Making Charge :", MakingC)
print("Discount :", discountA)
print("Discount Amount :", Discount)

print("Net Amount :", netamount)