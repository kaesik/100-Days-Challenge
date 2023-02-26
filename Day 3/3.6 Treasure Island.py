print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
answer1 = input("You are in the forest. You see two path, left and right. Where do you go?\n"
                "left or right: ")
if answer1 == "left":
    answer2 = input("Your path is crossed by the lake. What are you doing?\n"
                    "swim, pass or look around: ")
    if answer2 == "look around" or "look":
        answer3 = input(
            "You found a bridge. When you pass it you see the tower with three doors. Which one do you open?\n"
            "red, blue or yellow: ")
        if answer3 == "yellow":
            print("Congratulations! You found the chest. When you open the chest you see the letter.\n"
                  "In the letter is:\n"
                  "'The real treasure is Harnaś'")
        else:
            print("There is a trapdoor behind these door. You died.\n"
                  "Game Over.")
    else:
        print("You tried to cross the river but it was too strong. Your drown.\n"
              "Game Over.")
else:
    print("Unfortunately, at the end of the path there is a cliff. And you fell from him.\n"
          "Game Over.")