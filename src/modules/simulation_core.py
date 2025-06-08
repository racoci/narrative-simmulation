class SimulationCore:
    def __init__(self):
        self.agents = []
        self.current_tick = 0

    def register_agent(self, agent):
        self.agents.append(agent)

    def tick(self):
        self.current_tick += 1
        print(f"Simulation Tick: {self.current_tick}")
        for agent in self.agents:
            agent.update(self.current_tick)

class Agent:
    def __init__(self, id):
        self.id = id

    def update(self, current_tick):
        # This method will be overridden by specific agent types
        pass


