from bangtal import *
from Othello import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

#Scene 
Rat_House_Scene = Scene('생쥐의 집', 'images/Rat_House.jpg')
scene2 = Scene('집 앞', 'images/House_Scene2.jpg')
scene3 = Scene('주방 앞', 'images/House_Scene3.jpg')
scene4 = Scene('주방', 'images/House_Scene4.jpg')

#Object
Rat = Object("images/MainChar1.png")
Cat = Object("images/Cat.png")
bed = Object("images/RatBed.png")
Flower_pot = Object("images/Flower_Pot.png")
Flower_Pot_2 = Object("images/Flower_Pot.png")
Flower_Pot_3 = Object("images/Flower_Pot.png")
Map_1 = Object("images/Map.png")
Mini_Map = Object("images/Mini_Map.png")
Desk = Object("images/Desk.png")
GG = Object("GG.png")

#trap (in Scene3)
Trap_1 = Object("images/Trap.png")
Trap_2 = Object("images/Trap.png")
Trap_3 = Object("images/Trap.png")
Trap_4 = Object("images/Trap.png")
Trap_5 = Object("images/Trap.png")

#direction switch
up = Object('images/Direction/up.png')
left = Object('images/Direction/left.png')
down = Object('images/Direction/down.png')
right = Object('images/Direction/right.png')

#Rat Variables
Rat.x = 950
Rat.y = 300
Rat.scene = 1
Rat.scene_STAY = False

#Scene1 
Desk.locate(Rat_House_Scene, 400, 200)
bed.locate(Rat_House_Scene,800,100)
Flower_pot.locate(Rat_House_Scene,100,100)
Map_1.locate(Rat_House_Scene,10,10)

#기능이 있는 객체 
Rat.locate(Rat_House_Scene,Rat.x,Rat.y); Rat.setScale(0.4) 
up.locate(Rat_House_Scene, 1000,120); up.setScale(0.5)
left.locate(Rat_House_Scene, 930,50); left.setScale(0.5)
down.locate(Rat_House_Scene, 1000,50); down.setScale(0.5)
right.locate(Rat_House_Scene, 1100,50); right.setScale(0.5)
Mini_Map.locate(Rat_House_Scene, 1100, 600); Mini_Map.setScale(0.5)

#Scene2 관련 오브젝트 
Flower_Pot_2.locate(scene2,1000,200) #때로는 화분 하나가 집의 분위기를 살리는 법이죠... 

#Scene3 관련 오브젝트 
trapSize_x = 137
trapSize_y = 90

Trap_1.locate(scene3,500,100)
Trap_2.locate(scene3,700,400)
Trap_3.locate(scene3,600,450)
Trap_4.locate(scene3,100,500)
Trap_5.locate(scene3,150,400)
Flower_Pot_3.locate(scene3,100,100); Flower_Pot_3.setScale(0.8);
GG.locate(scene3, 250, 100)

#Scene4 관련 
Cat.locate(scene4,600,100)


#object show
Cat.show()
Desk.show()
bed.show()
Mini_Map.show()
Flower_pot.show()
Flower_Pot_2.show()
Flower_Pot_3.show()
Rat.show()
up.show()
left.show()
down.show()
right.show()
Trap_1.show()
Trap_2.show()
Trap_3.show()
Trap_4.show()
Trap_5.show()
#시간이 얼마 없습니다. 이악물고 하겠습니다. 



def up_press(x,y,action): #up /down /left/ right press 함수는 캐릭터의 이동을 결정하는 함수입니다.
    Rat.y = Rat.y + 30
    if Rat.scene == 1:
        Rat.locate(Rat_House_Scene, Rat.x, Rat.y)
    elif Rat.scene == 2:
        Rat.locate(scene2, Rat.x, Rat.y)
    elif Rat.scene ==3:
        Rat.locate(scene3, Rat.x, Rat.y)
    NextScene()
    On_Trap()
    print('up')
    debug()

