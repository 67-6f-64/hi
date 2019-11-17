fin=open("logins.txt","r")
email=open("email.txt","a")
referal=open("referal.txt","a")
big_string = fin.read()
fin.close()
entries=big_string.split('\n')

def mail():
    for i in range(len(entries)):
        # num=(2*i)
        # e=entries[num]
        # r=entries[(1+num)]
        if i%2==0:
            e=entries[i]
            email.write(e+"\n")
    print email
def ref():
    for i in range(len(entries)):
        # num=(2*i)
        # e=entries[num]
        # r=entries[(1+num)]
        if i%2==1:
            r=entries[i]
            referal.write(r+"\n")
    print referal

mail()
ref()