from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 3439
        self._members = []
    
    

    # Este método genera un 'id' único al agregar miembros a la lista (no debes modificar esta función)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        """
        Agrega un nuevo miembro a la lista de miembros.
        """
        member['id'] = self._generate_id()
        member['first_name'] = member['first_name']
        member['last_name'] = self.last_name  # Asegurar que el apellido sea siempre Jackson
        member['age'] = member['age']
        member['lucky_numbers'] = member['lucky_numbers']
        self._members.append(member)

    def delete_member(self, id):
        """
        Elimina un miembro de la lista basado en su ID.
        """
        self._members = [member for member in self._members if member['id'] != id]

    def get_member(self, id):
        """
        Devuelve la información de un miembro basado en su ID.
        """
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    def get_all_members(self):
        """
        Devuelve la lista de todos los miembros de la familia.
        """
        return self._members
    
    def update_member(self, id, updated_data):
        """
        Actualiza la información de un miembro basado en su ID.
        """
        for member in self._members:
            if member['id'] == id:
                member.update(updated_data)
                return member
        return None
