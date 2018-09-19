# library for AAWQ universe gen

# library imports
import random
import string
import time
import sys
import numpy as np

import wordgen
import ansi_color as ac

##### Globals #####

# global vowel list for some reason
vowels = list('aeiou')
# global round precision
roundPrecision = 2

# there are always at least 1 continents and 1 oceans
continents = 1
oceans = 1

##### Generation #####

# Determines the fates of successful star generations.
def determineFate():
    chance = random.random()
    if chance <= 0.5:
        print("Star cluster failed!")
        return False
    else:
        print("Star cluster survived!")
        return True

##### Observable Universe #####

# For some reason I decided this was necessary to reduce the scale of what I'm working with
def filterObservableUniverse(numGalaxies):
    observable = (4 * numGalaxies) // 100
    print("\nThe observable universe is only four percent of the actual universe.")
    print(f"This means that the observable universe generated contains {observable} galaxies.")
    return observable

##### Vaguely Planet Related Functions #####

# Randomly generates the number of possible habitable planets
def filterHabitablePlanets(numObserved):
    randomPercentage = round(random.uniform(1, 45), roundPrecision)
    print(f"\nIn the observable universe, roughly {randomPercentage}% of all planets are habitable.")
    randomPlanets = random.randint(100000, 100000000)
    randomHabitablePlanets = int((randomPercentage * randomPlanets) // 100)
    print(f"Given that there are {randomPlanets} planets in the observable universe, this implies that there are {randomHabitablePlanets} habitable planets in the observable universe.")
# Randomly generates a name for the "home planet"
def nameYourPlanet():
    randomstr = wordgen.gen_word(random.randint(1, 5), random.randint(1,7))
    print("\nLuckily, we find ourselves at one of that vast number.")
    print(f"The name of your home planet is {randomstr}.")
    return randomstr

##### Planet Time Functions #####

# Determines the date of and location of your planet.
def dateYourPlanet(eons, planetstr):
    systemName = wordgen.gen_word(random.randint(1, 5), random.randint(1,7))
    planetAge = str(round(random.uniform(0.01, eons), roundPrecision))
    print(f"\nYour planet, {planetstr}, formed roughly {planetAge} billion years ago in the cluster named {systemName}.")
    moons = generateMoons()
    moonNames = []
    for i in range(0, moons):
        moon_name = wordgen.gen_word(random.randint(1, 5), random.randint(1,7))
        moonNames.append(moon_name)
    moonList = ', '.join(moonNames)
    print(f"\n{planetstr} has {moons} moons. They are named: {moonList}")
    return planetAge
# Determines the length of a year on the planet.
# Generates time based on distance from home star.
# See this article: http://www.planetarybiology.com/calculating_habitable_zone.html
# (yes, these measurements come in Earth Units(TM) for our humanly convenience)
def generateYearLength():
    # get the class and name of the home star
    starClass = generateStarClass()
    starColor = getColor(starClass)
    starName = wordgen.gen_word(random.randint(1, 5), random.randint(1,7))
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
    # For some reason, I did this such that the universe assumes a "standard year" is 336 days (12 months of exactly 28 days each).
    # This is why I divide by 336 here.
    standardYearLength = 336 # days
    return round(lengthYearSquared/standardYearLength, roundPrecision)
# Determines the length of a day on a planet.
# I really didn't want to make up arbitrary mass values, so I'm just randomly generating this
def generateDayLength():
    return round(random.uniform(5.0, 50.0), roundPrecision)
# Generate any moons for your planet, if any exist
def generateMoons():
    numMoons = random.randint(0, 5)
    return numMoons

# Generates elements present in the planet. Element names are randomly generated; generates 100-200 elements.
# TODO : Allow menus during generation
# ## TODO : This chart may be accessed at any time with command :ptable ##
# Currently saves elements to external list, "elements.dat"

### Division of Elements ###
###     The elements present in the generated universe are distributed through states and types similarly to
###     how they are on Earth. This means to say, that there are 11 (effectively, 10, if you're the type to
###     exclude unknown elements) types of element and they are divided up as follows:
###             5.9% are in class 0 ("noble gasses")
###             5.9% are in class 1 ("nonmetals")
###             5.1% are in class 2 ("alkali metals")
###             5.1% are in class 3 ("alkaline earth metals")
###             29.7% are in class 4 ("transition metals")
###             7% are in class 5 ("post-transition metals")
###             5.1% are in class 6 ("metalloids")
###             4.24% are in class 7 ("halogens")
###             13% are in class 8 ("lanthanides")
###             13% are in class 9 ("actinides")
###             7% are in class 10 and comprise the "unknown" elements in the universe.
###
###    Additionally dividing the elements:
###             76.3% exist in a solid state under normal conditions
###             1.7% exist in a liquid state under normal conditions
###             10.2% exist in a gaseous state under normal conditions
###             A further 11.86% exist in an uknown state under normal conditions.
def generateElements():
    # generate the elements - random integer between 100 and 200
    numElts = random.randint(100,200)
    f = open('elements.dat', 'w')
    for i in range(0, numElts):
        en = wordgen.gen_word(random.randint(1, 6), random.randint(1, 6))
        # if a generated word is longer than 5, then it gets the suffix "-ium" appended to the end.
        if len(en) > 5:
            en = en + "ium"
        # otherwise it stays as it is.
        # this has no real science behind it, it's just for fun.
        f.write(en)
    print(f"\n{numElts} elements generated.")
    print("These elements are broken down into: ")
    eltType = []
    for i in range(0, 10):
        et = wordgen.gen_word(random.randint(1,4), random.randint(1,6))
        print(f"{et}s, ")
        eltType.append(et)
    numSolids = int((numElts * 76.3) // 100)
    print(f"{numSolids} elements exist in a solid state under normal conditions.")
    numLiquids = int((numElts * 1.7) // 100)
    print(f"{numLiquids} elements exist in a liquid state under normal conditions.")
    numGasses = int((numElts * 10.2) // 100)
    print(f"{numGasses} elements exist in a gaseous state under normal conditions.")
    numUn = int((numElts * 11.86) // 100)
    print(f"{numUn} elements exist in an unknown state under normal conditions.")
    f.close()
    print("\n")

# Generates the atmosphere content of a planet.
# Must be composed of gasses.
###     Random floating point number between 75 and 78 goes to primary element -
###     unless element is only element comprising an atmosphere.
###     If B, 20-21% of atmosphere is delegated to element B.
###     Any further elements are denoted as "trace elements"
def generateAtmosphere():
    pass

# Generates land or plasma elemental construction of planet.
# May be composed of anything.
###     A rocky planet has five primary elements making up its landmasses
###     A gaseous planet has two primary elements making up its plasma ocean.
def generateLandElements():
    pass
# Generates elements necessary for life on the planet.
# May be composed of anything.
###     There are 11 primary elements necessary for life.
###     There are 22 trace elements necessary for life.
def generateNecessaryForLife():
    pass

##### Descriptors and Biomes #####

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
# Retrieve descriptive adjective for landscape from adjectives.dat
def getLandDescriptor():
    numDescriptors = random.randint(2, 4)
    adjectives = open('planet_adjectives.dat')
    adjectivesList = adjectives.read().splitlines()
    size = len(adjectivesList)
    description_list = []
    for i in range(0, numDescriptors):
        size = size - 1
        descriptor = random.randint(0, size)
        return_descriptor = adjectivesList.pop(descriptor)
        description_list.append(return_descriptor)
    adjectives.close()
    weather = open('weather.dat').read().splitlines()
    weather_desc = random.choice(weather)
    print(f"The weather is {weather_desc}.")
    return description_list
# Retrieve descriptive adjective for creature
def getCreatureDescriptor():
    pass
# Retrieve descriptive adjective for personality
def getCreaturePersonality():
    pass

##### Star Functions #####

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

##### Planet GTS Ages #####
# Generates five age names
def generateAgeNames(numberOfAges):
    agesList = []
    for i in range(0, numberOfAges):
        ageStr = wordgen.gen_word(random.randint(1, 5), random.randint(1,7))
        agesList.append(ageStr)
    return agesList
# Fetches the name of an Age, an Eon, a Period, or an Epoch.
def geologicTimeScale(s):
    timeString = wordgen.gen_word(random.randint(1, 10), random.randint(1, 10))
    return {
        'Age'    : f"The age of {timeString} has begun!"   ,
        'Eon'    : f"The eon of {timeString} has begun!"   ,
        'Period' : f"The period of {timeString} has begun!",
        'Epoch'  : f"The epoch of {timeString} has begun!"
    }[s]

# Determines the fate of a formed landmass.
def determineLandmassFate():
    chance = random.random()
    if chance <= 0.5:
        return False
    else:
        return True

# Generates events of first Primary Age
# During the first primary age, there is a very very low chance of life spawning - 0.000001% (here listed as 1e-6)
# this is because the planet has really just formed.
def generateFirstAge(planetGeologicAges, planetAge):
    firstAge = planetGeologicAges[0]
    print(f"The first age, {firstAge}, has begun!")
    lengthOfAge = round(planetAge / 5, roundPrecision)
    remainingTime = round(planetAge - lengthOfAge, roundPrecision)
    print(f"The length of {firstAge} is {lengthOfAge} billion years.")
    generatePlanetTerrain(lengthOfAge, 3)
    chanceOfLifeRoll(1e-6)
    time.sleep(1.0)
    return remainingTime

# Generates events of second Primary Age
def generateSecondAge(planetGeologicAges, planetAge, lastAgeLength):
    secondAge = planetGeologicAges[1]
    print(f"The second age, {secondAge}, has begun!")
    planet_newAge = planetAge - lastAgeLength
    lengthOfAge = round(planet_newAge / 4, roundPrecision)
    remainingTime = round(planet_newAge - lengthOfAge, roundPrecision)
    print(f"The length of {secondAge} is {lengthOfAge} billion years.")
    generatePlanetTerrain(lengthOfAge, 2)
    time.sleep(1.0)
    return remainingTime

# Generates events of third Primary Age
def generateThirdAge(planetGeologicAges, planetAge, lastAgeLength):
    thirdAge = planetGeologicAges[2]
    print(f"The third age, {thirdAge}, has begun!")
    planet_newAge = planetAge - lastAgeLength
    lengthOfAge = round(planet_newAge / 3, roundPrecision)
    remainingTime = round(planet_newAge - lengthOfAge, roundPrecision)
    print(f"The length of {thirdAge} is {lengthOfAge} billion years.")
    generatePlanetTerrain(lengthOfAge, 2)
    time.sleep(1.0)
    return remainingTime

# Generates events of fourth Primary Age
def generateFourthAge(planetGeologicAges, planetAge, lastAgeLength):
    fourthAge = planetGeologicAges[3]
    print(f"The fourth age, {fourthAge}, has begun!")
    planet_newAge = planetAge - lastAgeLength
    lengthOfAge = round(planet_newAge / 2, roundPrecision)
    remainingTime = round(planet_newAge - lengthOfAge, roundPrecision)
    print(f"The length of {fourthAge} is {lengthOfAge} billion years.")
    generatePlanetTerrain(lengthOfAge, 1)
    time.sleep(1.0)
    return remainingTime

# Generates events of fifth Primary Age
def generateFifthAge(planetGeologicAges, planetAge, lastAgeLength):
    fifthAge = planetGeologicAges[4]
    print(f"The fifth age, {fifthAge}, has begun!")
    planet_lastAge = planetAge - lastAgeLength
    print(f"The fifth age ranges from {planet_lastAge} billion years ago to present.")
    generatePlanetTerrain(planet_lastAge, 0)
    time.sleep(1.0)

# alternate func for generating a gas planet's timescale
def generateGasPlanet(planetGeologicAge, planetAge):
    gtsAge = planetGeologicAge[0]
    print(f"The age of {gtsAge} has begun!")
    time.sleep(1.0)

# generate planet terrain (continents, oceans)
# weight modifier adjusts tendency towards successful/failed continents/oceans
def generatePlanetTerrain(lengthOfAge, weight):
    global continents
    global oceans
    while(lengthOfAge >= 0):
        chance = random.randint(0, 2)
        if chance==1:
            print("The world is changing.")
            if determineLandmassFate():
                continents += random.randint(0, 2) * weight
                oceans += random.randint(0, 2) * weight
            else:
                continents -= continents // 2 * weight
                oceans -= continents // 2 * weight
        else:
            print("Time passes.")
            lengthOfAge -= random.uniform(0.0, 1.0)
        time.sleep(1.0)
    print(f"{continents} continents exist, and {oceans} oceans exist.")

# End of the Planet's Life
def endOfPlanet():
    pass

# The Chance of Life roll is for determining when and if life spawns on a planet.
def chanceOfLifeRoll(weight):
    return random.uniform(0, 1) * weight

##### LIFE FUNCTIONS #####

# Generates primary element of life on planet (Carbon or Silicon)
def generateLifeCtor():
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

# Generates "player"
def generatePlayer():
    pass
# Generates "player" appearance
def generatePlayerAppearance():
    pass
# Generates "player" personality
def generatePlayerPersonality():
    pass
# Generates "player" relationships
def generatePlayerRelationships():
    pass
# Generates "player" religion
def generatePlayerReligion():
    pass

# Generates non-described species
def generateNonDescribedSpecies():
    pass

# Generates random alternate species at given times with random descriptions
def generateRandomSpecies(type):
    pass

# Generates extinction events
def generateExtinctionEvent():
    pass
