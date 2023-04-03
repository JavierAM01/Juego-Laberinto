import pygame 
import mapas as M
import personajes as P
import random
import os
from constantes import *


# nivel del mapa 
MUROS = M.mapa1
inicio_usuario = M.c1_usuario
inicio_killer = M.c1_killer
inicio_snake = M.c1_snake

# crear personajes
BALAS = []
COMIDA = []
SNAKES, KILLERS = [P.Snake(inicio_snake)], [P.Killer(inicio_killer)]
usuario = P.Usuario(inicio_usuario)

# caracteristicas de los personajes
usuario_vel = 1
N_snake = 3   # número de personajes
N_killer = 6
VEL_snake = 3  # cuanto menos más rapido (es cada cuanto tiempo se actualiza)
VEL_killer = 6

# inicio del juego
pygame.init()
pantalla = pygame.display.set_mode((ANCHURA, ALTURA))
pygame.display.set_caption("Nivel 1")
fuente = pygame.font.Font(None, 30)
reloj = pygame.time.Clock()
fps = 100

def zoom(pos_usuario):
    x, y = pos_usuario[0]-ANCHURA/(ZOOM*2), pos_usuario[1]-ANCHURA/(ZOOM*2)
    lim_superior = ANCHURA - ANCHURA/ZOOM
    if x < 0: x = 0
    elif  x > lim_superior: x = lim_superior
    if y < 0: y = 0
    elif  y > lim_superior: y = lim_superior
    def transformar(pos): 
        return  [ZOOM*(pos[0]-x), ZOOM*(pos[1]-y)]
    return transformar

def make_food():
    done = False
    while not done:
        pos = [DIM*random.randint(0,NX-1), DIM*random.randint(0,NY-1)]
        if pos not in MUROS and pos[0] >= 0 and pos[0] < ANCHURA and pos[1] >= 0 and pos[1] < ALTURA:
            done = True
            COMIDA.append(pos)

def mover_personajes(tiempo_aux):
    # snakes
    if tiempo_aux % VEL_snake == 0:
        for snake in SNAKES:
            if len(COMIDA) > 0:
                if snake.esta_vivo():
                    l = snake.mover(COMIDA, MUROS)
                    if l != []: 
                        COMIDA.remove(l)
    # killers
    if tiempo_aux % VEL_killer == 0:
        for killer in KILLERS:
            if killer.esta_vivo():
                killer.mover(cuadrar_coordenada(usuario.get_pos()), MUROS)

def mover_usuario():
    keys = pygame.key.get_pressed()
    new_pos = usuario.get_pos()
    if keys[pygame.K_KP6]:
        new_pos[0] += usuario_vel
        usuario.cambiar_direccion([1,0])
    if keys[pygame.K_KP4]:
        new_pos[0] -= usuario_vel
        usuario.cambiar_direccion([-1,0])
    if keys[pygame.K_KP8]:
        new_pos[1] -= usuario_vel
        usuario.cambiar_direccion([0,-1])
    if keys[pygame.K_KP5]:
        new_pos[1] += usuario_vel
        usuario.cambiar_direccion([0,1])
    [pos1, pos2, pos3, pos4] = conseguir_esquinas(new_pos)
    if pos1 not in MUROS and pos2 not in MUROS and pos3 not in MUROS and pos4 not in MUROS and pos1[0] >= 0 and pos2[0] < ANCHURA and pos1[1] >= 0 and pos3[1] < ALTURA:
        usuario.mover(new_pos)
        for c in COMIDA:
            if c in [pos1, pos2, pos3, pos4]:
                usuario.comer()
                COMIDA.remove(c)

