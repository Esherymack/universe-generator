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

# class Logger allows a log to be generated as the console prints as well
# stolen from here: https://stackoverflow.com/questions/14906764/how-to-redirect-stdout-to-both-file-and-console-with-scripting
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("genlog.txt", "w")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        # flush method is for python 3 compatibility
        # handles flush command by doing Nothing
        # extra behaviour may be specified here
        pass

# global vowel list for some reason
vowels = list('aeiou')
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
            if determineFate():
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

# Determines the fates of successful star generations.
def determineFate():
    chance = random.random()
    if chance <= 0.5:
        print("Star cluster failed!")
        return False
    else:
        print("Star cluster survived!")
        return True

# For some reason I decided this was necessary to reduce the scale of what I'm working with
def filterObservableUniverse(numGalaxies):
    observable = (4 * numGalaxies) // 100
    print("\nThe observable universe is only four percent of the actual universe.")
    print(f"This means that the observable universe generated contains {observable} galaxies.")
    return observable

# Randomly generates the number of possible habitable planets
def filterHabitablePlanets(numObserved):
    randomPercentage = round(random.uniform(1, 45), roundPrecision)
    print(f"\nIn the observable universe, roughly {randomPercentage}% of all planets are habitable.")
    randomPlanets = random.randint(100000, 100000000)
    randomHabitablePlanets = int((randomPercentage * randomPlanets) // 100)
    print(f"Given that there are {randomPlanets} planets in the observable universe, this implies that there are {randomHabitablePlanets} habitable planets in the observable universe.")

# Randomly generates a name for the "home planet"
def nameYourPlanet():
    randomstr = gen_word(random.randint(1, 5), random.randint(1,7))
    print("\nLuckily, we find ourselves at one of that vast number.")
    print(f"The name of your home planet is {randomstr}.")
    return randomstr

# Determines the date of and location of your planet.
def dateYourPlanet(eons, planetstr):
    systemName = gen_word(random.randint(1, 5), random.randint(1,7))
    planetAge = str(round(random.uniform(0.01, eons), roundPrecision))
    print(f"\nYour planet, {planetstr}, formed roughly {planetAge} billion years ago in the cluster named {systemName}.")
    return planetAge


##### Utility Functions Below This Line #####
# ^ lol i stopped caring

# Generates planet profile after planet is named.
def generatePlanetProfile(name, age):
    print(f"\nPlanet name is {name}.")
    print(f"Planet age is {age} billion years.")
    description = getDescriptor()
    description = ', '.join(description)
    planet_type = random.random()
    if planet_type < 0.5:
        print(f"{name} is a rocky planet.")
        generatePlanetBiomes()
        print(f"The terrain of {name} is {description}.")
    else:
        print(f"{name} is a gaseous planet.")
        print(f"The plasma oceans of {name} are {description}.")
    day_length = generateDayLength()
    print(f"The length of a day on {name} is {day_length} hours.")
    year_length_hours = generateYearLength()
    year_length_days = round(year_length_hours / day_length, roundPrecision)
    print(f"Given that a year is {year_length_hours} hours long, there are {year_length_days} days in a year on {name}.")
    input("\nPress enter to continue...\n")
    return (year_length_days, day_length)

# Determines the number and kinds of biomes the planet has.
def generatePlanetBiomes():
    print("Because the planet has land, it has developed several biomes. They are: ")
    # must develop at least two biomes
    numBiomes = random.randint(2, 22)
    # biomes.dat contains biomes as outlined in the Ecosystems of the World, ed. Goodall (1974)
    biomes = open('biomes.dat')
    biomeList = biomes.read().splitlines()
    size = len(biomeList)
    for i in range(0, numBiomes):
        # ensures that the biome selection doesn't pick the same biome twice
        size = size - 1
        choice = random.randint(0, size)
        return_choice = biomeList.pop(choice)
        print(f"Biome: {return_choice}")
    biomes.close()

# Determines the length of a day on a planet.
# I really didn't want to make up arbitrary mass values, so I'm just randomly generating this
def generateDayLength():
    return round(random.uniform(5.0, 50.0), roundPrecision)

# Determines the length of a year on the planet.
# Generates time based on distance from home star.
# See this article: http://www.planetarybiology.com/calculating_habitable_zone.html
# (yes, these measurements come in Earth Units(TM) for our humanly convenience)
def generateYearLength():
    # get the class and name of the home star
    starClass = generateStarClass()
    starColor = getColor(starClass)
    starName = gen_word(random.randint(1, 5), random.randint(1,7))
    print(f"The class of the host star, {starName}, is {starClass}.")
    print(f"{starName} is {starColor} in color. How beautiful it is!")
    # arbitrary but some reasoning involved to get the luminosity of the star.
    luminosity = averageLuminosity(starClass)
    # simple, divide sqrt luminosity by 1.1 for inner boundary and sqrt luminosity by 0.53 for outer
    inner_boundary = round(np.sqrt(luminosity / 1.1), roundPrecision)
    outer_boundary = round(np.sqrt(luminosity / 0.53), roundPrecision)
    # pick a random spot in that range for planet distance from star
    planet_distance = round(random.uniform(inner_boundary, outer_boundary), roundPrecision)
    print(f"The planet is located {planet_distance} AUs away from {starName}.")
    # use Kepler's third law to calculate the length of a year
    # T^2 = 4pi^2 / G(Mstar + Mplanet)(R^3)
    # where T is the time period, G is the Newtonian gravitational constant, M represents the mass, and R is the semi-major axis of the elliptical orbit
    # G is apparently 6.67x10^-11 newton meters squared per kilogram squared, so we're using that (0.0000000000667, or 6.67e-11 for simplicity)
    # We're also assuming that the planet's mass is negligible compared to the host star (as are most), for ease.
    newtonianGravitationConstant = 6.67e-11
    lengthYearSquared = round(np.sqrt((4*np.pi**2)/(newtonianGravitationConstant*averageMass(starClass))*planet_distance**3), roundPrecision)
    # For some reason, I did this such that the universe assumes a standard year is 336 days (12 months of exactly 28 days each).
    # This is why I divide by 336 here.
    standardYearLength = 336 # days
    return round(lengthYearSquared/standardYearLength, roundPrecision)


# Generates the class of the home star
def generateStarClass():
    # a star can be class O, B, A, F, G, K, or M
    classChoice = ['O', 'B', 'A', 'F', 'G', 'K', 'M']
    return random.choice(classChoice)
# Retrieves average luminosity of the home star
def averageLuminosity(sc):
    return {
        'O' : 1400000 + random.uniform(-9999, 999),
        'B' : 20000   + random.uniform(-999, 99)  ,
        'A' : 80      + random.uniform(-4, 4)      ,
        'F' : 6       + random.uniform(-2, 2)      ,
        'G' : 1.2     + random.uniform(-0.09, 0.09)  ,
        'K' : 0.4     + random.uniform(-0.04, 0.04),
        'M' : 0.04    + random.uniform(-0.0009, 0.0009)
    }[sc]
# Retrieves average mass of home star
def averageMass(sc):
    return {
        'O' : 60,
        'B' : 18,
        'A' : 3.2,
        'F' : 1.7,
        'G' : 1.1,
        'K' : 0.8,
        'M' : 0.3
    }[sc]
# Retrieves color of home star
def getColor(sc):
    return {
        'O' : 'Blue',
        'B' : 'Blue',
        'A' : 'Blue',
        'F' : 'White',
        'G' : 'Yellow',
        'K' : 'Orange',
        'M' : 'Red'
    }[sc]

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
    planetGeologicAges = generateAgeNames()
    planetGeologicAges = ', '.join(planetGeologicAges)
    print(f"The five ages of {name} are: {planetGeologicAges}")

# Generates events of first Primary Age
def generateFirstAge():
    pass

# Generates events of second Primary Age
def generateSecondAge():
    pass

# Generates events of third Primary Age
def generateThirdAge():
    pass

# Generates events of fourth Primary Age
def generateFourthAge():
    pass

# Generates events of fifth Primary Age
def generateFifthAge():
    pass

# Generates five age names
def generateAgeNames():
    numberOfAges = 5
    agesList = []
    for i in range(0, numberOfAges):
        ageStr = gen_word(random.randint(1, 5), random.randint(1,7))
        agesList.append(ageStr)
    return agesList
# Fetches the name of an Age, an Eon, a Period, or an Epoch.
def geologicTimeScale(s):
    timeString = gen_word(random.randint(1, 10), random.randint(1, 10))
    return {
        'Age'    : f"The age of {timeString} has begun!"   ,
        'Eon'    : f"The eon of {timeString} has begun!"   ,
        'Period' : f"The period of {timeString} has begun!",
        'Epoch'  : f"The epoch of {timeString} has begun!"
    }[s]
# End of the Planet's Life
def endOfPlanet():
    pass

# Generates primary species ("player species")
def generatePrimarySpecies():
    pass
# Generates profie of primary species
def generateSpeciesProfile():
    pass
# Triggers evolution
def triggerEvolve():
    pass

# Generates non-described species
def generateNonDescribedSpecies():
    pass

# Generates random alternate species at given times with random descriptions
def generateRandomSpecies():
    pass

# Generates extinction events
def generateExtinctionEvent():
    pass

# Retrieve descriptive adjective for landscape from adjectives.dat
def getDescriptor():
    numDescriptors = random.randint(2, 4)
    adjectives = open('adjectives.dat')
    adjectivesList = adjectives.read().splitlines()
    size = len(adjectivesList)
    description_list = []
    for i in range(0, numDescriptors):
        size = size - 1
        descriptor = random.randint(0, size)
        return_descriptor = adjectivesList.pop(descriptor)
        description_list.append(return_descriptor)
    adjectives.close()
    return description_list

# http://pythonfiddle.com/random-word-generator/ because I'm lazy and didn't feel like figuring this out myself
def gen_word(min, max):
    word = ''
    syllables = min + int(random.random() * (max-min))
    for i in range(0, syllables):
        word += gen_syllable()
    return word.capitalize()
def gen_syllable():
    ran = random.random()
    if ran < 0.333:
        return word_part('v')+ word_part('c')
    if ran < 0.666:
        return word_part('c') + word_part('v')
    return word_part('c') + word_part('v') + word_part('c')
def word_part(type):
    if type is 'c':
        return random.sample([ch for ch in list(string.ascii_lowercase) if ch not in vowels], 1)[0]
    if type is 'v':
        return random.sample(vowels, 1)[0]

##### Function Calls Below This Line #####

# who needs a main function lol

# start log now
sys.stdout = Logger()

systemTime = time.strftime("%c")
print(f"Universe spawned at : {systemTime}")
valueNumbers = spawnSystems()
totalGalaxies, timePassed = valueNumbers
observed = filterObservableUniverse(totalGalaxies)
filterHabitablePlanets(observed)
planetName = nameYourPlanet()
planetAge = dateYourPlanet(timePassed, planetName)
timeCounters = generatePlanetProfile(planetName, planetAge)
yearLength, dayLength = timeCounters
runTime(yearLength, dayLength, planetAge, planetName)

time.sleep(1.0)
stopTime = time.strftime("%c")
print(f"\nSimulation ended at : {stopTime}")
time.sleep(1.0)

print(f"\nAnd all was silent.\n")
time.sleep(2.0)
