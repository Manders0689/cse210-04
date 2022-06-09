from game.casting.actor import Actor

class Gem(Actor):

    """An item of value. 

    The responsibility of a gem is to provide a point value.

    Attributes:
        _value (int): An integer value."""

    def __init__(self):

        """Contructs a new Gem
        Pulls attributes and methods from Actor class """

        super().__init__()
        self._value = 1

    def get_value(self):

        """Gets the gem's value
        
        Returns:
            Int: The gem's value"""

        return self._value

