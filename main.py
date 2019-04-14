game_over = False
game_setup_complete = False
turn_count = 0
debug_mode = True


def debug_print(message):
    if(debug_mode==True):
        print(message)


def player_turn():
    # This is essentially the game loop
    # since this is a turn based game. It checks
    # for game setup, defeat and victory.

    # Check game setup
    global game_setup_complete
    if(game_setup_complete == False):
        print("player_turn determined game_setup needed")
        game_setup()
    
    # Check turn count
    global turn_count
    turn_count += 1
    debug_print(turn_count)
    return turn_count


def game_setup():
    debug_print("game_setup running")
    global game_setup_complete
    game_setup_complete = True
    return game_setup_complete


while(game_over == False):
    print("Next turn?")
    action_command = input()
    player_turn()