class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    person_id = 0

    def create_person(self, name):
        instance_id = self.person_id
        self.person_id += 1
        return Person(instance_id, name)
