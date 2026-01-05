# Jordan AM
# 7
# Value Return Function HW
# Time Spent: 20 minutes

a = int(input("Input a number: ")) #inputs
b = int(input("Input a number: "))

#function
def muth(a, b):

    aa = a + b
    ac = a - b
    am = a * b
    ad = a / b

    return(aa, ac, am, ad)

aa, ac, am, ad = muth(a, b)

#print
print(aa)
print(ac)
print(am)
print(ad)



input("Press enter to quit...")