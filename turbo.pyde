import random, os, time
add_library ('sound')
path = os.getcwd ()
#classes

class Game:
    def __init__(self):
        self.w=1280
        self.h=700
        self.lane= 'lane'
        self.paused = False
        self.state = 'menu'
        self.name=''
        self.img = loadImage (path+ '\\resources\\bg.png')
        
    def create_game (self):
        # self.lanes=[]
        self.bgImgs=[]
        self.obscar=[]
        self.x=0
        self.cnt=0
        self.sec = 120
        self.user_car = userCar(50,620,150,70,"\\resources\\ucar.png")
        # self.user_car1= userCar(50,480,150,70,"\\resources\\car6.png")
        # self.user_car2= userCar(50,550,150,70,"\\resources\\car5.png")
        
        for i in range (12):
            self.obscar.append(obstacleCar((200+i*150),(490+70*random.randint(0,2)),150,70,'\\resources\\car'+str(random.randint(0,6))+'.png'))
        
        #image layers of the background 
        for i in range(4):
            self.bgImgs.append(loadImage(path+'\\resources\\layer'+str(i+1)+'.png'))
        #pause sound
        
        #load resources form the stage file (2 stages)
        
        

    

    
    def display (self):
        cnt = 0
        for img in self.bgImgs:
            if cnt == 0:
                x = (self.x//10)%self.w
            elif cnt == 1:
                x = (self.x//5)%self.w
            elif cnt == 2:
                x = (self.x//3)%self.w
            else:
                x = (self.x)%self.w
                
            image(img,0,0,self.w-x,self.h,x,0,self.w,self.h)
            image(img,self.w-x-1,0,x,self.h,0,0,x,self.h)
            cnt+=1
            
        self.cnt = (self.cnt +1)%60
        if self.cnt == 0:
            self.sec -=1
        
        fill(0)
        textSize(32)
        if self.sec%60<10 and self.sec//60<10:
            text('0{0}:0{1}'.format(self.sec//60,self.sec%60), 10, 50)
        elif self.sec//60<10:
            text('0{0}:{1}'.format(self.sec//60,self.sec%60), 10, 50)
        elif self.sec%60<10:
            text('{0}:0{1}'.format(self.sec//60,self.sec%60), 10, 50)
        else:
            text('{0}:{1}'.format(self.sec//60,self.sec%60), 10, 50)
            
        self.user_car.display()
        
        for i in self.obscar:
            i.display()

                
class Car:
    def __init__(self,x,y,w,h,ImgName):
        self.x=x
        self.y=y
        self.h=h
        self.w=w
        self.lane=0
        #top lane y=490
        #mid lane y=560
        #bot lane y=630
        self.img=loadImage(ImgName)
        self.direction=1
        
    def update(self):
        self.y+=self.lane
    def display(self):
        self.update()
        image(self.img,self.x,self.y,self.w,self.h)
        
class userCar(Car):
    def __init__(self,x,y,w,h,ImgName):
        Car.__init__ (self,x,y,w,h,ImgName)
        self.keyHandler={UP:False,DOWN:False}
        

    
    def update(self):
        if self.keyHandler[UP]:
            self.lane = -10
        elif self.keyHandler[DOWN]:
            self.lane = 10
        else:
            self.lane = 0
        self.y+=self.lane
        # self.move_sound=SoundFile (path+'\\resorces\\move_sound.mp3')
        
    #def display(self):
        
    

class obstacleCar(Car):
    def __init__(self,x,y,w,h,ImgName):
        Car.__init__ (self,x,y,w,h,ImgName)
        
      
    #def display (self):
        #image (self.obscar,50, 50,self.w,self.h)
  
  
#class racetrack:
    #def __init__(self,track):
        #self.track=track
        
    #def createtrack(self,trackwidth):
        #self.trackwidth=trackwidth
      

    




game = Game()

def setup():
    size (game.w,game.h)
    background(0)
    game.create_game()
  
  
def draw():
    if game.state == 'menu':
        image (game.img, 0, 0, game.w, game.h)
        
        if game.state=='menu' and game.w//2-80 <= mouseX <= game.w//2+80 \
        and game.h//2-110 <= mouseY <= game.h//2-80:
            fill(255,0,0)
        else:
            fill(0)
        textSize(32)
        text("Play Game",game.w//2-80,game.h//2-80)
        if game.state=='menu' and game.state=='menu' and game.w//2-80 <= mouseX <= game.w//2+80 \
        and game.h//2-10 <= mouseY <= game.h//2+40:
            fill(255,0,0)
        else:
            fill(0)
        textSize(32)
        text("Highscores", game.w//2-80,game.h//2+30)
        fill(0)
        textSize(72)
        text('TURBO',game.w//2-110,game.h-600)
        
    elif game.state == 'play':
        if not game.paused:
            background(0)
            game.display()
        else:
            fill(255,0,0)
            textSize(32)
            text("Pause",game.w//2,game.h//2)
    elif game.state=='inputName':
        background(0)
        textSize(32)
        text("Please enter your name",game.w//2,game.h//2-200)
        text(game.name,game.w//2,game.h//2)
  
def keyPressed():
    if game.state == 'play':
        game.user_car.keyHandler[keyCode]=True
 
        
  
def keyReleased():
    game.user_car.keyHandler[keyCode]=False
  
def mouseClicked():
    if game.state=='menu' and game.w//2-80 <= mouseX <= game.w//2+80 \
        and game.h//2-110 <= mouseY <= game.h//2-80:
       game.state='play'
    if game.state=='menu' and game.state=='menu' and game.state=='menu' and game.w//2-80 <= mouseX <= game.w//2+80 \
        and game.h//2-10 <= mouseY <= game.h//2+40:
       game.state='highscores'
