#Andres Hernandez Alvarado A01798208
import os
import random
import time
from art import *

red = '\033[91m'
lred = '\033[1;31m'
blue = '\033[94m'
lblue = '\033[1;34m'
white = '\033[1;37m'
green = '\033[32m'
C_RESET = '\033[0m'
player1 = [7,2,8, 'Jugador 1', lblue,blue,0]
player2 = [9,3,10,'Jugador 2', lred, red,0]
e_flag = [1, 'Empty Flag', white]
upper = 4
lower = 5
DEFAULT_GRAPHICS = """/// 0 - vacio | 2 - flag  4 - Upper limit  5 - Lower limit  7 - Player 1   9 - Player 2 /// CHANGE COLORS OF FLAG DEPENDING ON PLAYER
│   │
│ ⚐ │
│ ⚐ │
| ⚐ |
┌───┐
└───┘
------6
│ ♔ │
│ ⚑ │
│ ♚ │
│ ⚑ │

"""
#RESET TERMINAL /////////////////////////////////////////////////////////////////
def clear_terminal():                       #LIMPIA LA TERMINAL
    os.system("cls" if os.name == "nt" else "clear")
clear_terminal()

def reset_tab(matrix):        #COMANDO QUE LIMPIA LA TERMINAL Y REIMPRIME EL TABLERO
    clear_terminal()
    graphics = creategraphics()
    matrix_graphics(matrix, graphics)

#CREAR ARCHIVO DE TABLERO Y TABLERO /////////////////////////////////////////////
def ensuregraphics(path = 'graphics.txt'):  
    print('Generando graficos...')
    with open(path, 'w', encoding="utf-8") as cells:
        cells.write(DEFAULT_GRAPHICS)
#GUARDAR JUEGO
def savegame(matrix,count,l, filename="savedgame.txt"):
    pass  
    with open(filename, "w") as f:
        for row in matrix:
            f.write(','.join(str(x) for x in row) + "\n")
        f.write(f't={count}'+'\n')
        f.write(f'l={l}')
    
#CONTINUAR JUEGO
def loadgame():
    matrix=[]
    with open('../savedgame.txt', 'r') as f:
        for line in f:
            if "," in line:  # part of the matrix
                matrix.append([int(g) for g in line.split(",")])
            elif line.startswith("t="):
                count = int(line.split("=")[1])
            elif line.startswith("l="):
                l = int(line.split("=")[1])
        f.seek(0)
        n = len(f.readline())

    return matrix, n, count,l

def crear_tablero(size):    #CREA LA MATRIZ QUE DESCRIBE AL TABLERO
    tablero = []       
    for _ in range(size):
        tablero.append([])
        for x in range(size):
            tablero[_].append(0)
    return tablero


#Lee el archivo de los graphicos linea por linea y lo guarda en una matriz. Donde la matriz se basa en la matriz que describe al juego para generar los graficos
def creategraphics():       
    with open("graphics.txt", 'r', encoding ="utf-8") as cell:
        for line in cell:
            graphics = [line.rstrip("\n") for line in cell]
        return graphics
    
#Dibuja el tablero en la terminal dependiendo de la matriz y los graficos.    
def matrix_graphics(tablero, graphics):   
    for i, fila in enumerate(tablero):
        # Celda parte superior
        print("".join([graphics[upper] for _ in fila]))
        row_out = []
        #Color a grafico dentro de la celda
        for j, celda in enumerate(fila):
            cell_graphic = graphics[celda]                          #Separar simbolo dentro de celda
            left = cell_graphic[0]                 
            mid = cell_graphic[1:-1]               
            right = cell_graphic[-1]                
            symbol = mid.strip()
            if celda == player1[0]:                                 #J1 - jugador 1
                symbol_colored = player1[4] + symbol + C_RESET
            elif celda == player2 [0]:                              #J2 - jugador 2
                symbol_colored = player2[4] + symbol + C_RESET
            elif celda == e_flag[0]:                                #bandera vacia
                symbol_colored = e_flag[2] + symbol + C_RESET
            elif celda == player1[1]:                               #bandera 1
                symbol_colored = player1[4] + symbol + C_RESET
            elif celda == player2[1]:                               #bandera 2
                symbol_colored = player2[4] + symbol + C_RESET
            elif celda == player1[2]:                               #J1 + bandera1
                symbol_colored = player1[5] + symbol + C_RESET
            elif celda == player2[2]:                               #J2 + bandera2
                symbol_colored = player2[5] + symbol + C_RESET
            else:
                symbol_colored = " "                                #Celda vacia

            mid_colored = " " + symbol_colored + " "                #Crear contenido interno de celda a partir de simbolo con color

            row_out.append(left + mid_colored + right)              #Crear una matriz del la celda del medio

        print("".join(row_out))                                     #Imprimir matriz del texto (Celda media)
        # Celda parte inverior
        print("".join([graphics[lower] for _ in fila]))             #Imprimir parte inferior de la celda


