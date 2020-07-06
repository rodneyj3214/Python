# Funciones: Secuencia de comandos que realizan un computo
# Para definirlas se utiliza el keyword def

# Programa para crear un cuadrado mediante funciones
import turtle as TK

def main():
    my_window = TK.Screen() #Abrimos una nueva ventana
    dave = TK.Turtle() #Generamos una tortuga
    
    make_square(dave) #Llamamos a la funcion hacer cuadrado
    
  #  TK.mainloop() #Mantenemos nuestra ventana activa posterior al dibujo
    
def make_square(dave):
    length = int(input('Ingresa el tamaño del cuadrado: '))
    
    #Generamos cuatro veces la funcion para crear y girar lineas
    for i in range(4): #Funcion range que permite generar una serie de valores
        make_line_and_turn(dave, length)
        
        
def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)

