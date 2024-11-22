import unittest
import tests_12_1
import tests_12_2

BigTest = unittest.TestSuite()
BigTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
BigTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(BigTest)