#SET PLAYER POSITIONS AND RANDOM FLAGS/////////////////////////////////

#Coloca a los jugadores dentro del tablero y a las banderas en posiciones aleatorias
def set_tablero(n):                                                    
    matrix = crear_tablero(n)
    matrix[0][0] = player1[0]
    matrix[-1][-1] = player2[0]
    placed_f = 0
    l = 0
    while l<n:
        l = n//2 + (n-random.randrange(1,n))
    while placed_f < l:
        r = random.randrange(n)
        c = random.randrange(n)
        if matrix[r][c] == 0:
            matrix[r][c] = e_flag[0]
            placed_f += 1        
    return matrix,l

#PLAYER TURN LOGIC////////////////////////////////////////////////////////////////////
def player_turn(matrix, count,n):
    mensaje = ""
    for p_marker in (player1,player2):
        reset_tab(matrix)
        
        print(f'Turno {count}/{n} de {p_marker[5] + p_marker[3]+C_RESET} ')
        input("Tirar dado - (Enter para continuar)") 
        dado = random.randrange(1,7)
        input(f"¡Tiraste un {green + str(dado) + chr(0x267F +dado) + C_RESET}!") #Usando el UNICODE (U+2680–U+2685) para mostrar el símbolo ⚀–⚅ del dado. :D
        for g in range(dado):    
            i, j = player_position(matrix,p_marker[0])
            if i == -1:
                print("Jugador no encontrado")
                break
            moved = False
            while not moved:
                reset_tab(matrix)
                print(red + mensaje.upper() + C_RESET)
                print(f'Turno {count}/{n} de {p_marker[5] + p_marker[3]+C_RESET}.     Movimientos restantes: {green + str(dado-g) + C_RESET}')
                move = (input("Moverse. \n (w - arriba)(s - abajo)(a - izquierda)(d - derecha): ").lower())
                if move not in ("w", "a", "s", "d"):
                    mensaje = "Input Invalido"
                    continue
                #BOTONES PARA MOVIMIENTO (INPUTS)
                if move == "w":
                    ni,nj = i-1,j
                elif move == "a":
                    ni,nj = i,j-1
                elif move == "s":
                    ni,nj = i+1,j
                elif move == "d":
                    ni,nj = i,j+1
                #INPUT INVALIDO DE MOVIMIENTO
                mensaje = ""
                #OUT OF BOUNDS
                if not (0<=ni < len(matrix) and 0 <=nj < len(matrix[0])):
                    mensaje = "Movimiento fuera del tablero"
                    continue
                #COLISION ENTRE JUGADORES
                dest = matrix[ni][nj]
                defender = player1 if p_marker == player2 else player2

                if dest in(defender[0] , defender[2]):  # Player standing on a flag
                    mensaje = (f"Movimiento no posible / Posicion ocupada por {defender[3]}")
                    continue
                
                # INTERACCION CON BANDERAS

                if matrix[i][j] == p_marker[2]:       # J + bandera
                    if dest == (defender[1]):  # Combat with opponent
                        winner, loser = combatlogic(p_marker, defender)
                        if winner == p_marker:
                            matrix[ni][nj] = p_marker[2] 
                            matrix[i][j] = p_marker[1] 
                    elif dest == 0:                       # Vacío
                        matrix[ni][nj] = p_marker[0]
                        matrix[i][j] = p_marker[1]
                    elif dest == p_marker[1]:             # Propia bandera
                        matrix[ni][nj] = p_marker[2]
                        matrix[i][j] = p_marker[1]
                    elif dest == e_flag[0]:               # Bandera vacía
                        matrix[ni][nj] = p_marker[2]
                        matrix[i][j] = p_marker[1]

                elif matrix[i][j] == p_marker[0]:     # Jugador solo
                    if dest == (defender[1]):  # Combat with opponent
                        winner, loser = combatlogic(p_marker, defender)
                        if winner == p_marker:
                            matrix[ni][nj] = p_marker[2]
                            matrix[i][j] = 0

                    elif dest == 0:                       # Vacío
                        matrix[ni][nj] = p_marker[0]
                        matrix[i][j] = 0
                    elif dest == p_marker[1]:             # Propia bandera
                        matrix[ni][nj] = p_marker[2]
                        matrix[i][j] = 0
                    elif dest == e_flag[0]:               # Bandera vacía
                        matrix[ni][nj] = p_marker[2]
                        matrix[i][j] = 0
                

                reset_tab(matrix)
                moved = True

    return matrix

