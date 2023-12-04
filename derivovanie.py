#!/usr/bin/env python3
def myderive(f, var):
    if type(f) == int:
        return 0
    elif f == var:
        return 1
    elif type(f) == list:
        if f[0] == "+":
            return ["+", myderive(f[1], var), myderive(f[2], var)]
        elif f[0] == "-":
            return ["-", myderive(f[1], var), myderive(f[2], var)]
        elif f[0] == "*":
            return ["+", ["*", myderive(f[1], var), f[2]], ["*", f[1], myderive(f[2], var)]]
        elif f[0] == "/":
            return ["/", ["-", ["*", myderive(f[1],var), f[2]], ["*", f[1], myderive(f[2], var)]], ["*", f[2], f[2]]]

    return 0


print(myderive(1, "x"))  
print(myderive("y", "x"))  
print(myderive("x", "x"))  
print(myderive(["-", 2, "x"], "x"))  
print(myderive(["*", 2, "x"], "x")) 
print(myderive(["*", "x", "x"], "x"))  
print(myderive(["*", "x", "x"], "y"))  
print(myderive(["*",["-","x",1],"x"],"x"))
#print(myderive(["-", "x", 1], "x"))  
print(myderive(["+", "x", "x"], "x"))  
print(myderive(["+", "y", "x"], "x"))  
print(myderive(["/", "x", "y"], "y")) 
