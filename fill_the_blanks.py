# -*- coding: utf-8 -*-
# Project - Code Your Own Quiz (P2 of Introduction to Programming)
# Author: Fausto Rodrigues, Dec 2016

# For each difficulty level, there is a dictionary with the quiz sentence(s),
# the wildcard labels and the respective answers (a string and two lists).
# I am not sure yet if this should be just one dictionary, or even another file

# Hard difficult quiz
hard = {
    'quiz': """The first European to colonize Brazil was Pedro Álvares __1__
             on April 22, 1500 under the sponsorship of the Kingdom of
             Portugal. From the 16th to the early 19th century, Brazil was a
             colony and apart of the __2__ Empire. The country expanded
             south along the coast and west along the Amazon and other inland
             rivers from the original 15 donatary captaincy colonies
             established on the northeas Atlantic coast east of the Tordesillas
             Line of 1494 (approximately the 46th meridian west) that divided
             the __2__ domain to the east from the Spanish domain to the
             west. The country's borders were only finalized in the early 20th
             century.""",
    'questions': ["__1__", "__2__", "__3__", "__4__"],
    'answers': ["Cabral", "Portuguese"]
}

# Medium difficult quiz
medium = {
    'quiz': ("It is likely that the word \"__1__\" comes from the Portuguese "
             "word for __1__wood, a __2__ that once grew plentifully along the "
             "__1__ian coast. In Portuguese, __1__wood is called \"pau-brasil\", "
             "with the word brasil commonly given the etymology \"__3__ like an "
             "ember\", formed from Latin brasa (\"ember\") and the suffix -il "
             "(from -iculum or -ilium). As __1__wood produces a deep __3__ dye, "
             "it was highly valued by the __4_ cloth industry and was the "
             "earliest commercially exploited product from __1__. Throughout "
             "the 16th century, massive amounts of __1__wood were harvested "
             "by indigenous peoples (mostly Tupi) along the __1__ian coast, "
             "who sold the timber to __4__ traders (mostly Portuguese, but "
             "also French) in return for assorted __4__ consumer goods."),
    'questions': ["__1__", "__2__", "__3__", "__4__"],
    'answers': ["Brazil", "tree", "red", "European"]
}

# Easy difficult quiz
easy = {
    'quiz': """Brazil, officially the Federative Republic of Brazil (República Federativa do Brasil), is the largest country in both South __1__ and Latin __1__. As the world's fifth-largest country by both area and population, it is the largest country to have __2__ as an official language and the only one in the __1__s. Bounded by the __3__ Ocean on the east, Brazil has a coastline of 7,491 km (4,655 mi). It borders all other South __1__n countries except Ecuador and Chile and covers 47.3%% of the __4__'s land area.""",
    'questions': ["__1__", "__2__", "__3__", "__4__"],
    'answers': ["America", "Portuguese", "Atlantic", "continent"]
}


def play(quiz, max_attempts=4):
    """For the selected quiz it prompts the user for the correct answers in
    order, it returns the result from the play_again method"""
    i, attempts = 0, 0
    questions, answers = quiz['questions'], quiz['answers']

    print "\n Let's begin! \n\n", quiz['quiz']

    while i < len(questions):
        if questions[i] in quiz['quiz']:
            question = "What the correct word in for %s? You still have %i attempts: " % (questions[i], max_attempts - attempts)
            answer = raw_input(question).lower()

            if answer == answers[i].lower():
                print "That is correct! The answer was %s. The updated quiz is:" % answers[i]
                quiz['quiz'] = quiz['quiz'].replace(questions[i], answers[i])

                i += 1
                attempts = 0
                print "\n", quiz['quiz']
            else:
                attempts += 1
                if attempts >= max_attempts:
                    print "\nOh no! You took all your chances!"
                    return play_again()
                else:
                    print "\n Sorry, but %s in not the correct answer for %s" % (answer, questions[i])

    print "\n" + "Well done! Go have a beer and play some more!"

    return play_again()


def play_again():
    """Prompts if the user wants to keep playing. Start the bootstrap proccess
    again or returns a goodby message"""
    user_input = raw_input("\n" + "Would you like to play again ((y)es):").upper()

    if user_input == "YES" or user_input == "Y":
        return bootstrap()
    else:
        return '\n' + "Thanks for playing. Goodbye!" + '\n'


def bootstrap():
    """Bootstrap the game prompting the user for the dificult level,
    returns the game result when selected correctly"""

    # Main loop for the game
    try:
        while True:
            user_input = raw_input("(E)asy, (M)edium or (H)ard):").upper()
            if user_input == "E":
                return play(easy)
            elif user_input == "M":
                return play(medium)
            elif user_input == "H":
                return play(hard)

            print '\n' + "Invalid input, please choose one of the valid options:\n"
    except KeyboardInterrupt:
        print "\nGoodbye!"
        pass


print(" --/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\--\n"
      "|  Welome to the Brazilian Fill the Blanks Quiz!  |\n"
      "|                                                  |\n"
      "| Brought to you by Fausto                         |\n"
      "|                                                  |\n"
      "| Pick the level you want to play:                 |\n"
      " ------------------------------------------------- ")
bootstrap()
