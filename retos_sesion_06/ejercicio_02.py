print("Operador XNOR")

# True XNOR True → True
a = True
b = True
print((a and b) or (not a and not b))  #True

# True XNOR False → False
a = True
b = False
print((a and b) or (not a and not b))  #False

# False XNOR True → False
a = False
b = True
print((a and b) or (not a and not b))  #False

# False XNOR False → True
a = False
b = False
print((a and b) or (not a and not b))  #True