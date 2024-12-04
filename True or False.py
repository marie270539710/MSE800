import sqlite3
import random
import request

# Initialize database
conn = sqlite3.connect('game_database.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                  (id INTEGER PRIMARY KEY, user_id INTEGER, score INTEGER, total_questions INTEGER)''')

# Question data
question_data = [
    {
        "question": "Nintendo started out as a playing card manufacturer.",
        "correct_answer": "True"
    },
    {
        "question": "The retail disc of Tony Hawk's Pro Skater 5 only comes with the tutorial.",
        "correct_answer": "True"
    },
    {
        "question": "In the 'Shrek' film franchise, Donkey is played by Eddie Murphy.",
        "correct_answer": "True"
    },
    {
        "question": "Hippopotomonstrosesquippedaliophobia is the irrational fear of long words.",
        "correct_answer": "True"
    },
    {
        "question": "The movie 'The Nightmare before Christmas' was all done with physical objects.",
        "correct_answer": "True"
    },
    {
        "question": "Soulja Boy's - Crank That won a Grammy for Best Rap Song in 2007.",
        "correct_answer": "False"
    },
    {
        "question": "The US emergency hotline is 911 because of the September 11th terrorist attacks.",
        "correct_answer": "False"
    },
    {
        "question": "The Republic of Malta is the smallest microstate worldwide.",
        "correct_answer": "False"
    },
    {
        "question": "In 'Super Mario 64', collecting 100 coins on a level will give you a 1-UP.",
        "correct_answer": "False"
    },
    {
        "question": "The logo for Snapchat is a Bell.",
        "correct_answer": "False"
    }
]


def register_user():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    return cursor.lastrowid


def play_game(user_id):
    num_questions = int(input("How many questions would you like to answer? (1-10): "))
    # Ensure number is between 1 and 10
    num_questions = min(max(num_questions, 1), 10)  

    score = 0
    random.shuffle(question_data)
    selected_questions = question_data[:num_questions]

    for question in selected_questions:
        print("\n" + question["question"])
        answer = input("True or False? ").capitalize()

        if answer == question["correct_answer"]:
            print("You got it right!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['correct_answer']}.")

    print(f"\nGame over! Your score: {score}/{num_questions}")

    cursor.execute("INSERT INTO scores (user_id, score, total_questions) VALUES (?, ?, ?)",
                   (user_id, score, num_questions))
    conn.commit()


def main():
    print("Welcome to the ABC Fish On's True or False Game!")
    user_id = register_user()
    play_game(user_id)


if __name__ == "__main__":
    main()

conn.close()