def cuadrar_coordenada(pos):
    new_pos = [DIM*(pos[0]//DIM), DIM*(pos[1]//DIM)]
    return new_pos

def conseguir_esquinas(pos):
    pos1 = cuadrar_coordenada(pos)
    pos2 = cuadrar_coordenada([pos[0]+DIM*0.9, pos[1]])
    pos3 = cuadrar_coordenada([pos[0]+DIM*0.9, pos[1]+DIM*0.9])
    pos4 = cuadrar_coordenada([pos[0], pos[1]+DIM*0.9])
    return [pos1, pos2, pos3, pos4]

def colisiones(run):
    for snake in SNAKES:
        for snake_rect in snake.get_rect():
            if usuario.get_rect().colliderect(snake_rect):
                usuario.die()
                run = False
    for killer in KILLERS:
        if usuario.get_rect().colliderect(killer.get_rect()):
            usuario.die()
            run = False
    for bala in BALAS:
        golpeado = False
        if cuadrar_coordenada(bala.get_pos()) in MUROS: 
            BALAS.remove(bala)
            break
        for killer in KILLERS:
            if bala.rect.colliderect(killer.get_rect()):
                killer.golpear()
                BALAS.remove(bala)
                golpeado = True
                break
        if golpeado:
            break
        for snake in SNAKES:
            for snake_rect in snake.get_rect():
                if bala.rect.colliderect(snake_rect):
                    snake.golpear()
                    BALAS.remove(bala)
                    break
    return run

def draw_screen(transformar, end_level = False, level_done = False):
    pantalla.blit(IM_fondo, transformar([0,0]))
    for pos in MUROS:
        pantalla.blit(IM_muro, transformar(pos))
        #pygame.draw.rect(pantalla, COLOR_PARED, pygame.Rect(pos[0], pos[1], DIM, DIM))
    
    """
    # cuadrícula
    for i in range(NY+1): 
        pos = transformar([0, i*DIM])
        pygame.draw.rect(pantalla, GRIS, pygame.Rect(pos[0], pos[1], ZOOM*ANCHURA, 2))
    for i in range(NX+1): 
        pos = transformar([i*DIM, 0])
        pygame.draw.rect(pantalla, GRIS, pygame.Rect(pos[0], pos[1], 2, ZOOM*ALTURA))
    """
    for pos in COMIDA:
        pantalla.blit(IM_comida, transformar(pos))
    # personajes
    if usuario.esta_vivo(): usuario.actualizar(pantalla, transformar)
    for snake in SNAKES:
        if snake.esta_vivo(): snake.actualizar(pantalla, transformar)
        else: SNAKES.remove(snake)
    for killer in KILLERS:
        if killer.esta_vivo(): killer.actualizar(pantalla, transformar)
        else: KILLERS.remove(killer)
    for bala in BALAS: 
        pos = transformar([bala.get_pos()[0]+DIM//2, bala.get_pos()[1]+DIM//2])
        pygame.draw.circle(pantalla, BLANCO, (pos[0], pos[1]), ZOOM*3, ZOOM*2)
    # numero de balas
    contador = fuente.render(f"Balas: {usuario.nbalas}", 0, BLANCO)
    pantalla.blit(contador, (ANCHURA//2-40, 20))
    # botones del final
    if end_level:
        if level_done: boton_level_completed.actualizar(pantalla)
        else: boton_lose.actualizar(pantalla)
    reloj.tick(fps)
    pygame.display.flip()

def jugar():
    run = True
    tiempo_aux = (pygame.time.get_ticks()//100) + 50 # centisegundos
    count_snake = 1
    count_killer = 1
    level_done = False
    quit = False
    while run:
        if len(SNAKES) == 0 and len(KILLERS) == 0 and count_snake == N_snake and count_killer == N_killer:
            level_done = True
            run = False
        if len(COMIDA) < 4: make_food()
        for bala in BALAS: bala.actualizar()
        time = pygame.time.get_ticks() // 100
        if time == tiempo_aux:
            tiempo_aux += 1
            mover_personajes(tiempo_aux)
            if tiempo_aux % 100 == 0:
                if count_snake < N_snake:
                    count_snake += 1
                    snake = P.Snake(inicio_snake)
                    SNAKES.append(snake)
                if count_killer < N_killer:
                    count_killer += 1
                    killer = P.Killer(inicio_killer)
                    KILLERS.append(killer)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bala = usuario.disparar()
                    if bala != None: BALAS.append(bala)
        mover_usuario()
        run = colisiones(run)
        transformar = zoom(usuario.get_pos())
        draw_screen(transformar)
    # fin de nivel 
    if not quit:
        run2 = True
        temp_transformar = zoom(usuario.get_pos())
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
            draw_screen(temp_transformar, end_level = True, level_done = level_done)


if __name__ == "__main__":
    jugar()