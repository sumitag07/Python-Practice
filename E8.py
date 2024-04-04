while True:
    p1 = input("Enter player 1 entry")
    p2 = input("Enter player 2 entry")
    if p1 == "sissors":
        if p2 =="paper":
            print("player 1 won")
        elif p2 == "rock":
            print("player 2 won")
    if p1 == "paper":
        if p2 =="rock":
            print("player 1 won")
        elif p2 == "sissors":
            print("player 2 won")
    if p1 == "rock":
        if p2 =="sissors":
            print("player 1 won")
        elif p2 == "paper":
            print("player 2 won")
    if p1 == p2:
        print("draw")
    q = input("do you want to play agin? Y/N")
    if q == "N":
        break  
    