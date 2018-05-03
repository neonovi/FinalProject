import time, random, os

#classes

class Game:
    def __init__(self):
        self.w=1280
        self.h=700
        self.paused = False
        self.state = 'menu'
        self.name=''
        
    def create_game ():
        self.lanes=[]
        self.bgImgs=[]
        self.x=0
        self.time = 120
        #image layers of the background 
            #for loop here
        #pause sound
        #load resources form the stage file (2 stages)
    
    def display ():
        self.cnt = (self.cnt +1)%60
        if self.cnt == 0:
            self.time -=1

class Car:
    def __init__(self,x,y,h,w,model):
        self.x=x
        self.y=y
        self.h=h
        self.w=w
        self.model=model
        
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
    size (game.w,game.h)
    background(0)
    game.create_game
  
  
def draw():
    if game.state == 'menu':
        background(0)
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
  
  
def keyPressed():
    pass
  
def keyReleased():
    pass
  
def mouseClicked():
    pass
