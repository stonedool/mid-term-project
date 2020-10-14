from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)
scene1 = Scene('당근밭', 'images/scene.jpg')
scene2 = Scene('토끼집', 'images/scene2.png')

intro = Object('images/intro.png')
quest = Object('images/quest.png')
rabbit = Object('images/bunnybunny.png')
carrot1 = Object('images/carrot.png')
carrot2 = Object('images/carrot.png')
carrot3 = Object('images/carrot.png')
pot = Object('images/pot.png')
fullpot = Object('images/fullpot.png')
gg = Object('images/GG.png')
up = Object('images/up.png')
left = Object('images/left.png')
down = Object('images/down.png')
right = Object('images/right.png')

rabbit.carrotinventory = 0
rabbit.x = 100
rabbit.y = 100
rabbit.scene = 1

up.locate(scene1, 1000,120)
left.locate(scene1, 930,50)
down.locate(scene1, 1000,50)
right.locate(scene1, 1100,50)
rabbit.locate(scene1, rabbit.x,rabbit.y)
carrot1.locate(scene1, 400, 400)
carrot2.locate(scene1, 1000, 500)
carrot3.locate(scene1, 600, 100)
quest.locate(scene1, 620, 650)
intro.locate(scene1, 10,0)
pot.locate(scene2, 1060, 255)
gg.locate(scene2,0,0)

up.setScale(0.5)
left.setScale(0.5)
down.setScale(0.5)
right.setScale(0.5)
rabbit.setScale(0.5)
carrot1.setScale(0.1)
carrot2.setScale(0.1)
carrot3.setScale(0.1)

up.show()
left.show()
down.show()
right.show()
carrot1.show()
carrot2.show()
carrot3.show()
rabbit.show()
quest.show()




def bunny_get_carrot(x,y,action):
    if(rabbit.x > 340 and rabbit.y >350 and rabbit.x < 450 and rabbit.y <450):# +-50-60정도씩 하면 괜찮은듯...
        rabbit.carrotinventory = rabbit.carrotinventory+1
        carrot1.hide()
    if(rabbit.x > 940 and rabbit.y >450 and rabbit.x < 1050 and rabbit.y <550):
        rabbit.carrotinventory = rabbit.carrotinventory+1
        carrot2.hide()
    if(rabbit.x > 540 and rabbit.y >50 and rabbit.x < 650 and rabbit.y <150):
        rabbit.carrotinventory = rabbit.carrotinventory+16
        carrot3.hide()
    print('carrot' , rabbit.x , rabbit. y)
    if rabbit.x > 1050 and rabbit.x < 1190 and rabbit.y >420 and rabbit.y < 560 and rabbit.carrotinventory > 1: # scene2
        print("scene2")
        scene2.enter()
        rabbit.x = 50
        rabbit.y = 600
        rabbit.scene = 2
        rabbit.locate(scene2, rabbit.x, rabbit.y)
        up.locate(scene2, 1000,120)
        left.locate(scene2, 930,50)
        down.locate(scene2, 1000,50)
        right.locate(scene2, 1100,50)
        pot.show()

def up_press(x,y,action):
    rabbit.y = rabbit.y + 30
    if rabbit.scene == 1:
        rabbit.locate(scene1, rabbit.x, rabbit.y)
    else:
        rabbit.locate(scene2, rabbit.x, rabbit.y)
    print('up')

def left_press(x,y,action):
    rabbit.x = rabbit.x - 30
    if rabbit.scene == 1:
        rabbit.locate(scene1, rabbit.x, rabbit.y)
    else: 
        rabbit.locate(scene2, rabbit.x, rabbit.y)
    print('left')

def right_press(x,y,action):
    rabbit.x = rabbit.x + 30
    if rabbit.scene == 1:
        rabbit.locate(scene1, rabbit.x, rabbit.y)
    else:
        rabbit.locate(scene2, rabbit.x, rabbit.y)
    print('right')

def down_press(x,y,action):
    rabbit.y = rabbit.y - 30
    if rabbit.scene == 1:
        rabbit.locate(scene1, rabbit.x, rabbit.y)
    else:
        rabbit.locate(scene2, rabbit.x, rabbit.y)
    print('down')

def pot_press(x,y,action):
    if rabbit.x > 1000 and rabbit.y > 200 and rabbit.x < 1200 and rabbit.y < 350:
        pot.setImage('images/fullpot.png')
        print("endgame")
        showMessage("토끼는 맛있게 밥을 먹었습니다")
        gg.show()

def quest_click(x,y,action):
    intro.show()

def intro_click(x,y,action):
    intro.hide()

def GG_click(x,y,action):
    endGame()

up.onMouseAction = up_press
left.onMouseAction = left_press
down.onMouseAction = down_press
right.onMouseAction = right_press
rabbit.onMouseAction = bunny_get_carrot
pot.onMouseAction = pot_press
quest.onMouseAction = quest_click
intro.onMouseAction = intro_click
gg.onMouseAction = GG_click


startGame(scene1)
