from game.casting.actor import Actor

class Rock(Actor):
    """
    An item of negative value. 

    The responsibility of a rock is to provide a negative point value.

    Attributes:
        _value (int): An integer value."""

    def __init__(self):

        """Contructs a new Rock
        Pulls attributes and methods from Actor class """

        super().__init__()
        self._value = -1

    def get_value(self):

        """Gets the rock's value
        
        Returns:
            Int: The rock's value"""

        return self._value
    
    def set_value(self,value):
        """
        Updates the value to the given one.
        
        Args:
            value (int): The given value
        """
        self._value = value