def combatlogic(attacker, defender):
    hp_a, hp_d = 5, 5

    while hp_a > 0 and hp_d > 0:
        clear_terminal()
        print(f"⚔️ Combate: {attacker[5] + attacker[3] + C_RESET} vs {defender[5] + defender[3] + C_RESET}")
        print_lives(defender[5] + defender[3] + C_RESET, hp_d, 5)
        print_lives(attacker[5] + attacker[3] + C_RESET, hp_a, 5)
        print("\n")

        # Turno del atacante
        input(attacker[5] + "El atacante tira un dado" + C_RESET + '\n(Enter para tirar)')
        roll_a = random.randint(0, 3)
        print(f"{attacker[5] + attacker[3] + C_RESET} realiza {roll_a} de daño a {defender[5] + defender[3] + C_RESET}")
        hp_d -= roll_a
        if hp_d < 0:
            hp_d = 0
        time.sleep(1)

        clear_terminal()
        print(f"⚔️ Combate: {attacker[5] + attacker[3] + C_RESET} vs {defender[5] + defender[3] + C_RESET}")
        print_lives(defender[5] + defender[3] + C_RESET, hp_d, 5)
        print_lives(attacker[5] + attacker[3] + C_RESET, hp_a, 5)
        print("\n")

        if hp_d <= 0:
            break

        # Turno del defensor
        input(defender[5] + "El defensor tira un dado" + C_RESET + '\n(Enter para tirar)')
        roll_d = random.randint(0, 3)
        print(f"{defender[5] + defender[3] + C_RESET} realiza {roll_d} de daño a {attacker[5] + attacker[3] + C_RESET}")
        hp_a -= roll_d
        if hp_a < 0:
            hp_a = 0
        time.sleep(1)

        clear_terminal()
        print(f"⚔️ Combate: {attacker[5] + attacker[3] + C_RESET} vs {defender[5] + defender[3] + C_RESET}")
        print_lives(defender[5] + defender[3] + C_RESET, hp_d, 5)
        print_lives(attacker[5] + attacker[3] + C_RESET, hp_a, 5)
        print("\n")

    # Resultado final
    clear_terminal()
    print(f"⚔️ Resultado del combate:")
    print_lives(defender[5] + defender[3] + C_RESET, hp_d, 5)
    print_lives(attacker[5] + attacker[3] + C_RESET, hp_a, 5)
    print("\n")

    if hp_a > 0:
        print(f"{attacker[5] + attacker[3] + C_RESET} gana el combate!")
        return attacker, defender
    else:
        print(f"{defender[5] + defender[3] + C_RESET} gana el combate!")
        return defender, attacker

def print_lives(player_name, hp, max_hp):               #Display de cantidad de vida durante situacion de combate
    full = '❤'
    empty = '♡'
    hearts = full * hp + ' ' + empty * (max_hp - hp)
    print(f"{player_name}: {hearts}")

