__author__ = 'Dariusz'

""" A simple elevator simulator takes a user entry of number of floors and a number of costumers.
    The building is being created based on user input,and costumers list which holds information
    about each of the costumers like its Id, its starting floor and its destination floor which are randomly picked.
     Elevator starts at ground floor moving up and picking up costumers and letting them out on their destination
      floors. Once the costumer have used a elevator its removed from a costumer list. When Lift reaches a top floor
      a direction is being changed and elevator moves down floor by floor.The simulation ends when all the costumers
      use an elevator"""

import random

""" class to define a building with a total number of floors and a costumer list and equipped with elevator """


class Building:

    def __init__(self, total_floor, costumer_list, elevator):
        self.total_floor = total_floor
        self.costumer_list = costumer_list
        self.total_costumers = len(costumer_list)

    def __str__(self):
        return ' |Total floors in building {}, Number of costumers {}| '.format(self.total_floor, self.total_costumers)

    def __repr__(self):
        return self.__str__()


""" class to define elevator"""


class Elevator(Building):

    def __init__(self, total_floor, costumer_list):
        super(Building, self).__init__()

        self.costumer_list = costumer_list
        self.direction = ['up']
        self.lift = []
        self.ground_floor = 0
        self.top_floor = total_floor
        self.current_floor = 0
        self.limit = 4
        self.total_floor = total_floor
        self.elevator_moves = 0

    def __str__(self):
        return ' |{},{}| '.format(self.current_floor, self.total_floor)

    def __repr__(self):
        return self.__str__()

    """ Function to run the simulation of the elevator
     it will run till costumers list is empty and there is no costumers in lift"""

    def run(self):

        while (len(self.costumer_list)) != 0:
            print('-------------')
            print('current floor...', self.current_floor)
            self.costumer_out()
            self.costumer_in()
            self.move()
            print('costumers in building ', len(self.costumer_list))

        while len(self.lift) != 0:
            print('-------------')
            print('current floor...', self.current_floor)
            self.costumer_out()
            self.move()
        print('costumers in building  ', len(self.costumer_list))
        print('costumers in lift .... ', len(self.lift))
        print('Elevator moves    .... {} '.format(self.elevator_moves))

    """ Function to let costumer in to an elevator if the current floor is equal to costumers starting floor and
        if the destination floor of costumer is correct with a direction of the lift
        and if the limit of the elevator is not exceeded, when the costumer enters the elevator its then removed
        from a floor"""

    def costumer_in(self):

        for i in self.costumer_list:
            if i.starting_floor == self.current_floor and i.destination_floor > i.starting_floor:
                if self.limit > len(self.lift):
                    self.lift.append(i)
                    print('costumer got in ....')
                    self.costumer_list.remove(i)
                    print('lift - ', self.lift)
            if i.starting_floor == self.current_floor and i.destination_floor < i.starting_floor:
                if self.limit > len(self.lift):
                    self.lift.append(i)
                    print('costumer got in ....')
                    self.costumer_list.remove(i)
                    print('lift - ', self.lift)
            else:
                pass

    """ Function to let the costumer out of the elevator if the current position of the lift matches costumer`s
    destination floor"""

    def costumer_out(self):

        print('lift - ', self.lift)
        for i in self.lift:
            if self.current_floor == i.destination_floor:
                self.lift.remove(i)
                print('costumer got out .....')
                print('lift - ', self.lift)


    """ Function that moves an elevator one floor at a time, up or down depends on direction of the elevator """

    def move(self):

        self.elevator_moves += 1
        """Moves the elevator one floor"""
        if self.current_floor == self.ground_floor:
            self.direction.clear()
            self.direction.append("up")

        if self.current_floor == self.total_floor:
            self.direction.clear()
            self.direction.append("down")

        if self.direction[0] == "down":
            self.current_floor -= 1
            print(' Going down ....')

        if self.direction[0] == 'up':
            self.current_floor += 1
            print(' Going up ....')
        print('lift - {}'.format(self.lift))

""" Class to define costumers. The starting floor and the destination floor of costumers
    its randomly picked"""

class Costumer(Building):

    def __init__(self, Id, total_floor, destination_floor=0):
        super(Building, self).__init__()

        self.Id = Id
        self.total_floor = total_floor
        self.starting_floor = random.randint(1, self.total_floor)
        self.destination_floor = random.randint(1, self.total_floor)
        while self.destination_floor == self.starting_floor:
            self.destination_floor = random.randint(1, self.total_floor)


    def __str__(self):
        return '{}, {}, {}'.format(self.Id, self.starting_floor, self.destination_floor)

    def __repr__(self):
        return self.__int__()

    def __int__(self):
        return '{}, {}, {}'.format(self.Id, self.starting_floor, self.destination_floor)

""" Start of a main function """

def main():

    """ Getting user input for floor numbers and number of costumers """

    total_floors = int(input('Enter number of floors ...'))
    num_cost = int(input('Enter number of costumers'))


    cost_list = []

    """ for loop to create costumer list """

    for i in range(num_cost):
        cost_list.append(Costumer(i, total_floors))

    """ create elevator using total floors number and costumer list """

    elevator = Elevator(total_floors, cost_list)
    print("------------------")
    print(" Creating Building ....")
    print("------------------")

    """ creating building """

    b = Building(total_floors, cost_list, elevator)

    print(b)
    print(" Starting Simulation .....")
    print("----------------------------")

    """ start of the simulation """

    elevator.run()

    print('-----------------------------------------')
    print('end of simulation ....')


if __name__ == "__main__":
    main()
