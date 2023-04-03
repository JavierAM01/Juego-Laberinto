import pygame, os

main_path = "../../imagenes"

class Boton(pygame.sprite.Sprite):

    def __init__(self, pos, texto, tipo = 1):
        if tipo == 1: self.escala = ESCALA_BOTON
        else: self.escala = ESCALA_BOTON_MENU 
        self.imagen = pygame.transform.scale(pygame.image.load(os.path.join(main_path, "button.png")), self.escala)
        self.texto = texto
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = pos[0], pos[1]

    def get_rect(self):
        return self.rect

    def actualizar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
        texto = pygame.font.SysFont("Arial", 30).render(self.texto, 0, BLANCO)
        coordenada_texto = (self.rect.left + (self.escala[0]-texto.get_width())/2, self.rect.top + (self.escala[1]-texto.get_height())/2)
        pantalla.blit(texto, coordenada_texto)


# colores
NEGRO = (0,0,0)
BLANCO = (255,255,255 )
GRIS = (50,50,50)
AMARILLO = (255,255,0)
VERDE = (9, 217, 12)
MORADO = (150,25,200)
COLOR_PARED = (200,200,200)
AZUL = (25,25,250)
ROJO = (255,0,0)

# dimensiones
NX = 50    # nº de casillas en el eje x
NY = 50    # nº de casillas en el eje x
DIM = 15   # dimension de cada casilla del juego
ANCHURA = NX*DIM
ALTURA = NY*DIM
ZOOM = 2 # 5
ESCALA_BOTON = (250, 100)
ESCALA_BOTON_MENU = (125, 90)

# imagenes
IM_comida = pygame.transform.scale(pygame.image.load(os.path.join(main_path, "food.png")), (ZOOM*DIM, ZOOM*DIM))
IM_killer = pygame.transform.scale(pygame.image.load(os.path.join(main_path, "killer.png")), (ZOOM*DIM, ZOOM*DIM))
IM_usuario = pygame.transform.scale(pygame.image.load(os.path.join(main_path, "user.png")), (ZOOM*DIM, ZOOM*DIM))
IM_snake = pygame.transform.scale(pygame.image.load(os.path.join(main_path, "snake.jpg")), (ZOOM*DIM, ZOOM*DIM))
IM_fondo = pygame.transform.scale(pygame.image.load(os.path.join(main_path, "background.jpg")), (ZOOM*ANCHURA, ZOOM*ALTURA))
IM_muro = pygame.transform.scale(pygame.image.load(os.path.join(main_path, "wall.jpg")), (ZOOM*DIM,ZOOM*DIM))

# botones
boton_level_completed = Boton([ANCHURA/2-100, ALTURA/2-50], "Level Completed!")
boton_lose = Boton([ANCHURA/2-100, ALTURA/2-50], "You lose!")


