import unittest

from PIL.IcnsImagePlugin import read_32t


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)
        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = []

    @classmethod
    def tearDownClass(cls):
        global all_results
        for i in all_results:
            print(i)

    def setUp(self):
        global r_1, r_2, r_3
        r_1 = Runner('Mike', 10)
        r_2 = Runner('Bob', 9)
        r_3 = Runner('Ana', 3)

    def test_Tournament_run_1(self):
        t_1 = Tournament(90, r_1, r_3)
        a = t_1.start()
        all_results.append(a)
        self.assertTrue(list(a.values())[-1] == 'Ana')

    def test_Tournament_run_2(self):
        t_2 = Tournament(90, r_2, r_3)
        b = t_2.start()
        all_results.append(b)
        self.assertTrue(list(b.values())[-1] == 'Ana')

    def test_Tournament_run_3(self):
        global all_results
        t_3 = Tournament(90, r_1, r_2, r_3)
        c = t_3.start()
        all_results.append(c)
        self.assertTrue(list(c.values())[-1] == 'Ana')

    def test_Tournament_run_4(self):
        global all_results
        t_4 = Tournament(4, r_3, r_2, r_1)
        d = t_4.start()
        all_results.append(d)
        self.assertTrue(list(d.values())[-1] == 'Ana')

