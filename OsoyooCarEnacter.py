# Olivier Georgeon, 2021.
# This code is used to teach Developmental AI.
# Requires:
#   - A robot Osoyoo Car https://osoyoo.com/2019/11/08/omni-direction-mecanum-wheel-robotic-kit-v1/
#   - Project https://github.com/OlivierGeorgeon/osoyoo
#       (Tested with commit 33519f3 December 04th 2021)
#   - Python libraries pyglet and keyboard
from EgoMemoryWindow import EgoMemoryWindow
import pyglet
import json


class OsoyooCarEnacter:
    def __init__(self):
        """ Instantiating the robot's egocentric spatial memory window """
        self.osoyoo_car_window = EgoMemoryWindow(600)
        self.osoyoo_car_window.zoom_level = 2

        self.osoyoo_car_window.dispatch_events()
        self.osoyoo_car_window.on_draw()
        self.osoyoo_car_window.flip()

    def outcome(self, action):
        """ Enacting an action and returning the outcome """
        outcome = 0
        if action == 0:
            # outcome = self.osoyoo_car_window.on_text('8')  # Move forward
            self.osoyoo_car_window.async_action_trigger('8')
        if action == 1:
            # outcome = self.osoyoo_car_window.on_text('1')  # Turn left
            self.osoyoo_car_window.async_action_trigger('1')
        if action > 1:
            # outcome = self.osoyoo_car_window.on_text('3')  # Turn right
            self.osoyoo_car_window.async_action_trigger('3')

        # Wait for the outcome while processing pyglet events
        while self.osoyoo_car_window.async_flag < 2:
            # Inspired by https://stackoverflow.com/questions/61217265/
            pyglet.clock.tick()
            self.osoyoo_car_window.dispatch_events()
            self.osoyoo_car_window.on_draw()
            self.osoyoo_car_window.flip()

        self.osoyoo_car_window.process_outcome(self.osoyoo_car_window.async_action, self.osoyoo_car_window.async_outcome_string)
        self.osoyoo_car_window.async_flag = 0

        pyglet.clock.tick()
        self.osoyoo_car_window.dispatch_events()
        self.osoyoo_car_window.on_draw()
        self.osoyoo_car_window.flip()

        outcome = 0
        json_outcome = json.loads(self.osoyoo_car_window.async_outcome_string)
        if 'floor_outcome' in json_outcome:
            outcome = json_outcome['floor_outcome']

        return int(outcome)


if __name__ == "__main__":
    """ Run in interactive mode """
    e = OsoyooCarEnacter()

    _outcome = 0
    for i in range(10):
        _action = input("Enter action: ")
        _outcome = e.outcome(int(_action))
        print("Action: " + _action + " Outcome: " + str(_outcome))
