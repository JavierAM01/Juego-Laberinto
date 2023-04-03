import pygame, random
from constantes import *


class Bullet(pygame.sprite.Sprite):

    def __init__(self, posicion, direccion):
        super().__init__()
        self.pos = posicion
        self.vel = 2 * ZOOM * direccion[0], 2 * ZOOM * direccion[1]
        self.image = pygame.transform.rotate(IM_bala, self.get_angle(direccion)) #pygame.Surface(((ZOOM*DIM)//2, (ZOOM*DIM)//2))
        self.rect = self.image.get_rect()  #pygame.Rect(posicion[0], posicion[1], DIM, DIM)
        self.rect.centerx, self.rect.centery = posicion[0] + self.rect.width//2, posicion[1] + self.rect.width//2
        self.size = self.rect.width
        # pygame.draw.circle(self.image, BLANCO, (self.size//2, self.size//2), self.size//2)

    def get_pos(self): 
        return list(self.pos)
    
    @staticmethod
    def get_angle(dir):
        if dir == [1,0]:
            return 0
        elif dir == [-1,0]:
            return 180
        elif dir == [0,1]:
            return 270
        else:
            return 90


    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect.left, self.rect.top = self.pos[0], self.pos[1]


class Food(pygame.sprite.Sprite):

    def __init__(self, posicion):
        super().__init__()
        self.pos = posicion
        i = random.choices([0,1], weights=[9,1], k=1)[0]
        self.image = IM_comidas[i]
        self.power = POWER_comida[i]
        self.rect = self.image.get_rect()  
        self.rect.left, self.rect.top = posicion[0], posicion[1]
        self.size = self.rect.width

    def change_pos(self, new_pos):
        self.pos = new_pos
        self.rect.left, self.rect.top = new_pos[0], new_pos[1]

    def update(self):
        pass


