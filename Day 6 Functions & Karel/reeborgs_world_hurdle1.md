https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

    def hurdle():
        move()
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

    hurdle()
    hurdle()
    hurdle()
    hurdle()
    hurdle()
    hurdle()



    def hurdle():
        move()
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

    # From 0 to 6 but not including 6
    # 0 1 2 3 4 5 
    for step in range(6):
        hurdle()
![](https://github.com/JeffLoboz/100DaysOfPython/blob/main/images/hurdle1.png)




    def hurdle():
        move()
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

    # FOR LOOP VERSION

    # From 0 to 6 but not including 6
    # 0 1 2 3 4 5 
    #for step in range(6):
    #    hurdle()


    # WHILE LOOP VERSION
    number_of_hurdles = 6
    while number_of_hurdles > 0:
        hurdle()
        number_of_hurdles -= 1
        print(number_of_hurdles)
