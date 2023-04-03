# Juego-Laberinto-Versiones

Se trata de un personaje *User* que se mueve por un mapa y tiene que eliminar a dos tipos de enemigos. Las serpientes *Snake* y los fantasmas *Killer*. Cada uno tiene su vida correspondiente. El personaje dispara con el *espacio* y se mueve con las teclas *4,5,6,8*. 

## Versión 0

- Los personajes son clases creadas desde cero, pero luego el juego y el display se mueve todo por funciones.
- Tanto el *Killer* como el *Snake* se mueven con un algoritmo de busqueda (Dikstra) hasta la posición del jugador y comida respectivamente.

## Versión 1

- Los personajes siguen siendo clases creadas desde cero, pero para el juego y el display se crean clases maás organizadas.

## Versión 2

- Cambio considerable en los personajes. Comienzan a heredar de la clase *pygame.sprite.Sprite*.
- En el *Game* los personajes se añaden en grupos *pygame.sprite.Group*. Así las actualizaciones son más dinámicas y las colisiones más organizadas.
- Queda algún fallo en la visualización de la serpiente. En la siguiente se arregla viendo que falta agregar la primera parte de la serpiente al *self.all_sprites*.

## Versión 3

- Se hacen cambios en la serpiente. Se arregla su visualización y además se distingue cabeza y cuerpo, cada una con un sprite / imagen diferente. 
- Se añaden niveles a los objetos *self.power*, cada nivel tiene distintas imagenes:
    - Serpiente (actualmente 2): Cuanto más nivel más difícil de eliminarla.
    - Comida (altualmente 2): Cuanto más nivel más nº de balas le da al usuario.

