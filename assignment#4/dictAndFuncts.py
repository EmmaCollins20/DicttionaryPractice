#Emma Collins       10/30/23
#COM S 127 Section F


#Exercise 1 (1/4)
# a+b+c+d
# a-b+c+d
# a+b-c+d
# a+b+c-d

# a-b-c+d
# a-b+c-d
# a+b-c-d
# a-b-c-d


# a*b+c+d
# a*b+c-d
# a*b-c-d
# a*b-c+d

#a+b*c+d
#a+b*c-d
#a-b*c+d
#a-b*c-d

#a+b+c*d
#a+b-c*d
#a-b+c*d
#a-b-c*d

#a*b*c+d
#a*b*c-d
#a-b*c*d
#a+b*c*d
#a*b+c*d
#a*b-c*d
#a*b*c*d

#Exercise 1 (2/4)

def inputValidInt ()

try:
    Val = int(input("Imput valid imput "))
except Exception as e:
print("ERROR: ivalid imput. Enter a valid imput")

def calcAAA (a,b,c,d):
    return a+b+c+d

def calcAAS (a,b,c,d):
    return a+b+c-d

def calASA (a,b,c,d):
    return a+b-c+d

def calcSAA (a,b,c,d):
    return a-b+c+d


def calcSSA (a,b,c,d):
    return a-b-c+d

def calcSAS (a,b,c,d):
    return a-b+c-d

def calcASS (a,b,c,d):
    return a+b-c-d

def calcSSS (a,b,c,d):
    return a-b-c-d


def calcMAA (a,b,c,d):
    return a*b+c+d

def calcMAS (a,b,c,d):
    return a*b+c-d

def calcMSS (a,b,c,d):
    return a*b-c-d

def calcMSA (a,b,c,d):
    return a*b-c+d


def calcAMA (a,b,c,d):
    return a+b*c+d

def calcAMS (a,b,c,d):
    return a+b*c-d

del calcSMA (a,b,c,d):
    return a-b*c+d

def calcSMS (a,b,c,d):
    return a-b*c-d


def calcAAM (a,b,c,d):
    return a+b+c*d

def calcASM (a,b,c,d):
    return a+b-c*d

def calcSAM (a,b,c,d):
    return a-b+c*d

def calcSSM (a,b,c,d):
    return a-b-c*d


def calcMMA (a,b,c,d):
    return a*b*c+d

def calcMMS (a,b,c,d):
    return a*b*c-d

def calcSMM (a,b,c,d):
    return a-b*c*d

def calcAMM (a,b,c,d):
    return a+b*c*d

def calcMAM (a,b,c,d):
    return a*b+c*d

def calcMSM (a,b,c,d):
    return #a*b-c*d

def calcMMM (a,b,c,d):
    return a*b*c*d


def main ():
    a =inputValidInteger()
    b =inputValidInteger()
    c =inputValidInteger()
    d =inputValidInteger()

    calculations = {}

    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["SAA"] = calcSAA(a,b,c,d)
    calculations["ASA"] = calcASA(a,b,c,d)
    calculations["AAS"] = calcAAS(a,b,c,d)
    
    calculations["SSA"] = calcSSA(a,b,c,d)
    calculations["SAS"] = calcSAS(a,b,c,d)
    calculations["ASS"] = calcASS(a,b,c,d)
    calculations["SSS"] = calcSSS(a,b,c,d)
    
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    calculations["AAA"] = calcAAA(a,b,c,d)
    



