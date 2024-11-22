import unittest
import logging

class Runner:
    def __init__(self, name, speed=5):
        try:
            if isinstance(name, str):
                self.name = name
                logging.info(f'runner name {self.name} is the string')
            else:
                raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
            self.distance = 0
            if speed > 0:
                self.speed = speed
            else:
                raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')
        except TypeError:
            logging.error(f'runner name should be string but  {name} is given')
        except ValueError:
            logging.error(f'speed should be positive number for {self.name} but given {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='test12_4.log', filemode='w',
                    format="%(asctime)s | %(levelname)s | %(message)s")

    first = Runner('Bob', 10)
    second = Runner(6, 5)
    third = Runner('Ana', 10)

    t = Tournament(101, first, second)
    print(t.start())

