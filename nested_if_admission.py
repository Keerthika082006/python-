phy=int(input("emnter phy mark:"))
chy=int(input("enter chy mark:"))
maths=int(input("enter maths mark:"))
bio=int(input("enter bio mark:"))



physics=phy/100*50
chemistry=chy/100*50
medical_cutoff = physics+chemistry+bio
print("medical_cutoff:",medical_cutoff)

engeenering_cutoff=phy+chy+maths
print("engeenering_cutoff:",engeenering_cutoff)

course=input("enter ur course:").lower()

if "medical":
    print(f"qulified cutoff is 180 and ur cutoff {medical_cutoff}")

    if medical_cutoff<180:
        print("not qulified for medical")

    else:
        print("qulified for medical")

        if"engeenering":
             print(f"qulified cutoff is 160 and ur cutoff is {engeenering_cutoff}")
        elif engeenering_cutoff>160:
             print("qulified for engeenering")
        else:
            print("not qulified")

else:
    print("ur course is not avalable")

    
