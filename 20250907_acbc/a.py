S = input()

world = int(S[0])
stage = int(S[2])

if stage < 8:
    print(str(world)+'-'+str(stage+1))
    exit()
elif world < 8:
    print(str(world+1)+'-'+str(1))
    exit()
