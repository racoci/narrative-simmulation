class World:
    def __init__(self):
        self.entities = {}

    def add_entity(self, entity_id, properties):
        self.entities[entity_id] = properties

    def get_entity_properties(self, entity_id):
        return self.entities.get(entity_id)

    def update_entity_properties(self, entity_id, new_properties):
        if entity_id in self.entities:
            self.entities[entity_id].update(new_properties)
            return True
        return False

    def remove_entity(self, entity_id):
        if entity_id in self.entities:
            del self.entities[entity_id]
            return True
        return False


