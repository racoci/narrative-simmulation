"""
Módulo que implementa o núcleo de simulação.
"""

from typing import Dict, List, Any, Optional, Set, Union, Callable
import time
from src.hypergraph import Hypergraph


class SimulationCore:
    """
    Classe que implementa o núcleo de simulação.
    Gerencia o tempo e a atualização dos estados dos agentes.
    """
    
    def __init__(self, time_step: float = 1.0):
        """
        Inicializa o núcleo de simulação.
        
        Args:
            time_step: Intervalo de tempo entre atualizações (em unidades de tempo da simulação).
        """
        self.time_step = time_step
        self.current_time = 0
        self.agents = {}  # Dicionário de agentes registrados
        self.world = None  # Módulo de mundo
        self.running = False
        self.event_listeners = {}  # Dicionário de ouvintes de eventos
        
    def register_agent(self, agent_id: str, agent: Any) -> None:
        """
        Registra um agente no núcleo de simulação.
        
        Args:
            agent_id: ID único do agente.
            agent: Objeto do agente.
        """
        self.agents[agent_id] = agent
        
    def unregister_agent(self, agent_id: str) -> None:
        """
        Remove um agente do núcleo de simulação.
        
        Args:
            agent_id: ID do agente a ser removido.
        """
        if agent_id in self.agents:
            del self.agents[agent_id]
            
    def set_world(self, world: Any) -> None:
        """
        Define o módulo de mundo.
        
        Args:
            world: Objeto do módulo de mundo.
        """
        self.world = world
        
    def register_event_listener(self, event_type: str, listener: Callable) -> None:
        """
        Registra um ouvinte para um tipo de evento.
        
        Args:
            event_type: Tipo de evento.
            listener: Função a ser chamada quando o evento ocorrer.
        """
        if event_type not in self.event_listeners:
            self.event_listeners[event_type] = []
        self.event_listeners[event_type].append(listener)
        
    def trigger_event(self, event_type: str, event_data: Any) -> None:
        """
        Dispara um evento.
        
        Args:
            event_type: Tipo de evento.
            event_data: Dados do evento.
        """
        if event_type in self.event_listeners:
            for listener in self.event_listeners[event_type]:
                listener(event_data)
                
    def tick(self) -> None:
        """
        Avança a simulação em um passo de tempo.
        """
        # Atualiza o tempo atual
        self.current_time += self.time_step
        
        # Atualiza o mundo
        if self.world:
            self.world.update(self.current_time)
            
        # Atualiza cada agente
        for agent_id, agent in self.agents.items():
            agent.update(self.current_time, self.time_step)
            
        # Dispara o evento de tick
        self.trigger_event("tick", {"time": self.current_time})
        
    def start(self) -> None:
        """
        Inicia a simulação.
        """
        self.running = True
        self.trigger_event("simulation_start", {"time": self.current_time})
        
    def stop(self) -> None:
        """
        Para a simulação.
        """
        self.running = False
        self.trigger_event("simulation_stop", {"time": self.current_time})
        
    def run(self, steps: int = 100, real_time: bool = False, real_time_factor: float = 1.0) -> None:
        """
        Executa a simulação por um número específico de passos.
        
        Args:
            steps: Número de passos a serem executados.
            real_time: Se True, a simulação será executada em tempo real.
            real_time_factor: Fator de aceleração do tempo real (ex: 2.0 = 2x mais rápido).
        """
        self.start()
        
        for _ in range(steps):
            if not self.running:
                break
                
            start_time = time.time()
            
            self.tick()
            
            if real_time:
                # Calcula o tempo que deve passar em tempo real
                real_time_step = self.time_step / real_time_factor
                
                # Calcula quanto tempo já passou
                elapsed = time.time() - start_time
                
                # Se ainda não passou tempo suficiente, espera
                if elapsed < real_time_step:
                    time.sleep(real_time_step - elapsed)
                    
        self.stop()

