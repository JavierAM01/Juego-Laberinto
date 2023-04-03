import pygame 
from mapas import get_map
import personajes as P
import random
import os
from constantes import *



def cuadrar_coordenada(pos):
    new_pos = [DIM*(pos[0]//DIM), DIM*(pos[1]//DIM)]
    return new_pos


class Game:

    def __init__(self, map_level=1):

        # nivel del mapa 
        self.MUROS, self.inicio_usuario, self.inicio_snake, self.inicio_killer = get_map(level=map_level)

        # crear personajes
        self.BALAS   = []
        self.COMIDA  = []
        self.SNAKES  = [P.Snake(self.inicio_snake)]
        self.KILLERS = [P.Killer(self.inicio_killer)]
        self.USUARIO = P.Usuario(self.inicio_usuario)

        # nº de enemigos a crear
        self.N_snakes = 3  
        self.N_killers = 6

    def make_food(self):
        done = False
        while not done:
            pos = [DIM*random.randint(0,NX-1), DIM*random.randint(0,NY-1)]
            if pos not in self.MUROS and pos[0] >= 0 and pos[0] < ANCHURA and pos[1] >= 0 and pos[1] < ALTURA:
                done = True
                self.COMIDA.append(pos)

    def mover_personajes(self, tiempo_aux):
        # snakes
        if len(self.SNAKES) > 0  and tiempo_aux % self.SNAKES[0].velocidad == 0:
            for snake in self.SNAKES:
                if len(self.COMIDA) > 0:
                    if snake.esta_vivo():
                        l = snake.mover(self.COMIDA, self.MUROS)
                        if l != []: 
                            self.COMIDA.remove(l)
        # killers
        if len(self.KILLERS) > 0 and tiempo_aux % self.KILLERS[0].velocidad == 0:
            for killer in self.KILLERS:
                if killer.esta_vivo():
                    killer.mover(cuadrar_coordenada(self.USUARIO.get_pos()), self.MUROS)



class Display:

    def __init__(self):

        self.game = Game()

        # inicio del juego
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHURA, ALTURA))
        pygame.display.set_caption("Nivel 1")
        self.font = pygame.font.Font(None, 30)

    @staticmethod
    def zoom(pos_usuario):
        x, y = pos_usuario[0]-ANCHURA/(ZOOM*2), pos_usuario[1]-ANCHURA/(ZOOM*2)
        lim_superior = ANCHURA - ANCHURA/ZOOM
        if x < 0: x = 0
        elif  x > lim_superior: x = lim_superior
        if y < 0: y = 0
        elif  y > lim_superior: y = lim_superior
        transformar = lambda pos : [ZOOM*(pos[0]-x), ZOOM*(pos[1]-y)]
        return transformar

    @staticmethod
    def conseguir_esquinas(pos):
        pos1 = cuadrar_coordenada(pos)
        pos2 = cuadrar_coordenada([pos[0]+DIM*0.9, pos[1]])
        pos3 = cuadrar_coordenada([pos[0]+DIM*0.9, pos[1]+DIM*0.9])
        pos4 = cuadrar_coordenada([pos[0], pos[1]+DIM*0.9])
        return [pos1, pos2, pos3, pos4]

    def mover_usuario(self):
        keys = pygame.key.get_pressed()
        new_pos = self.game.USUARIO.get_pos()
        if keys[pygame.K_KP6]:
            new_pos[0] += self.game.USUARIO.velocidad
            self.game.USUARIO.cambiar_direccion([1,0])
        if keys[pygame.K_KP4]:
            new_pos[0] -= self.game.USUARIO.velocidad
            self.game.USUARIO.cambiar_direccion([-1,0])
        if keys[pygame.K_KP8]:
            new_pos[1] -= self.game.USUARIO.velocidad
            self.game.USUARIO.cambiar_direccion([0,-1])
        if keys[pygame.K_KP5]:
            new_pos[1] += self.game.USUARIO.velocidad
            self.game.USUARIO.cambiar_direccion([0,1])
        [pos1, pos2, pos3, pos4] = self.conseguir_esquinas(new_pos)
        if pos1 not in self.game.MUROS and pos2 not in self.game.MUROS and pos3 not in self.game.MUROS and pos4 not in self.game.MUROS and pos1[0] >= 0 and pos2[0] < ANCHURA and pos1[1] >= 0 and pos3[1] < ALTURA:
            self.game.USUARIO.mover(new_pos)
            for c in self.game.COMIDA:
                if c in [pos1, pos2, pos3, pos4]:
                    self.game.USUARIO.comer()
                    self.game.COMIDA.remove(c)

    def colisiones(self, run):
        for snake in self.game.SNAKES:
            for snake_rect in snake.get_rect():
                if self.game.USUARIO.get_rect().colliderect(snake_rect):
                    self.game.USUARIO.die()
                    run = False
        for killer in self.game.KILLERS:
            if self.game.USUARIO.get_rect().colliderect(killer.get_rect()):
                self.game.USUARIO.die()
                run = False
        for bala in self.game.BALAS:
            golpeado = False
            if cuadrar_coordenada(bala.get_pos()) in self.game.MUROS: 
                self.game.BALAS.remove(bala)
                break
            for killer in self.game.KILLERS:
                if bala.rect.colliderect(killer.get_rect()):
                    killer.golpear()
                    self.game.BALAS.remove(bala)
                    golpeado = True
                    break
            if golpeado:
                break
            for snake in self.game.SNAKES:
                for snake_rect in snake.get_rect():
                    if bala.rect.colliderect(snake_rect):
                        snake.golpear()
                        self.game.BALAS.remove(bala)
                        break
        return run

    def draw_screen(self, transformar, end_level = False, level_done = False):
        self.screen.blit(IM_fondo, transformar([0,0]))
        for pos in self.game.MUROS:
            self.screen.blit(IM_muro, transformar(pos))
            #pygame.draw.rect(self.screen, COLOR_PARED, pygame.Rect(pos[0], pos[1], DIM, DIM))
        
        """
        # cuadrícula
        for i in range(NY+1): 
            pos = transformar([0, i*DIM])
            pygame.draw.rect(self.screen, GRIS, pygame.Rect(pos[0], pos[1], ZOOM*ANCHURA, 2))
        for i in range(NX+1): 
            pos = transformar([i*DIM, 0])
            pygame.draw.rect(self.screen, GRIS, pygame.Rect(pos[0], pos[1], 2, ZOOM*ALTURA))
        """
        for pos in self.game.COMIDA:
            self.screen.blit(IM_comida, transformar(pos))
        # personajes
        if self.game.USUARIO.esta_vivo(): self.game.USUARIO.actualizar(self.screen, transformar)
        for snake in self.game.SNAKES:
            if snake.esta_vivo(): snake.actualizar(self.screen, transformar)
            else: self.game.SNAKES.remove(snake)
        for killer in self.game.KILLERS:
            if killer.esta_vivo(): killer.actualizar(self.screen, transformar)
            else: self.game.KILLERS.remove(killer)
        for bala in self.game.BALAS: 
            pos = transformar([bala.get_pos()[0]+DIM//2, bala.get_pos()[1]+DIM//2])
            pygame.draw.circle(self.screen, BLANCO, (pos[0], pos[1]), ZOOM*3, ZOOM*2)
        # numero de balas
        contador = self.font.render(f"Balas: {self.game.USUARIO.nbalas}", 0, BLANCO)
        self.screen.blit(contador, (ANCHURA//2-40, 20))
        # botones del final
        if end_level:
            if level_done: boton_level_completed.actualizar(self.screen)
            else: boton_lose.actualizar(self.screen)
        # reloj.tick(fps)
        pygame.display.flip()

    def jugar(self):
        run = True
        reloj = pygame.time.Clock()
        fps = 100
        tiempo_aux = (pygame.time.get_ticks()//100) + 50 # centisegundos
        count_snake = 1
        count_killer = 1
        level_done = False
        quit = False
        while run:
            reloj.tick(fps)
            if len(self.game.SNAKES) == 0 and len(self.game.KILLERS) == 0 and count_snake == self.game.N_snakes and count_killer == self.game.N_killers:
                level_done = True
                run = False
            if len(self.game.COMIDA) < 4: self.game.make_food()
            for bala in self.game.BALAS: bala.actualizar()
            time = pygame.time.get_ticks() // 100
            if time == tiempo_aux:
                tiempo_aux += 1
                self.game.mover_personajes(tiempo_aux)
                if tiempo_aux % 100 == 0:
                    if count_snake < self.game.N_snakes:
                        count_snake += 1
                        snake = P.Snake(self.game.inicio_snake)
                        self.game.SNAKES.append(snake)
                    if count_killer < self.game.N_killers:
                        count_killer += 1
                        killer = P.Killer(self.game.inicio_killer)
                        self.game.KILLERS.append(killer)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bala = self.game.USUARIO.disparar()
                        if bala != None: self.game.BALAS.append(bala)
            self.mover_usuario()
            run = self.colisiones(run)
            transformar = self.zoom(self.game.USUARIO.get_pos())
            self.draw_screen(transformar)
        # fin de nivel 
        if not quit:
            run2 = True
            temp_transformar = self.zoom(self.game.USUARIO.get_pos())
            while run2:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run2 = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if level_done:
                            if boton_level_completed.get_rect().collidepoint(pygame.mouse.get_pos()):
                                run2 = False 
                        else:
                            if boton_lose.get_rect().collidepoint(pygame.mouse.get_pos()):
                                run2 = False 
                self.draw_screen(temp_transformar, end_level = True, level_done = level_done)


if __name__ == "__main__":
    display = Display()
    display.jugar()