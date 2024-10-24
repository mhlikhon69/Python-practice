class R:
    varR = "Welcome R"
    
    
class B:
    varB = "Welcome B"
    
    
class C(R,B):
    varC = "Welcome C"        
    
    
    
c1 = C()

print(c1.varC)   
print(c1.varB)   
print(c1.varR)    
print("Repsol")    