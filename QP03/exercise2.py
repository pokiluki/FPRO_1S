hour = int(input())
min = int(input())
period = "am"


if hour not in range(0,24) or min not in range(0,60):
    print("INVALID DATE FORMAT")

elif hour == 0:
    if min != 0:
        print(str(12)+":"+str(min).zfill(2)+" "+period)
    else:
        print(str(12)+" "+period)

elif hour == 12:
        if min != 0:
            print(str(12)+":"+str(min).zfill(2)+" pm")
        else:
            print(str(12)+" pm")  

elif hour >= 12:
    period = "pm"  

    if min != 0:
        print(str(hour-12)+":"+str(min).zfill(2)+" "+period)
    else:
        print(str(hour-12)+" "+period)

else:
    if min != 0:
        print(str(hour)+":"+str(min).zfill(2)+" "+period)
    else:
        print(str(hour)+" "+period)

