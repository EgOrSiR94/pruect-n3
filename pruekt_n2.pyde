
def setup():
    size(700,700)
    background(255, 248, 220)
    textSize(15)
def draw():
    fill(255)
def keyPressed():
    clear()
    fill(0)
    background(255, 248, 220)
    push()

    line(500,0,500,500)
    line(500,1000,500,500)
    line(40000,0,500,500)
    pop()
    push()
    if keyPressed:
        if key == ENTER:
            
            text(u"Привет",10,50)
            fill(0)


    else:
        fill(255)

    pop()
    push()
    if keyPressed:
        if key == DELETE:
            fill(0)

    else:
        fill(255)

    text(u"НЕГР",70,50)
    pop()
