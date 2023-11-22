num = int(input())

if (num%2)==0:
    nl = int((num-2)/2)
    center = str(nl*"#"+(str(0))*2+nl*"#")
    l = str(num*"#")

    print(str(str(l+"\n")*nl)+center+"\n"+center+"\n"+str(str(l+"\n")*nl))

else:
    nl = int(num//2)
    center = str(nl*"#"+str(0)+nl*"#")
    l = str(num*"#")

    print(str(str(l+"\n")*nl)+center+"\n"+str(str(l+"\n")*nl))
