foodi = [
    {"almond milk": 30, "skim": 45},
    {"sour cream, light": 16, "plain, low-fat": 77},
    {"egg": 75, "egg white": 16},
    {"cream cheese": 51, "american pasteurized": 79},
    {"peanuts, roasted": 170, "cashews, dry roasted": 163},
    {"lentils, boiled": 115, "edamame, boiled": 127},
    {"catfish, baked": 111, "swai, baked": 89},
    {"celery": 1, "corn": 59},
    {"pears": 20, "kiwi": 0},
    {"ranch": 73, "ranch, fat free": 17}
]
        
food1 = input("Type the name of a food : ").lower()
food2 = input("Type the name of another food : ").lower()

food3 = 0 
for xd in foodi:
    if food1 in xd:
        food3 += xd[food1]
    if food2 in xd:
        food3 += xd[food2]
print(f"Number of calories of the two foods combined: {food3}")
