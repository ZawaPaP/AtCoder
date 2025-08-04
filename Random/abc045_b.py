Sa = input()
Sb = input()
Sc = input()

turn = "a"

while True:
    if turn == "a":
        if Sa == "":
            print("A")
            break
        turn = Sa[0]
        Sa = Sa[1:]
    elif turn == "b":
        if Sb == "":
            print("B")
            break
        turn = Sb[0]
        Sb = Sb[1:]
    elif turn == "c":
        if Sc == "":
            print("C")
            break
        turn = Sc[0]
        Sc = Sc[1:]
