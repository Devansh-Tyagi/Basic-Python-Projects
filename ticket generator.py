#number of tickets one wants to make for a particular flight.
num=int(input("how many tickets you wanna make"))
base=num+101
lst=[]
i=101#ticket number
airline="AL1"
while int(i)<base:
    source=input("enter source city")
    str2=source[0:3]
    dest=input("enter destination city")
    dest1=dest[0:3]
    #format of ticket in str3 : example- AL1 : Har : Del : 101
    str3=airline+':'+str2+':'+dest1+':'+str(i)
    lst.append(str3)
    i=i+1
print(lst)






