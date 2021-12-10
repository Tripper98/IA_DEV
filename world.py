#!/usr/bin/env python
# Olivier Georgeon, 2021.
# This code is used to teach Developmental AI.
# from turtlesim_enacter import TurtleSimEnacter # requires ROS
from turtlepy_enacter import TurtlePyEnacter
# from Agent5 import Agent5
# from OsoyooCarEnacter import OsoyooCarEnacter


class Agent:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
<<<<<<< HEAD
        self._action = 0
        self.anticipated_outcome = 0
        
        self.cmpBored = 0
        self.memory = {}




=======
        self._action = None
        self.anticipated_outcome = None
>>>>>>> 61900a99422177c91cead89d8dc108e3fd3521dd

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) + ")")

        """ Computing the next action to enact """
        
        # On inverse l'action prévue lorsque l'agent atteint sa limite
        if self.cmpBored >= 4:
            self.cmpBored = 0
            if self._action == 1:
                self._action = 0
            else:
                self._action = 1

        # On initialise la memory avec l'outcome
        if self._action not in self.memory.keys():
            self.memory[self._action] = outcome

        # On donne à la mémoire la valeur de l'outcome si l'anticipation est ddifférente du outcome
        if self.anticipated_outcome != outcome:
            self.memory[self._action] = outcome

        # on augmente l'ennui de 1
        # si l'anticipation précédente est égale à l'outcome actuelle
        if self.anticipated_outcome == outcome:
            self.cmpBored += 1 

        

        return self._action

<<<<<<< HEAD
    def anticipation(self):
        """ computing the anticipated outcome from the latest action """
        # TODO: Implement the agent's anticipation mechanism
        # on anticipe la valeur de la mémoire pour l'action faite
        self.anticipated_outcome = self.memory[self._action]
        
        return self.anticipated_outcome



    def satisfaction(self, new_outcome):
        """ Computing a tuple representing the agent's satisfaction after the last interaction """
        # True if the anticipation was correct
        anticipation_satisfaction = (self.anticipated_outcome == new_outcome)
        # The value of the enacted interaction
        hedonist_satisfaction = self.hedonist_table[self._action][new_outcome]
        return anticipation_satisfaction, hedonist_satisfaction, self.cmpBored == 4

=======
>>>>>>> 61900a99422177c91cead89d8dc108e3fd3521dd

class Environment1:
    """ In Environment 1, action 0 yields outcome 0, action 1 yields outcome 1 """
    def outcome(self, action):
        if action == 0:
            return 0
        else:
            return 1


class Environment2:
    """ In Environment 2, action 0 yields outcome 1, action 1 yields outcome 0 """
    def outcome(self, action):
        if action == 0:
            return 1
        else:
            return 0


<<<<<<< HEAD
def world(agent, environment):
    """ The main loop controlling the interaction of the agent with the environment """
    outcome = 0
    print(" Action:  , Anticipation:  , Outcome:  , (Bonne Anticipation , Valeur Hedoniste, ennuie) \n" )
    for i in range(15):
        action = agent.action(outcome)
        outcome = environment.outcome(action)
        print(" Action: " + str(action) + ", Anticipation: " + str(agent.anticipation()) + ", Outcome: " + str(outcome)
              + ", Satisfaction: " + str(agent.satisfaction(outcome)))

cmpBored = 0
# TODO Define the hedonist values of interactions (action, outcome)
=======
class Environment3:
    """ Environment 3 yields outcome 1 only when the agent alternates actions 0 and 1 """
    def __init__(self):
        """ Initializing Environment3 """
        self.previous_action = 0

    def outcome(self, action):
        _outcome = 1
        if action == self.previous_action:
            _outcome = 0
        self.previous_action = action
        return _outcome


# TODO Define the hedonist valance of interactions (action, outcome)
>>>>>>> 61900a99422177c91cead89d8dc108e3fd3521dd
hedonist_table = [[-1, 1], [-1, 1]]
# TODO Choose an agent
a = Agent(hedonist_table)
# a = Agent5(hedonist_table)
# TODO Choose an environment
<<<<<<< HEAD
# e = Environment1()
e = Environment2()
=======
e = Environment1()
# e = Environment2()
# e = Environment3()
>>>>>>> 61900a99422177c91cead89d8dc108e3fd3521dd
# e = TurtleSimEnacter()
# e = TurtlePyEnacter()
# e = OsoyooCarEnacter()

if __name__ == '__main__':
    """ The main loop controlling the interaction of the agent with the environment """
    outcome = 0
    for i in range(70):
        action = a.action(outcome)
        outcome = e.outcome(action)
