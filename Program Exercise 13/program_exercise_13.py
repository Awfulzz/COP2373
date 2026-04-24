import sqlite3
import random
import matplotlib.pyplot as plt


# Database name with initials AB
DATABASE_NAME = 'population_AB.db'


def create_database():
    # Connect to the database
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Delete the table if it already exists
    cursor.execute('DROP TABLE IF EXISTS population')

    # Create the population table
    cursor.execute('CREATE TABLE population (city TEXT, year INTEGER, population INTEGER)')

    connection.commit()
    connection.close()


def add_starting_data():
    # Starting population data for 10 Florida cities in 2025
    cities = [
        ['Jacksonville', 1016000],
        ['Miami', 455000],
        ['Tampa', 410000],
        ['Orlando', 330000],
        ['St. Petersburg', 265000],
        ['Hialeah', 220000],
        ['Port St. Lucie', 250000],
        ['Tallahassee', 205000],
        ['Cape Coral', 225000],
        ['Fort Lauderdale', 185000]
    ]

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Insert each city into the table
    for city in cities:
        cursor.execute(
            'INSERT INTO population VALUES (?, ?, ?)',
            (city[0], 2025, city[1])
        )

    connection.commit()
    connection.close()


def add_future_population_data():
    # This makes the random numbers the same each time the program runs
    random.seed(10)

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Get the 2025 data
    cursor.execute('SELECT city, population FROM population WHERE year = 2025')
    cities = cursor.fetchall()

    # Create population data for the next 20 years
    for city, population in cities:
        current_population = population

        for year in range(2026, 2046):
            # Random rate between -2% and 3%
            rate = random.uniform(-0.02, 0.03)

            # Calculate the new population
            current_population = int(current_population * (1 + rate))

            # Insert the new year and population
            cursor.execute(
                'INSERT INTO population VALUES (?, ?, ?)',
                (city, year, current_population)
            )

    connection.commit()
    connection.close()


def show_city_options():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Get all city names
    cursor.execute('SELECT DISTINCT city FROM population ORDER BY city')
    cities = cursor.fetchall()

    connection.close()

    print('\nChoose one city:')

    for number in range(len(cities)):
        print(str(number + 1) + '. ' + cities[number][0])

    return cities


def graph_city_population(city):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Get population data for the chosen city
    cursor.execute(
        'SELECT year, population FROM population WHERE city = ? ORDER BY year',
        (city,)
    )

    data = cursor.fetchall()
    connection.close()

    years = []
    populations = []

    for row in data:
        years.append(row[0])
        populations.append(row[1])

    # Create the graph
    plt.plot(years, populations, marker='o')
    plt.title('Population Growth and Decline for ' + city)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.show()


def main():
    create_database()
    add_starting_data()
    add_future_population_data()

    cities = show_city_options()

    choice = int(input('\nEnter a number from 1 to 10: '))
    chosen_city = cities[choice - 1][0]

    print('\nShowing graph for ' + chosen_city)
    graph_city_population(chosen_city)


main()

