numDict={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',
         6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
         11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
         16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
tenDict={2:'twenty',3:'thirty',4:'forty',5:'fifty',
         6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

def ldouble(num):
    if int(num)<20:
        return(len(numDict[int(num)]))
    else:
        return(len(tenDict[int((num)[0])])+len(numDict[int((num)[1])]))
    
def ltriple(num):
    if len(num)<3:
        return(ldouble(num))
    else:
        if(int(num[1:3])==0):
            adder=7
        else:
            adder=10
        return(adder+len(numDict[int(num[0])])+ldouble(str(int(num[1:3]))))
    
sum=0
for i in range(1,1000):
    sum+=ltriple(str(i))
print(sum+len('onethousand'))