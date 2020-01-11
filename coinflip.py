import random, sys
while True:
    coin = ["heads", "tails"]
    toss = 1
    flips = input("How many times do you want to flip?" + "\n")
    results = []
    try:
        while toss != int(flips):
            result = random.choice(coin)
            results += result
            toss += 1
            print(result)
    except ValueError:
        if flips == "":
            print("You need to enter a value.")
            continue
        else:
            print("Only numbers will work!")
            continue
    heads = results.count("h")
    tails = results.count("t")
    flip = tails > heads
    if flip == True:
        print("Tails wins!")
    else:
        print("Heads wins!")
    cat = input("Play agian? y/n" + "\n")
    if cat == "y":
        continue
    else:
        break