class Wall(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        self.pos = posicion
        self.image = IM_muro
        self.rect = self.image.get_rect()  #pygame.Rect(posicion[0], posicion[1], DIM, DIM)
        self.rect.left, self.rect.top = posicion[0], posicion[1]
        self.size = self.rect.width

    def update(self):
        pass

    def draw(self, screen):
        print("drawing part")
        super().draw(screen)

class User(pygame.sprite.Sprite):

    def __init__(self, posicion):
        super().__init__()
        self.fuerza = 1
        self.nbalas = 5
        self.vida = 10
        self.velocidad = 1*ZOOM
        self.pos = posicion
        self.direccion = [1,0]
        self.image = IM_usuario
        self.rect = self.image.get_rect()  #pygame.Rect(posicion[0], posicion[1], DIM, DIM)
        self.rect.left, self.rect.top = posicion[0], posicion[1]
        self.size = self.rect.width

    def disparar(self):
        if self.nbalas > 0:
            pos = [self.pos[0], self.pos[1]]
            dir = [self.direccion[0], self.direccion[1]]
            bala = Bullet(pos, dir)
            self.nbalas -= 1
            return bala
        return None
    
    def die(self, name=""):
        print("Killed by:", name)

    def get_pos(self): 
        return list(self.pos)

    def get_rect(self): return self.rect

    def mover(self, new_pos): 
        self.pos = new_pos
        self.rect.left, self.rect.top = new_pos[0], new_pos[1]

    def comer(self, food): 
        self.nbalas += food.power

    def cambiar_direccion(self, _dir): self.direccion = _dir

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass


class Snake_Body(pygame.sprite.Sprite):

    def __init__(self, posicion, i):
        super().__init__()
        self.pos = posicion
        self.image = IM_snake_body[i]
        self.rect = self.image.get_rect()  
        self.rect.center = posicion[0]+(DIM*ZOOM)//2, posicion[1]+(DIM*ZOOM)//2
        self.size = self.rect.width
    
    def change_pos(self, new_pos):
        self.pos = new_pos
        self.rect.center = self.pos[0]+(DIM*ZOOM)//2, self.pos[1]+(DIM*ZOOM)//2
        # self.rect.left, self.rect.top = self.pos[0], self.pos[1]

    def update(self):
        pass


class Snake(pygame.sprite.Sprite):

    def __init__(self, posicion):
        super().__init__()

        self.i = random.choices([0,1], weights=[9,1], k=1)[0]  # índice que indica de qué nivel es la serpiente : {0,1}
        self.image = IM_snake_head[self.i]
        self.power = POWER_snake[self.i]
        self.rect = self.image.get_rect()  
        self.rect.left, self.rect.top = posicion[0], posicion[1]
        self.cuerpo_pos = []

        self.pos = posicion
        self.vida = self.power
        self.velocidad = 3

        self.body = pygame.sprite.Group()
        #self.body.add(Snake_Body(posicion))
        
        self.camino = []
        self.update_rect()

    def draw(self, screen):
        print("Drawing...")
        self.body.draw(screen)

    def add(self, new_snake_part):
        self.body.add(new_snake_part)
        self.update_rect()

    def update(self):
        #self.update_rect()
        self.body.update()

    def update_rect(self):
        self.rect.left, self.rect.top = self.pos[0], self.pos[1]
        #self.rect = self.rectangle.unionall([s.rect for s in self.body.sprites()])   # self.body.sprites()[0].union... body.sprites()[1:]

    def get_shot(self): 
        self.vida -= 1
        if len(self.cuerpo_pos) > 0:
            if self.vida == 0:
                last_pos = self.cuerpo_pos[-1]
                self.cuerpo_pos.pop()
                for s in self.body:
                    if s.pos == last_pos:
                        s.kill()
                self.vida = self.power
        elif self.vida == 0:
            self.kill()

    def kill(self):
        for s in self.body:
            s.kill()
        super().kill()

    @staticmethod
    def check_pos(pos):
        return (pos[0] >= 0 and pos[0] < NX and pos[1] >= 0 and pos[1] < NY)
    
    @staticmethod
    def get_adyacencias(pos):
        return [(pos[0]+1, pos[1]), (pos[0], pos[1]+1), (pos[0]-1, pos[1]), (pos[0], pos[1]-1)]

    def algoritmo_busqueda(self, food_pos, muros):
        
        def invert(pos):
            return (pos[0] // (DIM*ZOOM), pos[1] // (DIM*ZOOM))
        def convert(pos):
            return (pos[0]*DIM*ZOOM, pos[1]*DIM*ZOOM)

        MUROS = [invert(muro.pos) for muro in muros]

        permisos = [[True for j in range(NX)] for i in range(NY)]
        for i,j in self.cuerpo_pos:
            i,j = invert((i,j))
            permisos[i][j] = False
        for i,j in MUROS:
            permisos[i][j] = False

        distancias = [["i" for j in range(NX)] for i in range(NY)]
        _pos = invert(self.pos)
        distancias[_pos[0]][_pos[1]] = 0
        activos = [_pos]

        # comprobar que podemos seguir (buscar adyacencias)
        end = True
        for i,j in self.get_adyacencias(_pos):
            if self.check_pos((i,j)) and permisos[i][j]:  #convert(ady) not in self.cuerpo and convert(ady) not in MUROS and ady[0] >= 0 and ady[0] < NX and ady[1] >= 0 and ady[1] < NY:
                end = False
                break
        if end:
            return False

        # rellenar la matriz distancias (algoritmo de dijkstra)
        run = True
        longitud = 0

        while run:

            longitud += 1
            temp = []

            for pos in activos:
                for i,j in self.get_adyacencias(pos):
                    if self.check_pos((i,j)) and permisos[i][j]:  #if convert(ady) not in self.cuerpo and convert(ady) not in MUROS and ady[0] >= 0 and ady[0] < NX and ady[1] >= 0 and ady[1] < NY:
                            
                        movimiento_valido = False
                        if distancias[i][j] == "i": movimiento_valido = True
                        elif distancias[i][j] > longitud: movimiento_valido = True
                            
                        if movimiento_valido:
                            distancias[i][j]  = longitud
                            if (i,j) not in temp: 
                                temp.append((i,j))
                            if (i,j) == invert(food_pos): 
                                run = False

            if temp == []: run = False
            activos = temp

        def backtracking(posicion):
            i,j = invert(posicion)
            d = distancias[i][j]
            camino = [posicion]
            while d != 1:
                for ady in self.get_adyacencias((i,j)):
                    if self.check_pos(ady) and distancias[ady[0]][ady[1]] == d-1:
                        camino.append(convert(ady))
                        i,j = ady
                        break
                d -= 1
            return camino

        # buscar el camino (más corto) hasta la comida (si existe) 
        if distancias[invert(food_pos)[0]][invert(food_pos)[1]] != "i":
            camino = backtracking(food_pos)
        # si no, hacer el camino más largo que se pueda en el mapa
        else:
            d = 0
            pos = None
            for i in range(NX):
                for j in range(NY):
                    if distancias[i][j] != "i":
                        if distancias[i][j] > d:
                            d = distancias[i][j]
                            pos = (i,j)
            try:
                camino = backtracking(pos)
            except:
                camino = []

        self.camino = camino
        return True

    def mover(self, comida, muros):
        comida_pos = [c.pos for c in comida]
        if self.camino == []:
            comida_elegida = random.choice(comida_pos)
            if not self.algoritmo_busqueda(comida_elegida, muros):
                self.kill()
        else:
            actual_pos = self.pos[0], self.pos[1]
            next_pos = self.camino[-1]
            self.pos = next_pos

            n = len(self.cuerpo_pos)
            if n > 0:
                self.cuerpo_pos.insert(0, actual_pos)
            self.camino.pop()

            if next_pos not in comida_pos: 
                if n > 0:
                    last_pos = self.cuerpo_pos[-1]
                    for s in self.body:
                        if s.pos == last_pos:
                            s.change_pos(actual_pos)
                            break
                    self.cuerpo_pos.pop()
            else:
                if n == 0:
                    self.cuerpo_pos.insert(0, actual_pos)
                return actual_pos, next_pos
        self.update_rect()
        return None, None


class Killer(pygame.sprite.Sprite):

    def __init__(self, posicion):
        super().__init__()
        self.pos = posicion
        self.vida = 3
        self.velocidad = 6
        self.vivo = True
        self.camino = []
        self.image = IM_killer
        self.rect = self.image.get_rect()  #pygame.Rect(posicion[0], posicion[1], DIM, DIM)
        self.rect.left, self.rect.top = posicion[0], posicion[1]
        self.size = self.rect.width

    def mover(self, pos_usuario):
        signo = lambda x : 1 if x > 0 else (-1 if x < 0 else 0)
        x, y = int(pos_usuario[0] - self.pos[0]), int(pos_usuario[1] - self.pos[1])
        move = -1
        if x == 0 and y == 0:
            return 
        if x != 0 and y != 0:
            move = random.randint(0,1)
        if x == 0 or move == 1:
            new_pos = (self.pos[0], self.pos[1] + (DIM*ZOOM) * signo(y))
            self.pos = new_pos
        elif y == 0 or move == 0:
            new_pos = self.pos[0] + (DIM*ZOOM) * signo(x), self.pos[1]
            self.pos = new_pos
        self.rect.left, self.rect.top = self.pos[0], self.pos[1]

    def get_shot(self): 
        self.vida -= 1
        if self.vida == 0:
            self.kill()

    def get_pos(self): return list(self.pos)

    def get_rect(self): return self.rect

    def update(self):
        pass


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = IM_gameover
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHURA//2, ALTURA//2)
    def draw(self, screen):
        screen.blit(self.image, self.rect)


class LevelComplete(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = IM_levelcomplete
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHURA//2, ALTURA//2)
    def draw(self, screen):
        screen.blit(self.image, self.rect)


