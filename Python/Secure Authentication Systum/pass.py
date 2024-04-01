def check(uname,pass1,pass2,pass3,passw):
    if(len(passw)>=10):
        if(countu(passw)>=2):
            if(countl(passw)>=2):
                if(digit(passw)>=2):
                    if(special(passw)>=2):
                        if(rep(passw)):
                            if(passw != pass1 and passw != pass2 and passw != pass3):
                                print(uname , "  has successfully changed his password !!")
                        
def rep(passw):
    count=0
    for i in range(len(passw)):
        for j in range(len(passw)):
            if(passw[i]==passw[j]):
                count+=1
    
    if(count>3):
        cond=True
    else:
        cond=False
    return cond

def special(passw):
    cs=0
    for i in range(len(passw)):
        if(passw[i] in "!@#$%^&*"):
            cs+=1
    return cs

def digit(passw):
    cd=0
    for i in range(len(passw)):
        if(passw[i].isdigit()):
            cd+=1
    return cd

def countl(passw):
    cl=0
    for i in range(len(passw)):
        if(passw[i].islower()):
            cl+=1
    return cl

def countu(passw):
    cu=0
    for i in range(len(passw)):
        if(passw[i].isupper()):
            cu+=1
    return cu
            
uname=str(input("Enter your name : "))
pass1=str(input("Enter your 1st password : "))
pass2=str(input("Enter your 2nd password : "))
pass3=str(input("Enter your 3rd password : "))
passw=str(input("Enter your new password : "))

check(uname,pass1,pass2,pass3,passw)