import sys

def timeConversion(s):
    # Complete this function
    x=int(s[0]+s[1]) 
    if "A" in s :
        if x==12 :
            s = s.replace(s[0]+s[1],"00")
        s = s.replace("AM","")   
    
    else :
        if  x<12  :
            x=x+12
            k=""
            k=k+str(x)
            s = s.replace(s[0]+s[1],str(x))
        s = s.replace("PM","")
            
    
    print s

s = raw_input().strip()
result = timeConversion(s)
#print(result)