def left_press(x,y,action):
    Rat.x = Rat.x - 30
    if Rat.scene == 1:
        Rat.locate(Rat_House_Scene, Rat.x, Rat.y)
    elif Rat.scene == 2:
        Rat.locate(scene2, Rat.x, Rat.y)
    elif Rat.scene ==3:
        Rat.locate(scene3, Rat.x, Rat.y)
    NextScene()
    On_Trap()
    print('left')
    debug()

def right_press(x,y,action):
    Rat.x = Rat.x + 30
    if Rat.scene == 1:
        Rat.locate(Rat_House_Scene, Rat.x, Rat.y)
    elif Rat.scene == 2:
        Rat.locate(scene2, Rat.x, Rat.y)
    elif Rat.scene ==3:
        Rat.locate(scene3, Rat.x, Rat.y)
    NextScene()
    On_Trap()
    print('right')
    debug()

def down_press(x,y,action):
    Rat.y = Rat.y - 30
    if Rat.scene == 1:
        Rat.locate(Rat_House_Scene, Rat.x, Rat.y)
    elif Rat.scene == 2:
        Rat.locate(scene2, Rat.x, Rat.y)
    elif Rat.scene ==3:
        Rat.locate(scene3, Rat.x, Rat.y)
    NextScene()
    On_Trap()
    print('down')
    debug()

#위 네가지 코드가 캐릭터의 이동을 결정합니다.
#각 씬별 elif  케이스는 손을 좀 봐야 할것 같습니다. 


def NextScene(): # 씬체인지 기능입니다. 
    if Rat.scene == 1:
        if Rat.scene_STAY == False:
            if Rat.x >= 150 and Rat.x<=240:
                if Rat.y >= 300 and Rat.y <= 450:
                    scene2.enter() #특정 위치에 도달하면 다음 씬으로 이동시킵니다. 
                    Rat.scene = 2
                    Rat.x = 700 ; Rat.y = 440; #해당 씬의서의 생쥐의 위치를 적당한 위치에 위치하게 합니다.
                    Rat.locate(scene2, Rat.x, Rat.y)
                    Switch_ReLocate(scene2) # 방향키가 해당 씬에도 나타날수 있게 하는 함수입니다. 
                    Rat.scene_STAY = True
                    Mini_Map.locate(scene2, 1100, 600);
                    Map_1.locate(scene2,200,100)
        elif Rat.scene_STAY == True:
            Scene_Stay(150,240,300,450) #씬 체인지 이후에 stay중인지 이동하여 해당 구간을 벗어났는지를 판별합니다. 

    elif Rat.scene == 2:
        if Rat.scene_STAY == False: 
            #false 는 생쥐가 기존 씬에서 넘어온 후 다시 원래의 씬으로 돌아가지 않게 하는 변수입니다.
            #해당 구간에 있을때는 true, 나가면 false로 설정합니다. 

            if Rat.x >= 610 and Rat.x <= 760: # scene1 진입코드 
                if Rat.y >= 420 and Rat.y <= 520:
                    Rat_House_Scene.enter()
                    Rat.scene = 1
                    Rat.x = 200; Rat.y = 375;
                    Rat.locate(Rat_House_Scene, Rat.x, Rat.y)
                    Switch_ReLocate(Rat_House_Scene)
                    Rat.scene_STAY = True
                    Mini_Map.locate(Rat_House_Scene, 1100, 600);
                    Map_1.locate(Rat_House_Scene,200,100)

            if Rat.x <= 30:
                    scene3.enter() # scene 3 진입코드 
                    Rat.scene = 3
                    Rat.x = 1100; Rat.y = 60;
                    Rat.locate(scene3,Rat.x,Rat.y)
                    Switch_ReLocate(scene3)
                    Rat.scene_STAY = True
                    Mini_Map.locate(scene3, 1100, 600);
                    Map_1.locate(scene3,200,100)
        elif Rat.scene_STAY == True:
            if  Rat.x > 200:
                Scene_Stay(610,760,420,520) #scene stay Gate1 
            else:
                Scene_Stay(0, 100, 50, 120) #scene stay Gate3
        
        pass
    elif Rat.scene == 3:
        if Rat.scene_STAY == False: #scene2 진입코드 
            if Rat.x > 1230:
                scene2.enter()
                Rat.scene = 2
                Rat.x = 60; Rat.y = 100;
                Rat.locate(scene2, Rat.x, Rat.y)
                Switch_ReLocate(scene2)
                Rat.scene_STAY = True
                Mini_Map.locate(scene2, 1100, 600);
                Map_1.locate(scene2,200,100)
        elif Rat.scene_STAY == True:
            Scene_Stay(1050, 1200,40, 70 )
        pass
    elif Rat.scene == 4:
        pass

    #4 수정 필요. 
