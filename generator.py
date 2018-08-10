# Universe Generator by Madison Tibbett
# a product of infinite boredom.

# library imports
import random
import numpy as np # TODO: don't need this quite yet but will when graphics
import string
import time

# global vowel list for some reason
vowels = list('aeiou')

# chance to spawn universe is 1 in 4. don't know why. stop asking questions.
def spawnUniverse():
    while True:
        chance = random.randint(1, 4)
        if chance == 1:
            print("Universe spawned!")
            break;
        else:
            print("Universe did not spawn.")
            time.sleep(1)

# after a universe successfully spawns, need to populate it with stars and nebulae.
# There is always at least one star in the system.
# Generation ends after system meets or exceeds 100 trillion stars.
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
            if determineFate() == True:
                # if the stars survive, then increase by a power 1 through 4, randomly
                stars += stars**random.randint(1,4)
            else:
                # otherwise, decrease by division. If the star count drops below 0, reset to 1.
                stars -= stars//random.randint(1,5)
                if stars <= 0:
                    stars = 1
            print("Total Stars: " + str(stars))
            if stars >= 1000000000000000000000:
                # there are roughly 100 billion stars per galaxy, so easy division
                galaxies = stars // 100000000000000
                # nebulae form in clumps in this generator, so randomly some number between 1000 and 1999 * total number of nebulae rolled.
                nebula = nebula*(random.randint(0, 999) + 1000)
                print("Total galaxy formations: " + str(galaxies))
                print("Total nebula formations: " + str(nebula))
                # Represents billions of years.
                print("Billions of years past: " + str(timepassed))
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
    print("The observable universe is only four percent of the actual universe.")
    print("This means that the observable universe generated contains " + str(observable) + " galaxies.")
    return observable

# Randomly generates the number of possible habitable planets
def filterHabitablePlanets(numObserved):
    randomPercentage = random.uniform(1, 45)
    print("In the observable universe, roughly " + str(randomPercentage) + " percent of all planets are habitable.")
    randomPlanets = random.randint(100000000000, 100000000000000)
    randomHabitablePlanets = (randomPercentage * randomPlanets) // 100
    print("Given that there are " + str(randomPlanets) + " planets in the observable universe, this implies that there are " + str(randomHabitablePlanets) + " habitable planets in the observable universe.")

# Randomly generates a name for the "home planet"
def nameYourPlanet():
    randomstr = gen_word(random.randint(1, 10), random.randint(1,10))
    print("Luckily, we find ourselves at one of that vast number.")
    print("The name of your home planet is " + randomstr + ".")
    return randomstr

# Determines the date of and location of your planet.
def dateYourPlanet(eons, planetstr):
    systemName = gen_word(random.randint(1, 10), random.randint(1,10))
    planetAge = str(random.uniform(0.01, eons))
    print("Your planet, " + planetstr + ", formed roughly " + planetAge + " billion years ago in the cluster named " + systemName + ".")
    return planetAge

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

# who needs a main function lol
spawnUniverse()
valueNumbers = spawnSystems()
totalGalaxies, timePassed = valueNumbers
observed = filterObservableUniverse(totalGalaxies)
filterHabitablePlanets(observed)
planetName = nameYourPlanet()
planetAge = dateYourPlanet(timePassed, planetName)

print("Done")
