import unittest
import json

from talana_kombat import TalanaKombat

# Aquí agrego las pruebas unitarias de TalanaKombat

class TestTalanaKombat(unittest.TestCase):

    def setUp(self):
        self.juego = TalanaKombat()
        self.datos_combate1 = {
            "player1": {"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","P","K","P"]},
            "player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}
        }
        self.datos_combate2 = {
            "player1":{"movimientos":["SDD", "DSD", "SA", "DSD"] ,"golpes":["K", "P", "K", "P"]}, 
            "player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P","k"]}
        }
        self.datos_combate3 = {
            "player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", "", ]}, 
            "player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}
        }
    
    def test_combate1(self):
        # Prueba del primer combate - Arnardold Gana la pelea y aun le queda 1 de energía
        resultado = self.juego.simular_combate(self.datos_combate1)
        esperado = [
            'Tonyn da una patada', 
            'Arnaldor usa un Remuyuken', 
            'Tonyn usa un Taladoken', 
            'Arnaldor se mueve', 
            'Tonyn da un puñetazo al pobre Arnaldor', 
            'Arnaldor usa un Remuyuken',
            'Arnaldor Gana la pelea y aun le queda 1 de energía'
        ]
        self.assertEqual(resultado, esperado)
    # Prueba del segundo combate - Gana Tonyn
    def test_combate2(self):
        resultado = self.juego.simular_combate(self.datos_combate2)
        esperado = [
            'Tonyn da una patada',
            'Arnaldor da un puñetazo al pobre Tonyn', 
            'Tonyn usa un Taladoken', 
            'Arnaldor da una patada', 
            'Tonyn da una patada', 
            'Arnaldor da una patada', 
            'Tonyn usa un Taladoken', 
            'Tonyn Gana la pelea y aun le queda 3 de energía'
        ]
        self.assertEqual(resultado, esperado)

    # Prueba del tercer combate - Gana Arnaldor
    def test_combate3(self):
        resultado = self.juego.simular_combate(self.datos_combate3)
        esperado = [
            'Tonyn usa un Taladoken', 
            'Arnaldor da un puñetazo al pobre Tonyn', 
            'Tonyn se mueve', 
            'Arnaldor se mueve',
            'Arnaldor da un puñetazo al pobre Tonyn', 
            'Arnaldor da una patada', 'Arnaldor da una patada', 
            'Arnaldor usa un Remuyuken', 
            'Arnaldor Gana la pelea y aun le queda 3 de energía'
        ]
        self.assertEqual(resultado, esperado)
      

if __name__ == '__main__':
    unittest.main()
