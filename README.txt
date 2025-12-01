   _____    __         _____      ______       ___ __   
 /\_____\  /\_\       /\___/\    /_/\___\     /___ \ \  
( (  ___/ ( ( (      / / _ \ \   ) ) ___/         ) ) ) 
 \ \ \_    \ \_\     \ \(_)/ /  /_/ /  ___       / / /  
 / / /_\   / / /__   / / _ \ \  \ \ \_/\__\      \ \ \  
/ /____/  ( (_____( ( (_( )_) )  )_)  \/ _/       ) ) ) 
\/_/       \/_____/  \/_/ \_\/   \_\____/         \/_/  

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(FLAG) es un juego de terminal construido en python para la
versión 3.11 ...

                        INSTALACIÓN
                        ===========

1.- Instala python 3.11, puede ser tanto a través del sitio
    oficial de Python o de un gestor de paquetes:

    En linux, se puede buscar el paquete  "python@3.11",  y
    en windows o macos es similar si se  usan  gestores  de
    paquetes... Ese paso no lo describo más, hay  mucho  de
    esto en internet :)

2.- INSTALAR EL PAQUETE "art" con PyPi:

    Si tu instalación de python 3.11 tiene su  PIP,  puedes
    usar el siguiente script en tu terminal:

    $ pip install art

    Si usas una interfaz  gráfica,  selecciona  el  paquete
    art.

    Es necesaria esta dependencia para algunos detalles  en
    que el juego genera texto con arte ASCII. Solo  es  por
    que le añade un valor estético interesante, si bien  no
    es una dependencia indispensable.

3.- Copiar en  tu  directorio  de  preferencia  el  archivo
    main.py.

    Con esto solo, ya puedes tener el juego con  todas  sus
    características. Ningún otro archivo más es requerido.
    :)

                        INSTRUCCIONES
                        =============

1.- Elegir entre  un  juego  nuevo  o  continuar  un  juego
    pausado anteriormente.

    Para eso, escribir en la terminal  "New  game"  o  bien
    "Continue".  No  es  sensible  a  mayúsculas,  así  que
    mientras las palabras estén bien escritas, será más que
    suficiente.

2.- Luego de esto, el juego es iniciado...
                        ..__.
                        ||  |
                    .__//|  |
    2.1.- Presiona || Enter |  para lanzar un dado...
                   ||_______|
                 ./////////: 
    
    2.2.- Con este dado se determinará la cantidad de pasos
    que puedes dar con tu turno actual...

    2.3.- Movimiento:

            ._____._____._____.                 ^
           /|     | w   |     |                 |
           ||____:|____:|____:|                 w
           :/__._/___._/___._/___.       < - a     d - >
              /| a   | s   | d   |              s
              ||____:|____:|____:|              |
              :/__._/___._/___._/               v

        Ingresa (w,a,s,d) en la terminal y después presiona
               ..__.
               ||  |
           .__//|  |
          || Enter | . Cualquier otra entrada es inválida.
          ||_______|
        ./////////: 
    
    2.4.- Tu turno se  termina  hasta  que  se  termine  tu
    número de movimientos, entonces el siguiente turno será
    para el otro jugador. Y la dinámica se repite :D

3.- Banderas.

    Al principio  del  juego,  el  tablero  tiene  banderas
    vacías, las cuales se pueden reclamar si uno de los dos
    jugadores entra en la casilla con dicha bandera.

    3.1.- Banderas ocupadas.

    Una vez en la casilla, la bandera se  reclama  para  el
    jugador que la toma primero. Pero si el oponente  llega
    a la misma bandera ya ocupada, un combate ocurre.

4.- Combate.

    El combate ocurre cuando un jugador atacante atraviesa
    una bandera ocupada ya por un jugador defensor.

    Cuando esto ocurre, el juego entra en modo combate,  el
    cual consiste en una lucha por turnos decidida  por  un
    lanzamiento de dado, que decide cuánto daño se causan.

    Ambos jugadores comienzan con 5 corazones  de  vida,  y
    por cada  dado  lanzado  el  jugador  inflige  daño  al
    oponente, y viceversa, mientras sigan los turnos.

    El turno de combate solo termina hasta que uno  de  los
    dos jugadores se quede sin corazones. En  ese  momento,
    se cierra el modo combate y dependiendo  el  resultado,
    puede ocurrir que:

        - Si el atacante gana, se apodera de la bandera.

        - Si el defensor gana, el atacante regresa a su
        posición anterior.
    
    Luego de esto, el jugador atacante sigue con su  turno,
    si aún tiene movimientos, si no,  sigue  el  turno  del
    otro jugador.

5.- Salir y autoguardado.

    Para   detener   el  juego,  ejecuta  el  comando  para
    suspender tarea desde tu sistema operativo:
    
    / por ejemplo /:

     .________.       ._____.
    /| cmd  * |   +  /| z   |
    ||_______:|      ||____:|
    :/_____._/_      :/__._/_       en macos, con zsh...

    Y eso es todo, el juego está en pausa. Para volver al
    juego, solo basta con volver a ejecutar main.py.

    Con cada movimiento, el juego escribe el estado del
    juego en el fichero / savedgame.txt / .

6.- Fin

    El juego termina hasta que se agotan  los  turnos  para
    ambos jugadores.

    - Gana el jugador con más banderas.
    - Si ambos tienen la misma cantidad, es un empate.