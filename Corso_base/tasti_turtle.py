import turtle, keyboard

t=turtle.Turtle()

'''
    enter
    freccia su
    freccia giù
    freccia destra
    freccia sinistra
    space
    esc
'''


while True:
    key = keyboard.read_key() 
    if(key=='esc'):
        turtle.bye()
        quit()
    elif(key=='freccia destra'):
        t.forward(10)
    elif(key=='freccia sinistra'):
        t.backward(10)
