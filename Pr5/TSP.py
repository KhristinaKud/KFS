import numpy as np
import random
import matplotlib.pyplot as plt

# Координати для 5, 7 і 9 міст
cities_5 = {'A': (0, 0), 'B': (2, 3), 'C': (5, 2), 'D': (6, 6), 'E': (8, 3)}
cities_7 = {'A': (0, 0), 'B': (2, 3), 'C': (5, 2), 'D': (6, 6), 'E': (8, 3), 'F': (1, 7), 'G': (4, 5)}
cities_9 = {'A': (0, 0), 'B': (2, 3), 'C': (5, 2), 'D': (6, 6), 'E': (8, 3), 'F': (1, 7), 'G': (4, 5), 'H': (7, 1), 'I': (3, 8)}

# Вибір набору міст
def select_cities():
    print("Виберіть кількість міст:")
    print("1) 5 міст")
    print("2) 7 міст")
    print("3) 9 міст")
    choice = input("Ваш вибір (1/2/3): ")
    if choice == '1':
        return cities_5
    elif choice == '2':
        return cities_7
    elif choice == '3':
        return cities_9
    else:
        print("Невірний вибір, використовуємо 5 міст за замовчуванням.")
        return cities_5

# Розрахунок дистанції між двома містами
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Виведення відстаней між усіма парами міст
def print_distances(cities):
    print("\nВідстані між містами:")
    city_names = list(cities.keys())
    for i in range(len(city_names)):
        for j in range(i + 1, len(city_names)):
            city1, city2 = city_names[i], city_names[j]
            dist = distance(cities[city1], cities[city2])
            print(f"({city1}, {city2}) = {dist:.2f}")

# Загальна довжина маршруту
def total_distance(route, cities):
    dist = 0
    for i in range(len(route)):
        dist += distance(cities[route[i]], cities[route[(i + 1) % len(route)]])
    return dist

# Генерація ініціалізації популяції
def create_population(size, cities):
    population = []
    for _ in range(size):
        route = list(cities.keys())
        random.shuffle(route)
        population.append(route)
    return population

# Оцінка придатності популяції
def evaluate_population(population, cities):
    return [total_distance(route, cities) for route in population]

# Вибір найкращого маршруту
def select(population, fitnesses, num_best):
    best_indices = np.argsort(fitnesses)[:num_best]
    return [population[i] for i in best_indices]

# Схрещування двох маршрутів
def crossover(route1, route2):
    start, end = sorted(random.sample(range(len(route1)), 2))
    child = [None] * len(route1)
    child[start:end] = route1[start:end]
    pointer = 0
    for city in route2:
        if city not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = city
    return child

# Мутація: рандомно змінити  міста
def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]

# Вирішення задачі TSP
def genetic_algorithm(cities, population_size=100, generations=500, mutation_rate=0.01):
    # Крок 1: Ініціалізація популяції
    population = create_population(population_size, cities)
    best_route = None
    best_distance = float('inf')
    for generation in range(generations):
        fitnesses = evaluate_population(population, cities)
        best_gen_route = population[np.argmin(fitnesses)]
        best_gen_distance = min(fitnesses)
        mean_distance = np.mean(fitnesses)
        print(f"Покоління {generation + 1}: Найкраща відстань = {best_gen_distance:.2f}, Середня відстань = {mean_distance:.2f}")
        if best_gen_distance < best_distance:
            best_route = best_gen_route
            best_distance = best_gen_distance
        new_population = select(population, fitnesses, population_size // 2)
        while len(new_population) < population_size:
            parent1_idx, parent2_idx = random.sample(range(len(new_population)), 2)
            parent1 = new_population[parent1_idx]
            parent2 = new_population[parent2_idx]
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    return best_route, best_distance

#  Візуалізація найкращого маршруту
def plot_route(route, cities):
    route_coords = [cities[city] for city in route]
    route_coords.append(route_coords[0])  # Закриваємо маршрут
    x, y = zip(*route_coords)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, '-o', color='blue')
    start_city = cities[route[0]]
    plt.plot(start_city[0], start_city[1], 'go', markersize=15)
    for city, coords in cities.items():
        plt.annotate(city, coords, textcoords='offset points', xytext=(0, 10), ha='center')
    plt.grid(True)
    plt.show()

def main():
    cities = select_cities()
    population_size = int(input("Введіть розмір популяції (наприклад, 100): "))
    generations = int(input("Введіть кількість ітерацій (наприклад, 500): "))
    mutation_rate = float(input("Введіть ймовірність мутації (наприклад, 0.01): "))
    print_distances(cities)
    best_route, best_distance = genetic_algorithm(cities, population_size, generations, mutation_rate)
    print("\nНайкращий шлях:", best_route)
    print("Найкраща відстань:", f"{best_distance:.2f}")
    plot_route(best_route, cities)

if __name__ == "__main__":
    main()