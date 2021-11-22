
while True:
    user_table = int(input("Which multiplication table do you want to see? (1-10). 0 stops program.\n"))
    if user_table == 0:
        break

    else:
        try:
            if 1 < user_table <= 10:
                for i in range(10):
                    i += 1
                    print(f"{user_table} x {i} = {user_table * (i)}")
            else:
                print("Wrong number format.")
                pass
        except:
            print("What?")
