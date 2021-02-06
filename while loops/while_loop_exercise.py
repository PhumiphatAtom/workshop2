i = 2
while i <= 12:
    print("   " + "[", i, "]")
    x = 1
    while x <= 12:
        print(i, "*", x, ":", i * x)
        x += 1
    print("")
    print("---------------" "\n")
    i += 1