class Tablero:
    def __init__(self,tamaño):
        self.tamaño = tamaño
        self.tablero = [['.' for j in range(size)] for i in range(size)]
    #crear una función para mostrar el tablero
    def show(self):
        for row in self.tablero:
            for cell in row:
                print(cell,end=' ')
            print()
    #crear una función para actualizar el tablero
    def update(self,x,y,token):
        self.tablero[x][y] = token
    #crear una función para verificar si el movimiento es válido
    def check_move(self,x,y):
        if x<0 or x>=self.tamaño:
            return False
        if y<0 or y>=self.tamaño:
            return False
        if self.tablero[x][y] != '.':
            return False
        return True
    #crear una función para verificar si hay un ganador
    def check_win(self,token):
        #verificar si hay 4 en línea horizontal
        for row in self.tablero:
            count = 0
            for cell in row:
                if cell == token:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return True
        #verificar si hay 4 en línea vertical
        for j in range(self.tamaño):
            count = 0
            for i in range(self.tamaño):
                if self.tablero[i][j] == token:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return True
        #verificar si hay 4 en línea diagonal
        for i in range(self.tamaño-3):
            for j in range(self.tamaño-3):
                if self.tablero[i][j] == token and self.tablero[i+1][j+1] == token and self.tablero[i+2][j+2] == token and self.tablero[i+3][j+3] == token:
                    return True
        for i in range(self.tamaño-3):
            for j in range(3,self.tamaño):
                if self.tablero[i][j] == token and self.tablero[i+1][j-1] == token and self.tablero[i+2][j-2] == token and self.tablero[i+3][j-3] == token:
                    return True
        return False

#crear clase jugador
class Jugador:
    def __init__(self,token):
        self.token = token
    #crear una función para pedir al jugador que ingrese un movimiento
    def move(self,tablero):
        while True:
            x = int(input('Ingrese la fila (0-{}): '.format(tablero.tamaño-1)))
            y = int(input('Ingrese la columna (0-{}): '.format(tablero.tamaño-1)))
            if tablero.check_move(x,y):
                break
            else:
                print('Movimiento inválido. Intente de nuevo.')
        tablero.update(x,y,self.token)

#crear clase juego
class Juego:
    def __init__(self,tamaño):
        self.tablero = Tablero(tamaño)
        self.jugador1 = Jugador('X')
        self.jugador2 = Jugador('O')
    #crear una función para iniciar el juego
    def start(self):
        print('Bienvenido al juego 4 en línea!')
        print('El jugador 1 usará X y el jugador 2 usará O.')
        self.tablero.show()
        while True:
            self.jugador1.move(self.tablero)
            self.tablero.show()
            if self.tablero.check_win('X'):
                print('¡El jugador 1 ha ganado!')
                break
            self.jugador2.move(self.tablero)
            self.tablero.show()
            if self.tablero.check_win('O'):
                print('¡El jugador 2 ha ganado!')
                break

#pedir al usuario que ingrese el tamaño del tablero
size = int(input('Ingrese el tamaño del tablero (4-10): '))

#crear una instancia del juego
game = Juego(size)

#iniciar el juego
game.start()