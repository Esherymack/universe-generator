# Universe Generator by Madison Tibbett
# a product of infinite boredom.
# "And All Was Quiet."

# TODO: Figure out ANSI text colors in Python.

# library imports
import random
import string
import time
import sys
import numpy as np

import log_script
import genlib
import wordgen

# global round precision
roundPrecision = 2

##### Universe Spawn #####
# after a universe successfully spawns, need to populate it with stars and nebulae.
# There is always at least one star in the system.
# Generation ends after system meets or exceeds 100 billion stars.
def spawnSystems():
    stars = 1
    nebula = 0
    timepassed = 0.0
    while True:
        # If chance roll is 1, then a star cluster spawns.
        # System is then tested to see what stars survived and what stars failed overall.
        # The reasoning behind this allows for more time to build up for a more realistic time scale.
        chance = random.randint(1, 3)
        if chance == 1:
            print("Star cluster spawned!")
            if genlib.determineFate():
                # if the stars survive, then increase by a power 1 through 4, randomly
                stars += stars**random.randint(1,4)
            else:
                # otherwise, decrease by division. If the star count somehow drops below 0, reset to 1.
                stars -= stars//random.randint(1,5)
                if stars <= 0:
                    stars = 1
            maxStars = 10e+11
            galaxyDivisor = 100000000
            if stars >= maxStars:
                print(f'\nTotal Stars: {stars}')
                galaxies = stars // galaxyDivisor
                # nebulae form in clumps in this generator, so randomly some number between 1000 and 1999 * total number of nebulae rolled.
                nebula = nebula*(random.randint(1000, 1999))
                print(f"Total galaxy formations: {galaxies}")
                print(f"Total nebula formations: {nebula}")
                # Represents billions of years.
                print(f"Billions of years past: {timepassed}")
                break
        elif chance == 2:
            print("Nebulae formed!")
            nebula += 1
        else:
            print("Nothing happened...")
            timepassed += random.uniform(1.0, 2.0)
        time.sleep(1)
    # i really didn't want to return a tuple, i swear
    return(galaxies, timepassed)

# Generates planet profile after planet is named.
def generatePlanetProfile(name, age):
    print(f"\nPlanet name is {name}.")
    print(f"Planet age is {age} billion years.")
    description = genlib.getDescriptor()
    description = ', '.join(description)
    planet_type = random.random()
    if planet_type < 0.5:
        print(f"{name} is a rocky planet.")
        genlib.generatePlanetBiomes()
        print(f"The terrain of {name} is {description}.")
    else:
        print(f"{name} is a gaseous planet.")
        print(f"The plasma oceans of {name} are {description}.")
    day_length = genlib.generateDayLength()
    print(f"The length of a day on {name} is {day_length} hours.")
    year_length_hours = genlib.generateYearLength()
    year_length_days = round(year_length_hours / day_length, roundPrecision)
    print(f"Given that a year is {year_length_hours} hours long, there are {year_length_days} days in a year on {name}.")
    input("\nPress enter to continue...\n")
    return (year_length_days, day_length)

# Runs time on planet from formation to destruction.
def runTime(yearLength, dayLength, age, name):
    # print(f"\nThe length of a year is {yearLength} days.")
    # print(f"There are {dayLength} hours in a day.")
    counter = 0
    civilDay = int(dayLength)
    planetAge = int(float(age))
    # how the fuck do i want to do this hhhhhh
    # let's start basic: there are five main stages in every planet's time scale
    # each one will have a helper function below because different things can happen in each one.
    # so first will randomly generate the planet's five primary ages:
    planetGeologicAges = genlib.generateAgeNames()
    planetGeologicAges = ', '.join(planetGeologicAges)
    print(f"The five ages of {name} are: {planetGeologicAges}")

##### Function Calls Below This Line #####
# who needs a main function lol
# start log now
sys.stdout = log_script.Logger()

systemTime = time.strftime("%c")
print(f"Universe spawned at : {systemTime}")
valueNumbers = spawnSystems()
totalGalaxies, timePassed = valueNumbers
observed = genlib.filterObservableUniverse(totalGalaxies)
genlib.filterHabitablePlanets(observed)
planetName = genlib.nameYourPlanet()
planetAge = genlib.dateYourPlanet(timePassed, planetName)
timeCounters = generatePlanetProfile(planetName, planetAge)
yearLength, dayLength = timeCounters
runTime(yearLength, dayLength, planetAge, planetName)

time.sleep(1.0)
stopTime = time.strftime("%c")
print(f"\nSimulation ended at : {stopTime}")
time.sleep(1.0)

print(f"\nAnd all was silent.\n")
time.sleep(2.0)
