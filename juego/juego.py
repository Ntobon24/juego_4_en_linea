j1= input("ingrese el nombre del jugador 1")
j2= input("ingrese el nombre del jugador 2")

class Tablero:
    def __init__(self,tamaño):
        self.tamaño = tamaño
        self.tablero = [['.' for j in range(size)] for i in range(size)]

    def show(self):
        for row in self.tablero:
            for cell in row:
                print(cell,end=' ')
            print()

    def update(self,x,y,token):
        self.tablero[x][y] = token

    def check_move(self,x,y):
        if x<0 or x>=self.tamaño:
            return False
        if y<0 or y>=self.tamaño:
            return False
        if self.tablero[x][y] != '.':
            return False
        return True

    def check_win(self,token):

        for row in self.tablero:
            count = 0
            for cell in row:
                if cell == token:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return True

        for j in range(self.tamaño):
            count = 0
            for i in range(self.tamaño):
                if self.tablero[i][j] == token:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return True

        for i in range(self.tamaño-3):
            for j in range(self.tamaño-3):
                if self.tablero[i][j] == token and self.tablero[i+1][j+1] == token and self.tablero[i+2][j+2] == token and self.tablero[i+3][j+3] == token:
                    return True
        for i in range(self.tamaño-3):
            for j in range(3,self.tamaño):
                if self.tablero[i][j] == token and self.tablero[i+1][j-1] == token and self.tablero[i+2][j-2] == token and self.tablero[i+3][j-3] == token:
                    return True
        return False


class Jugador:
    def __init__(self,token):
        self.token = token

    def move(self,tablero):
        while True:
            x = int(input('Ingrese el valor de la fila en rango (0-{}): '.format(tablero.tamaño-1)))
            y = int(input('Ingrese el valor de la columna en rango (0-{}): '.format(tablero.tamaño-1)))
            if tablero.check_move(x,y):
                break
            else:
                print('Movimiento inválido. Intente de nuevo.')
        tablero.update(x,y,self.token)


class Juego:
    def __init__(self,tamaño):
        self.tablero = Tablero(tamaño)
        self.jugador1 = Jugador(j1)
        self.jugador2 = Jugador(j2)

    def start(self):
        print('Bienvenido al juego 4 en línea!')
        print(f' {j1} usará X y {j2} usará O.')
        self.tablero.show()
        while True:
            self.jugador1.move(self.tablero)
            self.tablero.show()
            if self.tablero.check_win('X'):
                print(f'¡{j1}ha ganado!')
                break
            self.jugador2.move(self.tablero)
            self.tablero.show()
            if self.tablero.check_win('O'):
                print(f'¡{j2} ha ganado!')
                break


size = int(input('Ingrese el tamaño del tablero (4-10): '))


game = Juego(size)


game.start()