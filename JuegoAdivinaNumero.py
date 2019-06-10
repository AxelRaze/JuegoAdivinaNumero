from random import randrange
from Juego import *
class JuegoAdivinaNumero(Juego):
    def __init__(self, num, vidas):
        self._num = num
        self._vidas = vidas
        if (num < 0 or vidas < 0):
            self._num = 0
            self._vidas = 0

    def Juega(self):
        while self._vidas != 0:
            #print('Numero de vidas:', self._vidas)
            #print('Numero que adivinar:', self._num)
            num = int(input('Adivina el numero '))
            #print('Numero:', num)

            if (num == self._num):
                self.ActualizaRecord()
                print('¡Acertaste!  El numero era', self._num)
                break
            else:
                self.QuitaVida()
                self.ActualizaRecord()
                if self._vidas != 0:
                    if (num > self._num):
                        print('Intenta otra vez. El numero es menor a ', num)
                    if (num < self._num):
                        print('Intenta otra vez. El numero es mayor a ', num)
                else:
                    print('Fin del juego, el número a adivinar era ', self._num)