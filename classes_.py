class RussianRegions:
    def __init__(self, type = 'Регион'):
        self._type = type

    def __str__(self):
        return str(self._type)

    def capitol(self):
        pass

class PopulatedLocality:
    def __init__(self, type = 'Населенный пункт'):
        self._type = type

    def __str__(self):
        return str(self._type)

    def population(self):
        pass

    def foundation_year(self):
        pass

    