

class Personaje:
    """
    Representa un personaje en el juego TalanaKombat.

    Attributes:
        nombre (str): El nombre del personaje.
        energia (int): La energía inicial del personaje (por defecto 6).
        movimientos_especiales (dict): Un diccionario que mapea combinaciones de movimientos y golpes a nombres de ataques especiales y sus respectivos daños.
    """

    def __init__(self, nombre, energia=6):
        """
        Inicializa un nuevo objeto Personaje.

        Args:
            nombre (str): El nombre del personaje.
            energia (int, optional): La energía inicial del personaje. Por defecto es 6.
        """
        self.nombre = nombre
        self.energia = energia
        self.movimientos_especiales = {}

    def recibir_danio(self, danio):
        """
        Reduce la energía del personaje cuando recibe daño.

        Args:
            danio (int): La cantidad de daño recibido.
        """
        self.energia -= danio
        if self.energia < 0:
            self.energia = 0

    def esta_vivo(self):
        """
        Verifica si el personaje está vivo.

        Returns:
            bool: True si la energía del personaje es mayor que 0, False en caso contrario.
        """
        return self.energia > 0

class TalanaKombat:
    """
    Representa el juego TalanaKombat, que simula un combate entre dos personajes.
    """

    def __init__(self):
        """
        Inicializa un nuevo objeto TalanaKombat.
        Crea los personajes Tonyn y Arnaldor y les asigna sus respectivos movimientos especiales.
        """
        
        self.tonyn = Personaje("Tonyn")
        self.arnaldor = Personaje("Arnaldor")
        self.tonyn.movimientos_especiales = {
            "DSD+P": ("Taladoken", 3),
            "SD+K": ("Remuyuken", 2)
        }
        self.arnaldor.movimientos_especiales = {
            "SA+K": ("Remuyuken", 3),
            "ASA+P": ("Taladoken", 2)
        }
    def procesar_turno(self, jugador, movimiento, golpe, jugador2):
        """
        Procesa un turno del combate, determinando la acción y el daño causado.

        Args:
            jugador (Personaje): El jugador que realiza la acción.
            movimiento (str): El movimiento realizado por el jugador.
            golpe (str): El golpe realizado por el jugador.
            jugador2 (Personaje): El jugador que recibe la acción.

        Returns:
            tuple: Una tupla con la descripción de la acción y el daño causado.
         """
        
        combinacion = movimiento + "+" + golpe
        if combinacion in jugador.movimientos_especiales:
            nombre_ataque, danio = jugador.movimientos_especiales[combinacion]
            return f"{jugador.nombre} usa un {nombre_ataque}", danio
        elif golpe == "P":
            return f"{jugador.nombre} da un puñetazo al pobre {jugador2.nombre}", 1
        elif golpe == "K":
            return f"{jugador.nombre} da una patada", 1
        elif movimiento:
            return f"{jugador.nombre} se mueve", 0
        else:
            return f"", 0
   
    def simular_combate(self, datos):
        """ 
        Simula un combate entre Simula un combate entre los personajes Tonyn y Arnaldor.

        Args:
            datos (dict): Un diccionario que contiene los movimientos y golpes de los dos jugadores.

        Returns:
            list: Una lista de strings que narran las acciones del combate. los personajes Tonyn y Arnaldor.
        """

        jugadores = [self.tonyn, self.arnaldor]
        movimientos = [datos["player1"]["movimientos"], datos["player2"]["movimientos"]]
        golpes = [datos["player1"]["golpes"], datos["player2"]["golpes"]]
        
        # Igualar la longitud de las listas
        max_longitud = max(len(movimientos[0]) + len(golpes[0]), len(movimientos[1]) + len(golpes[1]))
        for i in range(2):
            while len(movimientos[i]) + len(golpes[i]) < max_longitud:
                if len(movimientos[i]) <= len(golpes[i]):
                    movimientos[i].append("")
                else:
                    golpes[i].append("")
        
        turno = 0 if len(movimientos[0]) + len(golpes[0]) <= len(movimientos[1]) + len(golpes[1]) else 1
        narracion = []
        
        while all(jugador.esta_vivo() for jugador in jugadores):
            # Mientras ambos jugadores sigan vivos
            atacante = jugadores[turno]
            defensor = jugadores[1 - turno]
            # Determinar al atacante y al defensor según el turno actual

            if not movimientos[turno] and not golpes[turno]:
                # Si el atacante no tiene más movimientos ni golpes, termina el combate
                break

            # Obtener el siguiente movimiento y golpe del atacante
            mov = movimientos[turno].pop(0) if movimientos[turno] else ""
            golpe = golpes[turno].pop(0) if golpes[turno] else ""

            # Procesar el turno del atacante
            accion, danio = self.procesar_turno(atacante, mov, golpe, defensor)
            if accion:
                # Agregar la acción a la narración del combate
                narracion.append(accion)
            # Aplicar el daño al defensor
            defensor.recibir_danio(danio)

            # Cambiar el turno al otro jugador
            turno = 1 - turno
            
        ganador = self.tonyn if self.tonyn.esta_vivo() else self.arnaldor
        narracion.append(f"{ganador.nombre} Gana la pelea y aun le queda {ganador.energia} de energía")
        
        return narracion

# Ejemplo de uso
juego = TalanaKombat()
datos_combate1 = {
   "player1": {"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","P","K","P"]},
    "player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}
}


resultado = juego.simular_combate(datos_combate1)
for linea in resultado:
    print(f" {linea}")
   
