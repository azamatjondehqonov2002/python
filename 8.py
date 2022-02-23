from email.errors import MisplacedEnvelopeHeaderDefect

satr=""
def yozish(a):
    x=a//100
    y= a//10%10
    z=a%10
    yoz=""
    if x==1:
        yoz+="bir yuz "
    elif x==2:
        yoz+="ikki yuz "
    elif x==3:
        yoz+="uch yuz "
    elif x==4:
        yoz+="to'rt yuz "
    elif x==5:
        yoz+="besh yuz "
    elif x==6:
        yoz+="olti yuz "
    elif x==7:
        yoz+="yetti yuz "
    elif x==8:
        yoz+="sakkiz yuz "
    elif x==9:
        yoz+="to'qqiz yuz "
    if y==1:
        yoz+="o'n "
    elif y==2:
        yoz+="yigirma "
    elif y==3:
        yoz+="o'ttiz "
    elif y==4:
        yoz+="qirq "
    elif y==5:
        yoz+="ellik "
    elif y==6:
        yoz+="oltmish "
    elif y==7:
        yoz+="yetmish "
    elif y==8:
        yoz+="sakson "
    elif y==9:
        yoz+="to'qson "
    if z==1:
        yoz+="bir "
    elif z==2:
        yoz+="ikki "
    elif z==3:
        yoz+="uch "
    elif z==4:
        yoz+="to'rt "
    elif z==5:
        yoz+="besh "
    elif z==6:
        yoz+="olti "
    elif z==7:
        yoz+="yetti "
    elif z==8:
        yoz+="sakkiz "
    elif z==9:
        yoz+="to'qqiz "
    return yoz
    
    
s=int(input())
bir = s%1000
ming = s//1000%1000
million = s//1000000%1000
satr = ""
if million > 0:
    satr+=yozish(million) + "million "
if ming>0:
    satr+=yozish(ming)+"ming "
if bir>0:
    satr+=yozish(bir)
print(satr)