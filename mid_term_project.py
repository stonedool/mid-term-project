from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

Rat_House_Scene = Scene('집', 'images/Rat_House.jpg')
Map1 = Scene('집 앞', 'images/House_Scene2.jpg')
Rat = Object("images/MainChar1.png")
bed = Object("images/RatBed.png")
Flower_pot = Object("images/Flower_Pot.png")

up = Object('images/Direction/up.png')
left = Object('images/Direction/left.png')
down = Object('images/Direction/down.png')
right = Object('images/Direction/right.png')

Rat.x = 300
Rat.y = 300
Rat.scene = 1
Rat.locate(Rat_House_Scene,Rat.x,Rat.y); Rat.setScale(0.4) 
bed.locate(Rat_House_Scene,800,100)
Flower_pot.locate(Rat_House_Scene,100,100)
up.locate(Rat_House_Scene, 1000,120); up.setScale(0.5)
left.locate(Rat_House_Scene, 930,50); left.setScale(0.5)
down.locate(Rat_House_Scene, 1000,50); down.setScale(0.5)
right.locate(Rat_House_Scene, 1100,50); right.setScale(0.5)




up.show()
left.show()
down.show()
right.show()
Rat.show()
bed.show()
Flower_pot.show()

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
        pot.show() #기존에 토끼가 당근을 줍는 코드입니다. 이번 게임에서는 생쥐가 치즈를 주을때 사용합시다. 

def up_press(x,y,action):
    Rat.y = Rat.y + 30
    if Rat.scene == 1:
        Rat.locate(Rat_House_Scene, Rat.x, Rat.y)
    else:
        Rat.locate(scene2, Rat.x, Rat.y)
    print('up')

def left_press(x,y,action):
    Rat.x = Rat.x - 30
    if Rat.scene == 1:
        Rat.locate(Rat_House_Scene, Rat.x, Rat.y)
    else: 
        Rat.locate(scene2, Rat.x, Rat.y)
    print('left')

def right_press(x,y,action):
    Rat.x = Rat.x + 30
    if Rat.scene == 1:
        Rat.locate(Rat_House_Scene, Rat.x, Rat.y)
    else:
        Rat.locate(scene2, Rat.x, Rat.y)
    print('right')

def down_press(x,y,action):
    Rat.y = Rat.y - 30
    if Rat.scene == 1:
        Rat.locate(Rat_House_Scene, Rat.x, Rat.y)
    else:
        rabbit.locate(scene2, Rat.x, Rat.y)
    print('down')

#위 네가지 코드가 캐릭터의 이동을 결정합니다.

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
#rabbit.onMouseAction = bunny_get_carrot
#pot.onMouseAction = pot_press
#quest.onMouseAction = quest_click
#intro.onMouseAction = intro_click
#gg.onMouseAction = GG_click


startGame(Rat_House_Scene)
