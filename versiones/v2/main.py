import pygame 
from mapas import get_map
import personajes as P
import random
from constantes import *




class Game:

    def __init__(self, map_level=1):

        # nivel del mapa 
        muros_pos, inicio_usuario, inicio_snake, inicio_killer = get_map(level=map_level)
        self.inicio_usuario = (ZOOM * inicio_usuario[0], ZOOM * inicio_usuario[1])
        self.inicio_enemy  = [(ZOOM * inicio_killer[0], ZOOM * inicio_killer[1]), (0, ZOOM * inicio_killer[1]), 
                                    (ZOOM * inicio_snake[0], ZOOM * inicio_snake[1]), (ZOOM * inicio_snake[0], 0)]

        # crear sprites
        self.MUROS   = pygame.sprite.Group()
        self.BALAS   = pygame.sprite.Group()
        self.COMIDA  = pygame.sprite.Group()
        self.KILLERS = pygame.sprite.Group()
        self.SNAKES  = pygame.sprite.Group()
        self.USUARIO = P.User(self.inicio_usuario)
        
        self.SNAKES.add(P.Snake(random.choice(self.inicio_enemy)))
        self.KILLERS.add(P.Killer(random.choice(self.inicio_enemy)))
        for pos in muros_pos:
            zoom_pos = pos[0]*ZOOM, pos[1]*ZOOM
            self.MUROS.add(P.Wall(zoom_pos))

        # nº de enemigos a crear
        self.N_snakes = 3  
        self.N_killers = 6



