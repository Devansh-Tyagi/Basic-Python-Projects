#A dictionary predefined to get the correct flight number when user inputs source and destination.
dic={"AL1":"HARIDWAR TO DELHI","AL2":"DELHI TO LUCKNOW","BA1":"PATNA TO MUMBAI","DA1":"MUMBAI TO BANGLORE","JA4":"BANGLORE TO SHRIDI","KA2":"MUZZAFARNAGAR TO MEERUT"}
#number of tickets one wants to make for a particular flight.
num=int(input("how many tickets you wanna make"))
base=num+101
lst=[]
J=101#ticket number
while J<base:
    source=input("enter source city")
    str2=source[0:3]
    dest=input("enter destination city")
    dest1=dest[0:3]
    for i in dic:
        st=dic[i]
        ls=st.split()
        if source in ls and dest in ls:
            airline=i
        else:
            continue
    #format of ticket in str3 : example- AL1 : Har : Del : 101
    str3=airline+':'+str2+':'+dest1+':'+str(J)
    lst.append(str3)
    J=J+1
print(lst)