def Switch_ReLocate(SceneName): # 방향키가 해당 씬에도 나타날수 있게 하는 함수입니다. 

    up.locate(SceneName, 1000,120)
    left.locate(SceneName, 930,50)
    down.locate(SceneName, 1000,50)
    right.locate(SceneName, 1100,50)

def On_Trap():

    #트랩의 위치에 생쥐가 도달했는지를 판별합니다. 
    #print문을 이벤트로 바꿀 예정입니다. 
    if Rat.scene == 3: 
        #트랩이 있는 스테이지는 stage 3뿐이므로 이를 제외한 맵에서는 검사를 하지 않습니다.
        if Rat.x >= 450 and Rat.x <= 450+trapSize_x:
            if Rat.y >= 100 and Rat.y <= 100+trapSize_y:
                GG.show()
                debug()
        elif Rat.x >= 650 and Rat.x <= 650+trapSize_x:
            if Rat.y >= 400 and Rat.y <= 400+trapSize_y:
                GG.show()
                debug()
        elif Rat.x >= 550 and Rat.x <= 550+trapSize_x:
            if Rat.y >= 450 and Rat.y <= 450+trapSize_y:
                GG.show()
                debug()
        elif Rat.x >= 50 and Rat.x <= 50+trapSize_x:
            if Rat.y >= 500 and Rat.y <= 500+trapSize_y:
                GG.show()
                debug()
        elif Rat.x >= 100 and Rat.x <= 100+trapSize_x:
            if Rat.y >= 400 and Rat.y <= 400+trapSize_y:
                GG.show()


def Mini_Map_click(x,y,action): #화면 우측 위에 나오는 지도를 띄우기 위한 함수입니다. 클릭하면 지도가 열립니다. 
    Map_1.show()

def Map_1_click(x,y,action): #지도를닫기 위한 함수입니다. 클릭하면 지도가 닫힙니다. 
    Map_1.hide()

def GG_click(x,y,action): # 게임이 끝났다는것을 알리기 위한 기능입니다. 
    endGame()

def Scene_Stay(x1,x2,y1,y2):
    if Rat.x < x1 or Rat.x > x2 or Rat.y < y1 or Rat.y > y2: # 이전 씬에서 소환된 위치에서 벗어나면 위치를 벗어남을 인식합니다. 
                                                             # 무한히 문을 드나드는것을 방지합니다. 
        Rat.scene_STAY = False

up.onMouseAction = up_press
left.onMouseAction = left_press
down.onMouseAction = down_press
right.onMouseAction = right_press
Mini_Map.onMouseAction = Mini_Map_click
Map_1.onMouseAction = Map_1_click
GG.onMouseAction = GG_click

def debug():
    if Rat.scene_STAY == True:
        print("True",  end = " ")
        print(Rat.x, Rat.y)
    elif Rat.scene_STAY == False:
        print("False", end = " ")
        print(Rat.x, Rat.y)

startGame(Rat_House_Scene)
