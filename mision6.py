#Autor: Mariana Coria Rodríguez, A01374765
#Dibujar un espirografo

#importar pygae
import pygame   # Librería de pygame
import math


# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(R,r,l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)


        radio = 100
        k = r/R
        for angulo in range(0, 360 * r//math.gcd(r, R)):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(R*((1-k)*math.cos(a)+l*k*math.cos((1-k)/k*a)))
            y = int(R*((1-k)*math.sin(a)-l*k*math.sin((1-k)/k*a)))
            pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 1)




        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    R= int(input("Escribe el radio mayor: "))
    r=int(input("Escribe el radio menor: "))
    l= float(input("Escribe el valor de l: "))
    dibujar(R, r, l)


# Llamas a la función principal
main()