#COUNT FLAGS CAPTURED               Contar las banderas tomadas por cada jugador
def countpoints(matrix,p1,p2):
    p1 = 0
    p2 = 0
    for row in matrix:
        for val in row:
            if val == player1[1] or val == player1[2]:
                p1+=1
            elif val == player2[1] or val == player2[2]:
                p2+=1
    return p1, p2

def player_position(matrix, p_num):                 #Leer la posicion actual del jugador
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val in (player1[0], player1[2]):     #Celda contiene marca del jugador 1 (pos o bandera marcada)
                if p_num in (player1[0], player1[2]):
                    return i, j
            elif val in (player2[0], player2[2]):     #Celda contiene marca del jugador 2 (posicion o en bandera)
                if p_num in (player2[0], player2[2]):
                    return i, j
    return -1, -1

def loading_bar(text:str)->None:
    """
    It makes a loading bar animation, it is colored
    and made to look cool!

    It uses the same ANSI standard color codes we use
    throughout all of the game.

    █▒▒▒▒▒▒▒▒▒ how it might look like ...


    """
    lbar = '██'
    rbar = '▒▒'
    for i in range(10):
        bar = f"| {green}{lbar*(i)}{red}{rbar*(10-i)}{C_RESET} |"
        out = f"{text.center(50)} {((i+1)%4)*'.'}"
        print(f"{out}\n\n {bar.center(60)} {i*10} %")
        time.sleep(0.2)
        clear_terminal()

def loading_screen()->None:
    clear_terminal()

    loading_bar("Cargando archivo")
    loading_bar("Generando gráficos")
    loading_bar("Preparando juego")

    clear_terminal()

    print("¡Listo!".center(60)); time.sleep(1)

def title_screen()->None:

    x = [red, blue, green]
    for i in range(10):

        print(x[i%3])
        print((10-i)*"\n")
        tprint("Flag ", font="twisted")
        print(C_RESET)
        time.sleep(0.2)
        clear_terminal()

def instrucciones():
    
    with open("../README.txt", "r") as f:

        lines = [x for x in f.readlines()]
        
        # todo el capítulo 2!

        for i in range(58,90):

            print(lines[i], end="")

            time.sleep(0.1)

            if (i-57)%10==0:
                time.sleep(1)
                while not bool(input("Enter ==>\t")):
                    clear_terminal()
                    break


def main():
    ensuregraphics()
    clear_terminal()

    title_screen()


    print("Instrucciones: "); instrucciones()
    while True:
        continue_newgame = input("Continue / New Game: ").upper().replace(" ", "")
        if continue_newgame == "NEWGAME":
            dificultad = str(input("Dificultad:\n (Facil - 1)   (Normal - 2)    (Dificil - 3): "))
            count = 1

            loading_screen()

            if dificultad == "1":
                n = 5
                matrix,l = set_tablero(n)
                break
            elif dificultad == "2":
                n = 10
                matrix,l = set_tablero(n)
                break
            elif dificultad == "3":
                n = 15
                matrix,l = set_tablero(n)
                break
            else:
                print("Input Invalido")
        elif continue_newgame == "CONTINUE":
            #CREAR MATRIZ A PARTIR DEL ARCHIVO GUARDADO
            matrix,n,count,l = loadgame()
            
            loading_screen()
            break
        else:
            print("Input Invalido")

    clear_terminal()
    while ((player1[6] or player2[6]) < l) and count <= n:
        matrix = player_turn(matrix, count,n)
        player1[6], player2[6] = countpoints(matrix, player1[6], player2[6]) 
        count +=1
        savegame(matrix, count,l)

    print(f"Puntos:\n{player1[5] + player1[3] + C_RESET}: {player1[6]}\n{player2[5] + player2[3] + C_RESET}: {player2[6]}")
    if player1[6] != player2[6]:
        winner = player1 if player1[6] > player2[6] else player2 
        print(f"El ganador fue - {winner[5] + winner[3] + C_RESET}")
    else:
        print(f"Empate")
    time.sleep(3)



while True:
    main()
    if input("¿Volver a jugar? (y/n): ").upper() == ("N" or "NO"):
        break
    else:
        print("")