class Display:

    def __init__(self):

        self.game = Game()

        # inicio del juego
        pygame.init()
        self.window = pygame.display.set_mode((ANCHURA, ALTURA))
        self.screen = pygame.Surface((ANCHURA*ZOOM, ALTURA*ZOOM))
        pygame.display.set_caption("Nivel 1")
        self.font = pygame.font.Font(None, 30)

        # sprites
        self.all_sprites = pygame.sprite.Group()
        
        self.all_sprites.add(self.game.MUROS)
        self.all_sprites.add(self.game.KILLERS)
        self.all_sprites.add(self.game.SNAKES)
        self.all_sprites.add(self.game.BALAS)
        self.all_sprites.add(self.game.COMIDA)
        self.all_sprites.add(self.game.USUARIO)

        # for wall in self.game.MUROS:
        #     self.all_sprites.add(wall)
        # for killer in self.game.KILLERS:
        #     self.all_sprites.add(killer)
        # for snake in self.game.SNAKES:
        #     for snake_body in snake.body:
        #         self.all_sprites.add(snake_body)
        # for bullet in self.game.BALAS:
        #     self.all_sprites.add(bullet)
        # for food in self.game.COMIDA:
        #     self.all_sprites.add(food)


    # def zoom(self):
    #     pos_usuario = self.game.USUARIO.get_pos()
    #     x, y = pos_usuario[0]-ANCHURA/(ZOOM*2), pos_usuario[1]-ANCHURA/(ZOOM*2)
    #     lim_superior = ANCHURA - ANCHURA/ZOOM
    #     if x < 0: x = 0
    #     elif  x > lim_superior: x = lim_superior
    #     if y < 0: y = 0
    #     elif  y > lim_superior: y = lim_superior
    #     transformar = lambda pos : [ZOOM*(pos[0]-x), ZOOM*(pos[1]-y)]
    #     return transformar
    
    def get_camara(self):
        pos_usuario = self.game.USUARIO.get_pos()
        x = min(max(0, pos_usuario[0] - ANCHURA // 2), ANCHURA*ZOOM - ANCHURA)
        y = min(max(0, pos_usuario[1] - ALTURA // 2), ALTURA*ZOOM - ALTURA)
        return -x, -y

    def make_food(self):
        food = P.Food([0,0])
        while True:
            pos = [ZOOM*DIM*random.randint(0,NX-1), ZOOM*DIM*random.randint(0,NY-1)]
            food.change_pos(pos)
            if pygame.sprite.spritecollide(food, self.game.MUROS, dokill=False) == []: #pos not in self.MUROS and pos[0] >= 0 and pos[0] < ANCHURA and pos[1] >= 0 and pos[1] < ALTURA:
                self.game.COMIDA.add(food)
                self.all_sprites.add(food)
                break

    def move_enemies(self, tiempo_aux):
        # snakes
        if len(self.game.SNAKES) > 0  and tiempo_aux % self.game.SNAKES.sprites()[0].velocidad == 0:
            # del_s = []
            for i, snake in enumerate(self.game.SNAKES):
                if len(self.game.COMIDA) > 0:
                    pos_food = snake.mover(self.game.COMIDA, self.game.MUROS)
                    # if snake.vida == 0:
                    #     del_s.append(i)
                    if pos_food != None: 
                        new_snake_part = P.Snake_Body(pos_food)
                        snake.add(new_snake_part)
                        self.all_sprites.add(new_snake_part)
                        for comida in self.game.COMIDA:
                            if comida.pos == pos_food:
                                comida.kill()
                                break
            # # eliminar las serpientes muertas // normalmente son 0 pues es solo cuando se matan ellas mismas
            # e = 0
            # for i in del_s:
            #     del self.game.SNAKES[i-e]
            #     e += 1
        # killers
        if len(self.game.KILLERS) > 0 and tiempo_aux % self.game.KILLERS.sprites()[0].velocidad == 0:
            for killer in self.game.KILLERS:
                killer.mover(self.game.USUARIO.get_pos())

    def move_user(self):
        keys = pygame.key.get_pressed()
        actual_pos = self.game.USUARIO.get_pos()
        new_pos = self.game.USUARIO.get_pos()
        if keys[pygame.K_KP6]:
            new_pos[0] = min(new_pos[0] + self.game.USUARIO.velocidad, ANCHURA*ZOOM - self.game.USUARIO.size)
            self.game.USUARIO.cambiar_direccion([1,0])
        if keys[pygame.K_KP4]:
            new_pos[0] =  max(new_pos[0] - self.game.USUARIO.velocidad, 0)
            self.game.USUARIO.cambiar_direccion([-1,0])
        if keys[pygame.K_KP8]:
            new_pos[1] = max(new_pos[1] - self.game.USUARIO.velocidad, 0)
            self.game.USUARIO.cambiar_direccion([0,-1])
        if keys[pygame.K_KP5]:
            new_pos[1] = min(new_pos[1] + self.game.USUARIO.velocidad, ALTURA*ZOOM - self.game.USUARIO.size)
            self.game.USUARIO.cambiar_direccion([0,1])
        if actual_pos != new_pos:
            self.game.USUARIO.mover(new_pos)
            if not pygame.sprite.spritecollide(self.game.USUARIO, self.game.MUROS, dokill=False):
                if pygame.sprite.spritecollide(self.game.USUARIO, self.game.COMIDA, dokill=True):
                    self.game.USUARIO.comer()
            else:
                self.game.USUARIO.mover(actual_pos)

    """
        1) if spritecollide(sprite, grupo, dokill):
            "sprite" ha colisionado con algún sprite del "grupo" 
            if dokill -> eliminamos el sprite de "grupo" correspondiente
        2) for s1, lista in groupcollide(grupo1, grupo2, dokill1, dokill2).items():
            el sprite "s1" (del grupo1) ha colisionado con los sprites de "lista" (del grupo2) 
            if dokill1 / dokill2 -> eliminamos el sprite
    """
    def colisiones(self):
        # usuario vs killer
        if pygame.sprite.spritecollide(self.game.USUARIO, self.game.KILLERS, False):
            self.game.USUARIO.die("killer")
            return False
        # usuario vs snakes
        # for snake in self.game.SNAKES:
        if pygame.sprite.spritecollide(self.game.USUARIO, self.game.SNAKES, False):
            self.game.USUARIO.die("snake")
            return False
        # colisiones con las balas
        pygame.sprite.groupcollide(self.game.BALAS, self.game.MUROS, True, False)
        for bullet, killers in pygame.sprite.groupcollide(self.game.BALAS, self.game.KILLERS, True, False).items():
            #bullet.kill()
            killers[0].get_shot()
        # for snake in self.game.SNAKES:
        for bullet, snakes in pygame.sprite.groupcollide(self.game.BALAS, self.game.SNAKES, True, False).items():
            #bullet.kill()
            snakes[0].get_shot()
        return True

    def draw_screen(self):
        # mapa y personajes
        self.screen.blit(IM_fondo, (0,0))
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        (x_camara, y_camara) = self.get_camara()
        self.window.blit(self.screen, (x_camara, y_camara))
        # numero de balas
        contador = self.font.render(f"Balas: {self.game.USUARIO.nbalas}", 0, BLANCO)
        self.window.blit(contador, (ANCHURA//2-40, 20))

    def update(self):
        # reloj.tick(fps)
        pygame.display.flip()
        #pygame.display.update()

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
            # check final del juego -> hemos ganado
            if len(self.game.SNAKES) == 0 and len(self.game.KILLERS) == 0 and count_snake == self.game.N_snakes and count_killer == self.game.N_killers:
                level_done = True
                run = False
            # crear más comida
            if len(self.game.COMIDA) < 4: self.make_food()
            time = pygame.time.get_ticks() // 100
            # cada X tiempo... interaccionar con los enemigos
            if time == tiempo_aux:
                tiempo_aux += 1
                # mover enemigos
                self.move_enemies(tiempo_aux)
                # crear más enemigos
                if tiempo_aux % 100 == 0:
                    if count_snake < self.game.N_snakes:
                        count_snake += 1
                        snake = P.Snake(random.choice(self.game.inicio_enemy))
                        self.game.SNAKES.add(snake)
                        self.all_sprites.add(snake)
                    if count_killer < self.game.N_killers:
                        count_killer += 1
                        killer = P.Killer(random.choice(self.game.inicio_enemy))
                        self.game.KILLERS.add(killer)
                        self.all_sprites.add(killer)
            # check key events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bala = self.game.USUARIO.disparar()
                        if bala != None: 
                            self.game.BALAS.add(bala)
                            self.all_sprites.add(bala)
            # mover usuario
            self.move_user()
            run = run and self.colisiones()
            self.draw_screen()
            self.update()
        # fin de nivel 
        if not quit:
            run2 = True
            if level_done: 
                boton_level_completed.draw(self.window)
            else: 
                boton_lose.draw(self.window)
            self.update()
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


if __name__ == "__main__":
    display = Display()
    display.jugar()