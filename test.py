unit = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
eleventh ={10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
ten = [{20:"twenty"},{30:"thirty"},{40:"fourty"},{50:"fifty"},{60:"sixty"},{70:"seventy"},{80:"eighty"},{90:"ninety"}]

def hundred(num):
    num = num[:3]
    base = "hundred"
    hundred_  =None;
    Ten_  =None;
    unit_ = None;
    l = len(num )
    if  l ==3: hundred_=unit [num[0]]
    if  (l >=2) and num[1]>0: 
        if num[1] ==1: Ten_ =eleventh[num[1]]
        else: Ten_ =ten[num[0]*10]
    if(l>=1) and num[0]>0:
        unit_ = unit[num][0]

    number  =f"{hundred_ and  base}"



    
        




def thousand

def million

def billion

def zillion