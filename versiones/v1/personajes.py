import pygame, random, os
import copy
from constantes import *


class Bala:

    def __init__(self, posicion, direccion):
        self.pos = posicion
        self.rect = pygame.Rect(posicion[0], posicion[1], DIM // 2, DIM // 2)
        direccion[0] *= 2
        direccion[1] *= 2
        self.vel = direccion

    def get_pos(self): return list(self.pos)

    def actualizar(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], DIM // 2, DIM // 2)


class Usuario:

    def __init__(self, posicion):
        self.fuerza = 1
        self.nbalas = 5
        self.vida = 10
        self.velocidad = 1
        self.pos = posicion
        self.vivo = True
        self.direccion = [1,0]
        self.rect = pygame.Rect(posicion[0], posicion[1], DIM, DIM)

    def golpear(self, fuerza): 
        self.vida -= fuerza

    def disparar(self):
        if self.nbalas > 0:
            bala = Bala(self.pos, self.direccion)
            self.nbalas -= 1
            return bala
        return None

    def get_pos(self): return list(self.pos)

    def get_rect(self): return self.rect

    def mover(self, new_pos): self.pos = new_pos

    def comer(self): self.nbalas += 5

    def cambiar_direccion(self, _dir): self.direccion = _dir

    def actualizar(self, pantalla, transformar):
        if self.vida <= 0: self.vivo = False
        self.rect = pygame.Rect(self.pos[0], self.pos[1], DIM, DIM)
        pantalla.blit(IM_usuario, transformar(self.pos))
        # pygame.draw.rect(pantalla, AZUL, self.rect)

    def esta_vivo(self): return self.vivo

    def die(self): self.vivo = False


class Snake:

    def __init__(self, posicion):
        self.cuerpo = [posicion]
        self.pos = self.cuerpo[0]
        self.rect = [pygame.Rect(posicion[0], posicion[1], DIM, DIM)]
        self.vida = 1
        self.velocidad = 3
        self.vivo = True
        self.camino = []

    def algoritmo_busqueda(self, food_pos, MUROS):

        def invert(pos):
            return [int(pos[0]/DIM), int(pos[1]/DIM)]
        def convert(pos):
            return [pos[0]*DIM, pos[1]*DIM]

        distancias = [["i" for j in range(NX)] for i in range(NY)]
        distancias[invert(self.pos)[0]][invert(self.pos)[1]] = 0
        activos = [list(invert(self.pos))]

        _pos = activos[0]
        end = True
        for ady in [[_pos[0]+1, _pos[1]], [_pos[0], _pos[1]+1], [_pos[0]-1, _pos[1]], [_pos[0], _pos[1]-1]]:
            if convert(ady) not in self.cuerpo and convert(ady) not in MUROS and ady[0] >= 0 and ady[0] < NX and ady[1] >= 0 and ady[1] < NY:
                end = False
                break
        del _pos
        if end:
            return False

        run = True
        longitud = 0

        while run:

            longitud += 1
            temp = []

            for pos in activos:
                for ady in [[pos[0]+1, pos[1]], [pos[0], pos[1]+1], [pos[0]-1, pos[1]], [pos[0], pos[1]-1]]:
                    if convert(ady) not in self.cuerpo and convert(ady) not in MUROS and ady[0] >= 0 and ady[0] < NX and ady[1] >= 0 and ady[1] < NY:
                            
                        movimiento_valido = False
                        if distancias[ady[0]][ady[1]] == "i": movimiento_valido = True
                        elif distancias[ady[0]][ady[1]] > longitud: movimiento_valido = True
                            
                        if movimiento_valido:
                            distancias[ady[0]][ady[1]] = longitud
                            if ady not in temp: 
                                temp.append(list(ady))
                            if ady == invert(food_pos): 
                                run = False

            if temp == []: run = False
            activos = temp

        def backtracking(posicion):
            d = distancias[invert(posicion)[0]][invert(posicion)[1]]
            camino = [list(posicion)]
            pos = invert(posicion)
            while d != 1:
                encontrado = False
                for ady in [[pos[0]+1, pos[1]], [pos[0], pos[1]+1], [pos[0]-1, pos[1]], [pos[0], pos[1]-1]]:
                    if not encontrado and ady[0] >= 0 and ady[0] < NX and ady[1] >= 0 and ady[1] < NY:
                        if distancias[ady[0]][ady[1]] == d-1:
                            camino.insert(0, list(convert(ady)))
                            encontrado = True
                            pos = ady
                d -= 1
            return camino

        if distancias[invert(food_pos)[0]][invert(food_pos)[1]] != "i":
            camino = backtracking(food_pos)
        else:
            d = 0
            pos = None
            for i in range(NX):
                for j in range(NY):
                    if distancias[i][j] != "i":
                        if distancias[i][j] > d:
                            d = distancias[i][j]
                            pos = [i,j]
            camino = backtracking(pos)

        self.camino = camino
        return True

    def mover(self, comida, muros):
        if self.camino == []:
            comida_elegida = random.choice(comida)
            if not self.algoritmo_busqueda(comida_elegida, muros):
                self.vivo = False
        else:
            next_pos = list(self.camino[0])

            self.cuerpo.insert(0, next_pos)
            self.rect.insert(0, pygame.Rect(next_pos[0], next_pos[1], DIM, DIM))
            self.camino.pop(0)

            if next_pos not in comida: 
                self.cuerpo.pop()
                self.rect.pop()
            else:
                return next_pos
        return []

    def esta_vivo(self): return self.vivo

    def golpear(self): 
        self.cuerpo.pop()
        self.rect.pop()

    def die(self): self.vivo = False

    def get_pos(self): return list(self.cuerpo)

    def get_rect(self): return self.rect

    def actualizar(self, pantalla, transformar):
        self.vida = len(self.cuerpo)
        if self.vida <= 0: 
            self.vivo = False
            self.pos = [-DIM, -DIM]
        else: 
            self.pos = self.cuerpo[0]
            for pos in self.cuerpo:
                pantalla.blit(IM_snake, transformar(pos))






class Killer:

    def __init__(self, posicion):
        self.pos = posicion
        self.rect = pygame.Rect(posicion[0], posicion[1], DIM, DIM)
        self.vida = 3
        self.velocidad = 6
        self.vivo = True
        self.camino = []

    def algoritmo_busqueda(self, pos_usuario, MUROS):

        def invert(pos):
            return [int(pos[0]/DIM), int(pos[1]/DIM)]
        def convert(pos):
            return [pos[0]*DIM, pos[1]*DIM]

        distancias = [["i" for j in range(NX)] for i in range(NY)]
        distancias[invert(self.pos)[0]][invert(self.pos)[1]] = 0
        activos = [list(invert(self.pos))]

        run = True
        longitud = 0

        while run:

            longitud += 1
            temp = []

            for pos in activos:
                for ady in [[pos[0]+1, pos[1]], [pos[0], pos[1]+1], [pos[0]-1, pos[1]], [pos[0], pos[1]-1]]:
                    if convert(ady) not in MUROS and ady[0] >= 0 and ady[0] < NX and ady[1] >= 0 and ady[1] < NY:
                            
                        movimiento_valido = False
                        if distancias[ady[0]][ady[1]] == "i": movimiento_valido = True
                        elif distancias[ady[0]][ady[1]] > longitud: movimiento_valido = True
                            
                        if movimiento_valido:
                            distancias[ady[0]][ady[1]] = longitud
                            if ady not in temp: 
                                temp.append(list(ady))
                            if ady == invert(pos_usuario): 
                                run = False

            if temp == []: run = False
            activos = temp

        def backtracking(posicion):
            d = distancias[invert(posicion)[0]][invert(posicion)[1]]
            camino = [list(posicion)]
            pos = invert(posicion)
            while d != 1:
                encontrado = False
                for ady in [[pos[0]+1, pos[1]], [pos[0], pos[1]+1], [pos[0]-1, pos[1]], [pos[0], pos[1]-1]]:
                    if not encontrado and ady[0] >= 0 and ady[0] < NX and ady[1] >= 0 and ady[1] < NY:
                        if distancias[ady[0]][ady[1]] == d-1:
                            camino.insert(0, list(convert(ady)))
                            encontrado = True
                            pos = ady
                d -= 1
            return camino

        if distancias[invert(pos_usuario)[0]][invert(pos_usuario)[1]] != "i":
            camino = backtracking(pos_usuario)
        else:
            d = 0
            pos = None
            for i in range(NX):
                for j in range(NY):
                    if distancias[i][j] != "i":
                        if distancias[i][j] > d:
                            d = distancias[i][j]
                            pos = [i,j]
            camino = backtracking(pos)

        self.camino = camino
        return True

    def mover(self, pos_usuario, muros):
        if self.camino == []:
            if not self.algoritmo_busqueda(pos_usuario, muros):
                self.vivo = False
        else:
            next_pos = list(self.camino[0])
            self.pos = next_pos
            self.camino.pop(0)

    def esta_vivo(self): return self.vivo

    def golpear(self): 
        self.vida -= 1

    def die(self): self.vivo = False

    def get_pos(self): return list(self.pos)

    def get_rect(self): return self.rect

    def actualizar(self, pantalla, transformar):
        if self.vida <= 0: 
            self.vivo = False
            self.pos = [-DIM, -DIM]
            self.rect = pygame.Rect(self.pos[0],self.pos[1],DIM,DIM)
        else: 
            self.rect = pygame.Rect(self.pos[0],self.pos[1],DIM,DIM)
            pantalla.blit(IM_killer, transformar(self.pos))
            # pygame.draw.rect(pantalla, ROJO, pygame.Rect(self.pos[0], self.pos[1], DIM, DIM))



