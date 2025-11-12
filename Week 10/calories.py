def main():
    food0 = {{"almond milk": 30, "skim": 45},
    {"sour cream, light": 16, "plain, low-fat": 77},
    {"egg": 75, "Egg white": 16},
    {"cream cheese": 51, "american pasteurized": 79},
    {"peanuts, roasted": 170, "cashews, dry roasted": 163},
    {"lentils,boiled": 115, "edamame, boiled": 127},
    {"catfish, baked": 111, "swai, baked": 89},
    {"celery": 1, "corn": 59},
    {"pears": 20, "kiwi": 0},
    {"ranch": 73, "ranch, fat free": 17}}
        
while True:
    food1 = input("Type the name of a food : ")
    food2 = input("Type the name of another food : ")
    input("press enter")
    if (food1, food2):
        print("Number of calories of the two foods combined: ", {food0 + food0})
    break

else:
    print("NO")
main()