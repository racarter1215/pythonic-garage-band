class Band:

    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        self.__class__.instances.append(self.name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        return [player.play_solo() for player in self.members]
    
    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:
    def __init__(self, name: str, instrument: str=None):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
    
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

class Guitarist(Musician):   
    def __init__(self, name):
        super().__init__(name)
        self.instrument = 'guitar' 

    def play_solo(self):
        return "face melting guitar solo"

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.instrument = 'drums'

    def play_solo(self):
        return "rattle boom crash"

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.instrument = 'bass'

    def play_solo(self):
        return "bom bom buh bom"

if __name__ == "__main__":
    guitarist = Guitarist('Jane')
    print(guitarist)