#Programita para adivinar el numero con funcion while. EXTRA: Que el numero sea al alzar, pregunte al usuario si desea seguir jugando.
from random import randrange

input_valido = True

def Juego():
    print('-' * 30,'Adivina el numero del 0 al 30!','-' * 30 , sep='\n')
    print('Solo tienes 5 Oportunidades para adivinar el numero correctamente!')
    cuenta_oportunidades = 0
    numero_magico = randrange(30)
    oportunidades = 5

    while cuenta_oportunidades < oportunidades:
        try:
            respuesta = int(input('Esta es tu oportunidad ' + str(cuenta_oportunidades+1) + '/5. ' + 'Adivina el numero!: '))                                                      #De esta forma se cambia un valor a otro, desde la misma linea.
        except ValueError:
            print("Porfavor, escribe un numero.")
        cuenta_oportunidades += 1
        if respuesta == numero_magico:
            print('\n','Felicidades! Has acertado el numero correctamente! El numero era', + numero_magico )
            VolverJugar()
        if respuesta == int('777'):
            print('Asi que quieres chepia eh? Muy bien.... el numero es', numero_magico,'.')
        elif cuenta_oportunidades < 5:
            print('Error! Prueba de Nuevo.')
    else:
        print('Error!')

    print('\n','No has acertado! El numero era', + numero_magico, '. ( ‾ʖ̫‾)')
    VolverJugar()


def VolverJugar():
    nuevo_juego = (input('Quieres intentarlo de nuevo? Si/No: ')).lower()
    if nuevo_juego == 'si':
        Juego()
    if nuevo_juego == 'no':
        print('Muy Bien. Vuelve pronto!')
        exit()
    else:
        print('\n','No se lo que quisisite decir. Solo entiendo Si o No! ')
        VolverJugar()

while input_valido == True:
    Juego()
