"""
Testes para o núcleo de simulação.
"""

import sys
import os
import time

# Adiciona o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.simulation import SimulationCore

class MockAgent:
    """Agente simulado para testes."""
    
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.updates = 0
        self.last_time = 0
        
    def update(self, current_time, time_step):
        self.updates += 1
        self.last_time = current_time

class MockWorld:
    """Mundo simulado para testes."""
    
    def __init__(self):
        self.updates = 0
        self.last_time = 0
        
    def update(self, current_time):
        self.updates += 1
        self.last_time = current_time

def test_simulation_core():
    """Testa a criação e manipulação do núcleo de simulação."""
    print("Testando SimulationCore...")
    
    # Cria um núcleo de simulação
    sim = SimulationCore(time_step=0.5)
    
    # Verifica os atributos iniciais
    assert sim.time_step == 0.5
    assert sim.current_time == 0
    assert len(sim.agents) == 0
    assert sim.world is None
    assert sim.running == False
    
    # Cria e registra agentes
    agent1 = MockAgent("agent1")
    agent2 = MockAgent("agent2")
    
    sim.register_agent("agent1", agent1)
    sim.register_agent("agent2", agent2)
    
    # Verifica se os agentes foram registrados
    assert len(sim.agents) == 2
    assert sim.agents["agent1"] == agent1
    assert sim.agents["agent2"] == agent2
    
    # Cria e define o mundo
    world = MockWorld()
    sim.set_world(world)
    
    # Verifica se o mundo foi definido
    assert sim.world == world
    
    # Testa o método tick
    sim.tick()
    
    # Verifica se o tempo foi atualizado
    assert sim.current_time == 0.5
    
    # Verifica se o mundo foi atualizado
    assert world.updates == 1
    assert world.last_time == 0.5
    
    # Verifica se os agentes foram atualizados
    assert agent1.updates == 1
    assert agent1.last_time == 0.5
    assert agent2.updates == 1
    assert agent2.last_time == 0.5
    
    # Testa o método run
    sim.run(steps=5, real_time=False)
    
    # Verifica se o tempo foi atualizado
    assert sim.current_time == 3.0  # 0.5 + 5 * 0.5
    
    # Verifica se o mundo foi atualizado
    assert world.updates == 6  # 1 + 5
    assert world.last_time == 3.0
    
    # Verifica se os agentes foram atualizados
    assert agent1.updates == 6  # 1 + 5
    assert agent1.last_time == 3.0
    assert agent2.updates == 6  # 1 + 5
    assert agent2.last_time == 3.0
    
    # Testa o registro e disparo de eventos
    event_data = None
    
    def event_listener(data):
        nonlocal event_data
        event_data = data
    
    sim.register_event_listener("test_event", event_listener)
    sim.trigger_event("test_event", {"value": 42})
    
    # Verifica se o evento foi disparado
    assert event_data is not None
    assert event_data["value"] == 42
    
    # Testa a remoção de um agente
    sim.unregister_agent("agent1")
    
    # Verifica se o agente foi removido
    assert len(sim.agents) == 1
    assert "agent1" not in sim.agents
    assert "agent2" in sim.agents
    
    print("Teste de SimulationCore concluído com sucesso!")

def test_simulation_real_time():
    """Testa a execução em tempo real do núcleo de simulação."""
    print("Testando execução em tempo real...")
    
    # Cria um núcleo de simulação
    sim = SimulationCore(time_step=0.1)
    
    # Cria e registra um agente
    agent = MockAgent("agent")
    sim.register_agent("agent", agent)
    
    # Executa a simulação em tempo real
    start_time = time.time()
    sim.run(steps=5, real_time=True, real_time_factor=1.0)
    end_time = time.time()
    
    # Verifica se o tempo de execução foi próximo do esperado
    expected_time = 5 * 0.1  # 5 passos de 0.1 unidades de tempo
    actual_time = end_time - start_time
    
    # Permite uma margem de erro de 50% (para levar em conta o overhead)
    assert actual_time >= expected_time * 0.5
    assert actual_time <= expected_time * 1.5
    
    print("Teste de execução em tempo real concluído com sucesso!")

def run_tests():
    """Executa todos os testes."""
    test_simulation_core()
    test_simulation_real_time()
    print("Todos os testes concluídos com sucesso!")

if __name__ == "__main__":
    run_tests()

