#!/usr/bin/env python
# TODO Import the Turtlesim environment when ROS is installed
# from turtlesim_enacter import TurtleSimEnacter

# Olivier Georgeon, 2020.
# This code is used to teach Develpmental AI.


class Agent:
    def __init__(self, _hedonist_table, maxBored):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = 0
        self.anticipated_outcome = 0

        self.maxBored = maxBored
        self.memory = {}

        self.cmpGAnticipation = 0
        self.cmpBestAction = 0
        self.BestAction = 0
        self.BestOutcome = 0
        self.lastAction = 0

    def action(self, outcome):
        """ Computing the next action to enact """
        if self.valMeilleurHedonist(outcome):
            self.BestAction = self._action
            self.BestOutcome = outcome
            self.cmpBestAction = 0

        self._action = self.BestAction

        #  On remet les compteurs à zéro au cas ou l'agent s'ennuie
        if self.boolEnnui(): self.changerAction()

        # On met à jour la mémoire en fonction de l'outcome comme pour l'agent 1
        self.majmemory(outcome)

        # On met à jours le compte de bonne anticipation faite et d'action préféré faite
        self.majCmp(outcome)
        
        self.derniere_action = self._action
        return self._action

    def majmemory(self, outcome):
        if self._action not in self.memory.keys():
            self.memory[self._action] = outcome
        elif self.anticipated_outcome != outcome:
            self.memory[self.derniere_action] = outcome

    def majCmp(self, outcome):
        if self.anticipated_outcome == outcome:
            self.cmpGAnticipation += 1

        if self.BestAction == self._action:
            self.cmpBestAction += 1

    def valMeilleurHedonist(self, outcome):
        return self.hedonist_table[self._action][
            outcome] > self.hedonist_table[self.BestAction][self.BestOutcome]

    def changerAction(self):
        self.cmpGAnticipation = 0
        self.cmpBestAction = 0
        if self._action == 1:
            self._action = 0
        else:
            self._action = 1

    def anticipation(self):
        """ computing the anticipated outcome from the latest action """
        # TODO: Implement the agent's anticipation mechanism

        self.anticipated_outcome = self.memory[self._action]

        return self.anticipated_outcome

    def boolEnnui(self):
        return self.cmpGAnticipation >= self.maxBored and self.cmpBestAction >= self.maxBored

    def satisfaction(self, new_outcome):
        """ Computing a tuple representing the agent's satisfaction after the last interaction """
        # True if the anticipation was correct
        anticipation_satisfaction = (self.anticipated_outcome == new_outcome)
        # The value of the enacted interaction
        hedonist_satisfaction = self.hedonist_table[self._action][new_outcome]

        return anticipation_satisfaction, hedonist_satisfaction, self.boolEnnui(
        )


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


def world(agent, environment):
    """ The main loop controlling the interaction of the agent with the environment """
    outcome = 0
    print(" Action:  , Anticipation:  , Outcome:  , (Bonne Anticipation , Valeur Hedoniste, Ennuie) \n" )
    for i in range(15):
        action = agent.action(outcome)
        outcome = environment.outcome(action)
        print(" Action: " + str(action) + ", Anticipation: " +
              str(agent.anticipation()) + ", Outcome: " + str(outcome) +
              ", Satisfaction: " + str(agent.satisfaction(outcome)))


cmpGAnticipation = 0
# TODO Define the hedonist values of interactions (action, outcome)
hedonist_table = [[-1, 1], [-1, 1]]
# TODO Choose an agent
a = Agent(hedonist_table, 4)
# TODO Choose an environment
e = Environment1()
# e = Environment2()
# e = TurtleSimEnacter()

world(a, e)
