import random, os
add_library ('sound')
path = os.getcwd ()
#classes

class Game:
    def __init__(self):
        self.w=1280
        self.h=700
        self.paused = False
        self.state = 'menu'
        self.name=''
        self.img = loadImage (path+ '\\resources\\bg.png')
        
    def create_game (self):
        self.lanes=[]
        self.bgImgs=[]
        self.x=0
        self.cnt=0
        self.sec = 0
                
        #image layers of the background 
        for i in range(4):

            self.bgImgs.append(loadImage(path+'\\resources\\layer'+str(i+1)+'.png'))
        #pause sound
        #load resources form the stage file (2 stages)
    
    def display (self):
        self.cnt = (self.cnt +1)%60
        if self.cnt == 0:
            self.sec +=1
        
        fill(255)
        if self.sec%60<10 and self.sec//60<10:
            text('0{0}:0{1}'.format(self.sec//60,self.sec%60), 10, 50)
        elif self.sec//60<10:
            text('0{0}:{1}'.format(self.sec//60,self.sec%60), 10, 50)
        elif self.sec%60<10:
            text('{0}:0{1}'.format(self.sec//60,self.sec%60), 10, 50)
        else:
            text('{0}:{1}'.format(self.sec//60,self.sec%60), 10, 50)
            
class Car:
    def __init__(self,x,y,h,w):
        self.x=x
        self.y=y
        self.h=h
        self.w=w

        
    #def display(self):
        #displaying the car
        
#class userCar(Car):
    #pass

#class obstacleCar(Car):
    #pass
      
  
  
  
#class racetrack:
    #def __init__(self,track):
        #self.track=track
        
    #def createtrack(self,trackwidth):
        #self.trackwidth=trackwidth
      






game = Game()

def setup():
    frameRate(500)
    size (game.w,game.h)
    background(0)
    game.create_game()
  
  
def draw():
    if game.state == 'menu':
        background(255)
        image (game.img, 0, 0, game.h, game.w)
        if game.state=='menu' and game.w//2-80 <= mouseX <= game.w//2+80 \
        and game.h//2-110 <= mouseY <= game.h//2-80:
            fill(0,255,0)
        else:
            fill(255)
        textSize(32)
        text("Play Game",game.w//2-80,game.h//2-80)
        if game.state=='menu' and game.state=='menu' and game.w//2-80 <= mouseX <= game.w//2+80 \
        and game.h//2-10 <= mouseY <= game.h//2+40:
            fill(0,255,0)
        else:
            fill(255)
        textSize(32)
        text("Highscores", game.w//2-80,game.h//2+30)
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
    pass
  
def keyReleased():
    pass
  
def mouseClicked():
    if game.state=='menu' and game.w//2-80 <= mouseX <= game.w//2+80 \
        and game.h//2-110 <= mouseY <= game.h//2-80:
       game.state='play'
    if game.state=='menu' and game.state=='menu' and game.state=='menu' and game.w//2-80 <= mouseX <= game.w//2+80 \
        and game.h//2-10 <= mouseY <= game.h//2+40:
       game.state='highscores'
