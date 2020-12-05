from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

Rat_House_Scene = Scene('집', 'images/Rat_House.jpg')
scene2 = Scene('집 앞', 'images/House_Scene2.jpg')
Rat = Object("images/MainChar1.png")
bed = Object("images/RatBed.png")
Flower_pot = Object("images/Flower_Pot.png")
Map_1 = Object("images/Map.png")
Mini_Map = Object("images/Mini_Map.png")
Desk = Object("images/Desk.png")


up = Object('images/Direction/up.png')
left = Object('images/Direction/left.png')
down = Object('images/Direction/down.png')
right = Object('images/Direction/right.png')

Rat.x = 950
Rat.y = 300
Rat.scene = 1
Rat.scene_STAY = True

bed.locate(Rat_House_Scene,800,100)
Flower_pot.locate(Rat_House_Scene,100,100)
Map_1.locate(Rat_House_Scene,10,10)
up.locate(Rat_House_Scene, 1000,120); up.setScale(0.5)
left.locate(Rat_House_Scene, 930,50); left.setScale(0.5)
down.locate(Rat_House_Scene, 1000,50); down.setScale(0.5)
right.locate(Rat_House_Scene, 1100,50); right.setScale(0.5)
Mini_Map.locate(Rat_House_Scene, 1100, 600); Mini_Map.setScale(0.5)
Desk.locate(Rat_House_Scene, 400, 200)
Rat.locate(Rat_House_Scene,Rat.x,Rat.y); Rat.setScale(0.4) 

Desk.show()
bed.show()
Flower_pot.show()
Mini_Map.show()
Rat.show()
up.show()
left.show()
down.show()
right.show()


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
    elif Rat.scene == 2:
        Rat.locate(scene2, Rat.x, Rat.y)
    NextScene()
    print('up')

def left_press(x,y,action):
    Rat.x = Rat.x - 30
    if Rat.scene == 1:
        Rat.locate(Rat_House_Scene, Rat.x, Rat.y)
    elif Rat.scene == 2:
        Rat.locate(scene2, Rat.x, Rat.y)
    NextScene()
    print('left')

def right_press(x,y,action):
    Rat.x = Rat.x + 30
    if Rat.scene == 1:
        Rat.locate(Rat_House_Scene, Rat.x, Rat.y)
    elif Rat.scene == 2:
        Rat.locate(scene2, Rat.x, Rat.y)
    NextScene()
    print('right')

def down_press(x,y,action):
    Rat.y = Rat.y - 30
    if Rat.scene == 1:
        Rat.locate(Rat_House_Scene, Rat.x, Rat.y)
    elif Rat.scene == 2:
        Rat.locate(scene2, Rat.x, Rat.y)
    NextScene()
    print('down')

#위 네가지 코드가 캐릭터의 이동을 결정합니다.
#else 케이스는 손을 좀 봐야 할것 같습니다. 
# next scene을 위한 함수가 필요합니다. 

def NextScene(): # 씬체인지 기능입니다. 
    if Rat.scene == 1:
        if Rat.x >= 150 and Rat.x<=240:
            if Rat.y >= 300 and Rat.y <= 450:
                scene2.enter() #특정 위치에 도달하면 다음 씬으로 이동시킵니다. 
                Rat.scene = 2
                Rat.x = 700 ; Rat.y = 440; #해당 씬의서의 쥐의 위치를 적당한 위치에 위치하게 합니다.
                Rat.locate(scene2, Rat.x, Rat.y)
                Switch_ReLocate(scene2) # 방향키가 해당 씬에도 나타날수 있게 하는 함수입니다. 
                pass
    elif Rat.scene == 2:
        pass
def Switch_ReLocate(SceneName): # 방향키가 해당 씬에도 나타날수 있게 하는 함수입니다. 
    up.locate(SceneName, 1000,120);
    left.locate(SceneName, 930,50);
    down.locate(SceneName, 1000,50);
    right.locate(SceneName, 1100,50);

def Mini_Map_click(x,y,action): #화면 우측 위에 나오는 지도를 띄우기 위한 함수입니다. 클릭하면 지도가 열립니다. 
    Map_1.show()

def Map_1_click(x,y,action): #지도를닫기 위한 함수입니다. 클릭하면 지도가 닫힙니다. 
    Map_1.hide()

def GG_click(x,y,action): #미구현 기능입니다. 게임이 끝났다는것을 알리기 위한 기능입니다. 
    endGame()

up.onMouseAction = up_press
left.onMouseAction = left_press
down.onMouseAction = down_press
right.onMouseAction = right_press
#rabbit.onMouseAction = bunny_get_carrot
Mini_Map.onMouseAction = Mini_Map_click
Map_1.onMouseAction = Map_1_click
#gg.onMouseAction = GG_click


startGame(Rat_House_Scene)
