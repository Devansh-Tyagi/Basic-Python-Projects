b={"tl":" ","tm":" ","tr":" ","ml":" ","mm":" ","mr":" ","bl":" ","bm":" ","br":" "}
def printb(b):
    print(b["tl"], "|", b["tm"], "|", b["tr"])
    print("--+---+--")
    print(b["ml"], "|", b["mm"], "|", b["mr"])
    print("--+---+--")
    print(b["bl"], "|", b["bm"], "|", b["br"])
turn="x"
lst=[]
for i in range(0,9):
    printb(b)
    print("turn for "+turn+",move where?")
    move=input()
    if move not in lst:
        b[move] = turn
        lst.append(move)
        if b["tl"] == b["tm"] == b["tr"] != " ":
            printb(b)
            print('winner is : ', turn)
            break
        elif b["ml"] == b["mm"] == b["mr"] != " ":
            printb(b)
            print('winner is : ', turn)
            break
        elif b["bl"] == b["bm"] == b["br"] != " ":
            printb(b)
            print('winner is : ', turn)
            break
        elif b["tl"] == b["ml"] == b["bl"] != " ":
            printb(b)
            print('winner is : ', turn)
            break
        elif b["tm"] == b["mm"] == b["bm"] != " ":
            printb(b)
            print('winner is : ', turn)
            break
        elif b["tr"] == b["mr"] == b["br"] != " ":
            printb(b)
            print('winner is : ', turn)
            break
        elif b["tl"] == b["mm"] == b["br"] != " ":
            printb(b)
            print('winner is : ', turn)
            break
        elif b["tr"] == b["mm"] == b["bl"] != " ":
            printb(b)
            print('winner is : ', turn)
            break
        if turn == "x":
            turn = "o"
        else:
            turn = "x"
    else:
        print("please choose a non occupied position")
else:
    print("DRAW BETWEEN X AND O")





    




