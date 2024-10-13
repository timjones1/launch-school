interning = True

a = 0;
b = 0;

while interning:
    a -=1 
    b -=1
    
    if id(a) != id(b):
        print(f"{a = }, {id(a)=}, {b = }, {id(b) = }")
        interning = False
    
    if b <-500: 
        print("all 500 negative integers are interned")
        break

