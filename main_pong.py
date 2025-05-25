import pygame
import pygame.locals
import pygame.math

class Game:
    def __init__(self, name = "My Game", screensize = (800,600)):
        print ("Loading game: "+name)
        pygame.init()
        self.sprites = pygame.sprite.Group()
        Game.game = self
        
        self.screensize = screensize
        displayoptions = (pygame.HWSURFACE | pygame.SCALED)
        self.display = pygame.display.set_mode(screensize, displayoptions)
        self.clock = pygame.time.Clock()
        self.eventlist = []
        self.background_colour = (250,250,250)
        self.exit = False
        pygame.display.set_caption(name)
    
    def update(self, deltaTime):
        for event in self.eventlist:
            self.processEvent(event)
        self.sprites.update()

    def processEvent(self, event):
        if event.type == pygame.QUIT:
            self.exit = True

    def draw(self):
        self.display.fill(self.background_colour)
        self.sprites.draw(self.display)

    def run(self):
        print("run")
        while not self.exit:
            deltaTime = self.clock.tick(60)
            self.eventlist = pygame.event.get()
            self.update(deltaTime)
            self.draw()
            pygame.display.update()
        pygame.quit

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x,y,):
        print("paddle init")
        super().__init__()
        self.image = pygame.Surface([15,80])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.paddleup = False
        self.paddledown = False
        self.control_up = False
        self.control_down = False
    def update(self):
        super().update()
        print(self.rect.y)
        if self.control_down == True:
            if self.rect.y > 475:
                return
            self.rect.y += 5
        if self.control_up == True:
            if self.rect.y < 50:
                return
            self.rect.y -= 5
        if self.paddledown == True:
            if self.rect.y > 475:
                return
            self.rect.y += 5
        if self.paddleup == True:
            if self.rect.y < 50:
                return
            self.rect.y -= 5
    
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("ball.jpg")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity = pygame.math.Vector2 (6, 3)
    
    def update(self): 
        (vx, vy) = self.velocity
        player1_pos = Game.game.player1.rect.center
        player2_pos = Game.game.player2.rect.center
        if self.rect.x > 699 or self.rect.x < 5:
            vx = -1 * vx
        if self.rect.y > 500 or self.rect.y< 1:
            vy = -1 * vy
        if self.rect.colliderect(Game.game.player1.rect):
            vx = -1 * vx
        if self.rect.colliderect(Game.game.player2.rect):
            vx = -1 * vx
        self.velocity = pygame.math.Vector2(vx, vy)
        self.rect.y += vy
        self.rect.x += vx
        print("ball x:", self.rect.x)
        print("ball y:", self.rect.y)


class PongGame(Game):
    def __init__(self):
        print("Pong init")
        super().__init__(name = "Pong")
        #self.player1.image = pygame.Surface([15,80])
        #self.player1.image.fill((0,0,0))
        #self.player1.rect = self.player1/image.get_rect()
        self.player1 = Paddle(45,300)
        self.sprites.add(self.player1)
        self.player2 = Paddle(750,300)
        self.sprites.add(self.player2)
        self.ball = Ball(400,300)
        self.sprites.add(self.ball)
        self.sprites.update()

    def processEvent(self, event):
        super().processEvent(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.locals.K_w:
                print ("W pressed")
                self.player1.control_up = True
            if event.key == pygame.locals.K_s:
                print("S pressed")
                self.player1.control_down = True
            if event.key == pygame.locals.K_UP:
                print ("UP pressed")
                self.player2.paddleup = True
            if event.key == pygame.locals.K_DOWN:
                print("DOWN pressed")
                self.player2.paddledown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.locals.K_w:
                print ("W released")
                self.player1.control_up = False
            if event.key == pygame.locals.K_s:
                print("S released")
                self.player1.control_down = False
            if event.key == pygame.locals.K_UP:
                print ("UP released")
                self.player2.paddleup = False
            if event.key == pygame.locals.K_DOWN:
                print("DOWN released")
                self.player2.paddledown = False
PongGame().run()
