import random
people = {"John":0,
            "Tim":0,
            "Eric":0,
            "Tom":0,
            "James":0,
            "Luke":0,}
def getUser(jo):
    if jo in people:
        go = people.get(str(jo))
        print(f"Hello {jo}")
        return jo
    else:
        print(f"User {jo} is not found!")
def addPoints(po):
    user = getUser(ill)
    people[user] += po
def game():
    li = [1,2,3]
    ro = random.choice(li)
    choice = input("Please choose 1,2, or 3")
    if int(choice) == ro:
        print("Congrats +15 points")
        addPoints(15)
        print(people[ill])
    else:
        print("Sorry wrong awnser.")
ill = input("Enter Username\n")
getUser(ill)
game()
