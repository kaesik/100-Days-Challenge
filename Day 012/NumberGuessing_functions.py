def game_difficulty():
    function = True
    variable = 0
    while function:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            variable = 10
            function = False
        elif difficulty == "hard":
            variable = 5
            function = False
        else:
            print("Incorrect decision. Please repeat.")
            continue
    return variable
