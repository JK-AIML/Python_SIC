# using advanced form of returning boolean with conditionals:

#advanced return for conditonals
def is_odd(a):
    #syn: return <value> if <conditon> else <value>
    return True if a % 2 == 1 else False

#making it shorter as comparison only gives true or false
def is_odd(a):
    return a % 2 ==1

a = int(input("enter num"))
if is_odd(a):
    print("y")
else:
    print("n")