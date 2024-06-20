from random import shuffle

# Define a dictionary of questions and answers
flashcards = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the scientific name for a human?": "Homo sapiens",
    "What is the chemical symbol for water?": "H2O",
    "Who painted the Mona Lisa?": "Leonardo da Vinci"
}

# Function to display a flashcard
def show_flashcard(question, answer):
  print(question)
  input("Press Enter to see the answer...")
  print(answer)

# Function to play the flashcard game
def play_game():
  # Shuffle the flashcards for random order
  question_list = list(flashcards.keys())
  shuffle(question_list)

  # Loop through each flashcard
  for question in question_list:
    show_flashcard(question, flashcards[question])

    # Ask user to continue
    continue_playing = input("Next card? (y/n): ").lower()
    if continue_playing != 'y':
      break

# Start the game
play_game()

print("\nThanks for playing!")
