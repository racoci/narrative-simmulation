"""
Teste de depuração para o método contains da classe Location.
"""

import sys
import os

# Adiciona o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.world import Location

def test_contains():
    """Testa o método contains da classe Location."""
    
    # Cria um local
    location = Location(
        entity_id="l1",
        name="Test Location",
        position={"x": 0.0, "y": 0.0, "z": 0.0},
        area={"width": 10.0, "height": 10.0, "depth": 10.0}
    )
    
    # Calcula os limites do local
    min_x = location.position["x"] - location.area["width"] / 2
    max_x = location.position["x"] + location.area["width"] / 2
    min_y = location.position["y"] - location.area["height"] / 2
    max_y = location.position["y"] + location.area["height"] / 2
    min_z = location.position["z"] - location.area["depth"] / 2
    max_z = location.position["z"] + location.area["depth"] / 2
    
    print(f"Limites do local: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}], z=[{min_z}, {max_z}]")
    
    # Testa vários pontos
    test_points = [
        {"x": 0.0, "y": 0.0, "z": 0.0},  # Centro
        {"x": 4.0, "y": 4.0, "z": 4.0},  # Dentro
        {"x": 5.0, "y": 0.0, "z": 0.0},  # Na borda (x)
        {"x": 0.0, "y": 5.0, "z": 0.0},  # Na borda (y)
        {"x": 0.0, "y": 0.0, "z": 5.0},  # Na borda (z)
        {"x": 6.0, "y": 0.0, "z": 0.0},  # Fora (x)
        {"x": 0.0, "y": 6.0, "z": 0.0},  # Fora (y)
        {"x": 0.0, "y": 0.0, "z": 6.0},  # Fora (z)
    ]
    
    for i, point in enumerate(test_points):
        result = location.contains(point)
        print(f"Ponto {i}: {point} - Dentro do local: {result}")

if __name__ == "__main__":
    test_contains()

