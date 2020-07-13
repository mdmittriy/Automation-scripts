# quiz_gen.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
from pathlib import Path

# The quiz data. Keys are states and values are their capitals.
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}
# Generate 35 quiz files.

# Getting input done and destination here

p = input("Where to store?")
dest = Path(p)
while not dest.is_dir():
    p = input("One more time, where to store?")
    dest = Path(p)


dest = Path(p, "Newly_created_folder_of_quizzes_by_my_program")
dest.mkdir()

i = 0
for quiz_num in range(30):
    i += 1
    fileName = "" + str(i) + ".txt"
    newDest = Path(dest, fileName)
    quizFile = open(newDest, "a")
    for quiz_num in range(10):
        country, capital = random.choice(list(capitals.items()))
        listOfAnswers = [
            capital,
            random.choice(list(capitals.values())),
            random.choice(list(capitals.values())),
            random.choice(list(capitals.values())),
        ]
        nums = [0, 1, 2, 3]
        random.shuffle(nums)
        quizTest = (
            ""
            + "What is the capital of "
            + country
            + "?\n  "
            + listOfAnswers[nums[0]]
            + "\n  "
            + listOfAnswers[nums[1]]
            + "\n  "
            + listOfAnswers[nums[2]]
            + "\n  "
            + listOfAnswers[nums[3]]
            + "\n"
        )
        quizFile.write(quizTest)
