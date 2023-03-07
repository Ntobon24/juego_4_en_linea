class CuatroEnLinea:
    def __init__(self):
        self.tablero = []
        self.columnas = 0
        self.filas = 0
        self.turno = 1
        self.puntaje_jugador1 = 0
        self.puntaje_jugador2 = 0
        self.ganadores_previos = []

    def crear_tablero(self):
        while True:
            try:
                filas = int(input("Ingrese la cantidad de filas del tablero (4-6): "))
                if 4 <= filas <= 6:
                    break
                else:
                    print("La cantidad de filas debe ser entre 4 y 6. Intente de nuevo.")
            except:
                print("Debe ingresar un número entero. Intente de nuevo.")

        while True:
            try:
                columnas = int(input("Ingrese la cantidad de columnas del tablero (4-6): "))
                if 4 <= columnas <= 6:
                    break
                else:
                    print("La cantidad de columnas debe ser entre 4 y 6. Intente de nuevo.")
            except:
                print("Debe ingresar un número entero. Intente de nuevo.")

        self.filas = filas
        self.columnas = columnas
        self.tablero = [[" " for _ in range(columnas)] for _ in range(filas)]

    def mostrar_tablero(self):
        print("\n   " + "  ".join(str(i) for i in range(1, self.columnas + 1)))
        print(" +" + "---" * self.columnas + "+")
        for fila in self.tablero:
            print(" | " + " | ".join(fila) + " |")
            print(" +" + "---" * self.columnas + "+")

    def soltar_pieza(self, columna, jugador):
        for fila in range(self.filas - 1, -1, -1):
            if self.tablero[fila][columna] == " ":
                self.tablero[fila][columna] = "X" if jugador == 1 else "O"
                return True
        return False

    def verificar_ganador(self, fila, columna):
        if self.tablero[fila][columna] == " ":
            return False

        jugador = self.tablero[fila][columna]
        contador = 0

        # Verificar fila
        for c in range(self.columnas):
            if self.tablero[fila][c] == jugador:
                contador += 1
                if contador == 4:
                    return True
            else:
                contador = 0

        # Verificar columna
        contador = 0
        for f in range(self.filas):
            if self.tablero[f][columna] == jugador:
                contador += 1
                if contador == 4:
                    return True
            else:
                contador = 0

        # Verificar diagonal ascendente
        contador = 0
        for f, c in zip(range(fila, -1, -1), range(columna, -1, -1)):
            if self.tablero[f][c] == jugador:
                contador += 1
                if contador == 4:
                    return True
            else:
                contador = 0
        for f, c in zip(range(fila + 1, self.filas), range(columna + 1, self.columnas)):
            if self.tablero[f][c] == jugador:

                contador += 1
                if contador == 4:
                    return True
            else:
                contador = 0

                # Verificar diagonal descendente
            contador = 0
            for f, c in zip(range(fila, self.filas), range(columna, -1, -1)):
                if self.tablero[f][c] == jugador:
                    contador += 1
                    if contador == 4:
                        return True
                else:
                    contador = 0
            for f, c in zip(range(fila - 1, -1, -1), range(columna + 1, self.columnas)):
                if self.tablero[f][c] == jugador:
                    contador += 1
                    if contador == 4:
                        return True
                else:
                    contador = 0

            return False

    def jugar(self):
        print("\n¡Bienvenido al juego Cuatro en Línea!\n")

        while True:
            self.crear_tablero()
            self.mostrar_tablero()
            while True:
                try:
                    columna = int(input(f"Jugador {self.turno}: Elija una columna (1-{self.columnas}): ")) - 1
                    if columna < 0 or columna >= self.columnas:
                        print(f"La columna debe ser un número entre 1 y {self.columnas}. Intente de nuevo.")
                        continue
                    if self.soltar_pieza(columna, self.turno):
                        if self.verificar_ganador(
                                self.tablero.index([fila for fila in self.tablero if fila[columna] != " "][0]),
                                columna):
                            print(f"\n¡Felicidades! ¡Jugador {self.turno} ha ganado!\n")
                            if self.turno == 1:
                                self.puntaje_jugador1 += 1
                            else:
                                self.puntaje_jugador2 += 1
                            break
                        if all(" " not in fila for fila in self.tablero):
                            print("\n¡Empate!")
                            break
                        self.turno = 1 if self.turno == 2 else 2
                        self.mostrar_tablero()
                    else:
                        print("La columna está llena. Elija otra columna.")
                except:
                    print("Debe ingresar un número entero. Intente de nuevo.")

            if self.puntaje_jugador1 > 0 and self.puntaje_jugador1 == self.puntaje_jugador2:
                self.puntaje_jugador1 *= 3
            elif self.puntaje_jugador2 > 0 and self.puntaje_jugador2 == self.puntaje_jugador1 - 1:
                self.puntaje_jugador2 *= 3
            print(f"Puntaje del Jugador 1: {self.puntaje_jugador1}")
            print(f"Puntaje del Jugador 2: {self.puntaje_jugador2}")
            respuesta = input("¿Desea jugar de nuevo? (S/N): ")
            if respuesta.lower() != "s":
                break


juego = CuatroEnLinea()

juego.jugar()
