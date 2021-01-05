    def move_forward():
        if front_is_clear():
            move()
        elif wall_in_front():
            turn_left()
            move()
            turn_left()
            turn_left()
            turn_left()
            move()
            turn_left()
            turn_left()
            turn_left()
            move()
            turn_left()


    while not at_goal() :
        move_forward()
    


    def turn_right():
        turn_left()
        turn_left()
        turn_left()

    def jump():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left

    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()
