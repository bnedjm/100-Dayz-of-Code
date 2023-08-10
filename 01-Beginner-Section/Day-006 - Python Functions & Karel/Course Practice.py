#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_3():
    move()
    move()
    move()
    
def square():
    turn_left()
    move_3()
    turn_right()
    move_3()
    turn_right()
    move_3()
    turn_right()
    move_3()
    
square()
