import random
#top 200 first names both masculine and feminine
name = ["Mary","Patricia","Jennifer","Linda","Elizabeth","Barbara","Susan","Jessica","Sarah","Karen","Nancy","Margaret","Lisa","Betty","Dorothy","Sandra","Ashley","Kimberly","Donna","Emily","Michelle","Carol","Amanda","Melissa","Deborah","Stephanie","Rebecca","Laura","Sharon","Cynthia","Kathleen","Helen","Amy","Shirley","Angela","Anna","Brenda","Pamela","Nicole","Ruth","Katherine","Samantha","Christine","Emma","Catherine","Debra","Virginia","Rachel","Carolyn","Janet","Maria","Heather","Diane","Julie","Joyce","Victoria","Kelly","Christina","Joan","Evelyn","Lauren","Judith","Olivia","Frances","Martha","Cheryl","Megan","Andrea","Hannah","Jacqueline","Ann","Jean","Alice","Kathryn","Gloria","Teresa","Doris","Sara","Janice","Julia","Marie","Madison","Grace","Judy","Theresa","Beverly","Denise","Marilyn","Amber","Danielle","Abigail","Brittany","Rose","Diana","Natalie","Sophia","Alexis","Lori","Kayla","Jane","James","John","Robert","Michael","William","David","Richard","Joseph","Thomas","Charles","Christopher","Daniel","Matthew","Anthony","Donald","Mark","Paul","Steven","Andrew","Kenneth","Joshua","George","Kevin","Brian","Edward","Ronald","Timothy","Jason","Jeffrey","Ryan","Jacob","Gary","Nicholas","Eric","Stephen","Jonathan","Larry","Justin","Scott","Brandon","Frank","Benjamin","Gregory","Samuel","Raymond","Patrick","Alexander","Jack","Dennis","Jerry","Tyler","Aaron","Jose","Henry","Douglas","Adam","Peter","Nathan","Zachary","Walter","Kyle","Harold","Carl","Jeremy","Keith","Roger","Gerald","Ethan","Arthur","Terry","Christian","Sean","Lawrence","Austin","Joe","Noah","Jesse","Albert","Bryan","Billy","Bruce","Willie","Jordan","Dylan","Alan","Ralph","Gabriel","Roy","Juan","Wayne","Eugene","Logan","Randy","Louis","Russell","Vincent","Philip","Bobby","Johnny","Bradley"]
#top 100 Last names
lastName = ["Smith","Johnson","Williams","Jones","Brown","Davis","Miller","Wilson","Moore","Taylor","Anderson","Thomas","Jackson","White","Harris","Martin","Thompson","Garcia","Martinez","Robinson","Clark","Rodriguez","Lewis","Lee","Walker","Hall","Allen","Young","Hernandez","King","Wright","Lopez","Hill","Scott","Green","Adams","Baker","Gonzalez","Nelson","Carter","Mitchell","Perez","Roberts","Turner","Phillips","Campbell","Parker","Evans","Edwards","Collins","Stewart","Sanchez","Morris","Rogers","Reed","Cook","Morgan","Bell","Murphy","Bailey","Rivera","Cooper","Richardson","Cox","Howard","Ward","Torres","Peterson","Gray","Ramirez","James","Watson","Brooks","Kelly","Sanders","Price","Bennett","Wood","Barnes","Ross","Henderson","Coleman","Jenkins","Perry","Powell","Long","Patterson","Hughes","Flores","Washington","Butler","Simmons","Foster","Gonzales","Bryan","Alexander","Russell","Griffin","Diaz","Hayes"]
cat = True
names = []
trash = 0
while cat:
    if trash < 300000:
        ran = random.choice(name)
        ran2 = random.choice(lastName)
        namey = f"{ran} {ran2}"
        cat += 1
        car = namey
        if str(car) not in names:
            names.append(str(car))
            trash = 0
        else:
            trash += 1
    else:
        break
name = set(names)
print(len(names))
print(len(set(names)))
