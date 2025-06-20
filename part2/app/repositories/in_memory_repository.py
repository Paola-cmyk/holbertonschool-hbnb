import uuid

class InMemoryRepository:
    def __init__(self):
        self._storage = {}

    def add(self, obj):

        if not getattr(obj, 'id', None):
            obj.id = str(uuid.uuid4())
        self._storage[obj.id] = obj

    def get(self, obj_id):
        return self._storage.get(obj_id)

    def get_by_attribute(self, attr, value):
        for obj in self._storage.values():
            if getattr(obj, attr, None) == value:
                return obj
        return None

    def all(self):
        return list(self._storage.values())

    def update(self, obj_id, updated_obj):
        if obj_id in self._storage:
            self._storage[obj_id] = updated_obj
