import unittest
import numpy as np
from TSP import distance, total_distance, create_population, evaluate_population, select, crossover, mutate, cities_5

class TestTSP(unittest.TestCase):
   # Перевірка відстані між двома точками
    def test_distance(self):
        self.assertAlmostEqual(distance((1, 1), (1, 1)), 0.0, places=2)

    #перевірка загальної відстані маршруту
    def test_total_distance(self):
        route = ['A', 'B', 'C']
        cities = {'A': (0, 0), 'B': (3, 4), 'C': (0, 3)}
        self.assertAlmostEqual(total_distance(route, cities), 11.16227766016838, places=2)
        route_single = ['A']
        self.assertEqual(total_distance(route_single, cities), 0.0)


    #перевірка створення популяції
    def test_create_population(self):
        pop = create_population(2, cities_5)
        self.assertEqual(len(pop), 2)
        self.assertEqual(len(pop[0]), 5)  # Перевірка кількості міст у маршруті
    # перевірка оцінки придатності популяції
    def test_evaluate_population(self):
        population = [['A', 'B', 'C'], ['B', 'C', 'A']]
        cities = {'A': (0, 0), 'B': (3, 4), 'C': (0, 3)}
        fitnesses = evaluate_population(population, cities)
        self.assertAlmostEqual(fitnesses[0], 11.16227766016838, places=2)
        self.assertAlmostEqual(fitnesses[1], 11.16227766016838, places=2)


    # перевірка вибору найкращих особин
    def test_select(self):
        population = [['A', 'B', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B']]
        fitnesses = [10, 20, 15]
        selected = select(population, fitnesses, 2)
        self.assertEqual(len(selected), 2)
        self.assertIn(['A', 'B', 'C'], selected)

        #перевірка створення нащадка
    def test_crossover(self):
        route1 = ['A', 'B', 'C', 'D']
        route2 = ['B', 'D', 'A', 'C']
        child = crossover(route1, route2)
        self.assertEqual(len(child), 4)
        self.assertEqual(set(child), set(route1))


    #перевірка мутації маршруту
    def test_mutate(self):
        route = ['A', 'B', 'C', 'D']
        original = route.copy()
        mutate(route, 1.0)  # Примусова мутація
        self.assertEqual(len(route), 4)  # Перевірка довжини маршруту
        self.assertNotEqual(route, original)  # Перевірка, що маршрут змінився

if __name__ == '__main__':
    unittest.main()