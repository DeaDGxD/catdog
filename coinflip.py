import random
def coinflip(flips):
    running = True
    while running:
        coin = ["heads", "tails"]
        toss = 1
        results = []
        while toss != int(flips):
            result = random.choice(coin)
            results += result
            toss += 1
        heads = results.count("h")
        tails = results.count("t")
        flip = tails > heads
        running = False
        return flip
