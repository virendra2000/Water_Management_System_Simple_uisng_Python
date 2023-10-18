tank_size = 500
for i in range(1,tank_size+1):
    print("Asking At Stop",i)
    user_ip = int(input("How Many Litre of Water Do You Want : \n"))
    if(user_ip>tank_size):
        print("Out Of Range")
        print("Remaining Tank Size : ",tank_size)
        if(tank_size==0):
            break
        else:
            user_ip = int(input("Enter in Sufficient Amount From Remaining \n"))
            tank_size = tank_size - user_ip
            print("Remaining Tank Size : ",tank_size)
    else:
        tank_size = tank_size - user_ip
        print("Remaining Tank Size : ",tank_size)
    i=tank_size
