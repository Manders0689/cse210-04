class Director:
    
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
    _keyboard_service (KeyboardService): For getting directional input.
    _video_service (VideoService): For providing video output.
    """

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

def start_game(self):
    pass
        
# _get_inputs()



#store/update/outputs total game points