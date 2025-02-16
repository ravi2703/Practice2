def turn_right():
    turn_left()
    while front_is_clear:
      move()
def jump():
    turn_left()
  
    while front_is_clear:
      move()
      
      if wall_in_front():
        turn_left()
      if front_is_clear():
        move()
        if wall_in_front():
            turn_right()
            move()     
number_hurdles = 10
while number_hurdles > 0:
    number_hurdles -= 1
    move()
    while wall_in_front():
      jump()
     
