import random

def load_quiz_questions_mcq():
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["A. London", "B. Paris", "C. Berlin", "D. Rome"],
            "correct_answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["A. Mars", "B. Venus",  "C. Jupiter", "D. Saturn"],
            "correct_answer": "A"
        },
        {
            "question": "What is the largest mammal in the world?",
            "choices": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Gorilla"],
            "correct_answer": "B"
        },
        {
           "question": "Who is the founder of Alibaba?",
           "choices": ["A. Jack Ma", "B. Jeff Bezos", "C. Elon Musk", "D. Mark Zuckerberg"],
           "correct_answer":"A"
        },
        {
            "question": "Who is the founder of SpaceX?",
            "choices": ["A. Jack Ma","B. Jeff Bezos", "C. Elon Musk", "D. Mark Zuckerberg"],
            "correct_answer":"C"
        }
    ]
    return quiz_questions

def display_welcome_message_mcq():
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of multiple-choice questions.")
    print("Choose the correct option for each question.")

def present_quiz_questions_mcq(questions):
    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question['question']}")
        for choice in question['choices']:
            print(choice)

def evaluate_user_answer_mcq(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def display_feedback_mcq(is_correct, correct_answer):
    if is_correct:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

def calculate_final_score_mcq(score, total_questions):
    return f"\nYour final score is: {score}/{total_questions}"

def play_quiz_game_mcq():
    questions = load_quiz_questions_mcq()
    total_questions = len(questions)
    score = 0

    display_welcome_message_mcq()
    present_quiz_questions_mcq(questions)

    for question in questions:
        user_answer = input("\nEnter your answer (A, B, C, or D): ")
        is_correct = evaluate_user_answer_mcq(user_answer, question['correct_answer'])
        display_feedback_mcq(is_correct, question['correct_answer'])
        if is_correct:
            score += 1
            
    print(calculate_final_score_mcq(score, total_questions))


#    ****  below is the program for fill in the blanks *****

def load_quiz_questions_blanks():
    quiz_questions = [
        {
            "question": "what is the time duration of the national anthem of India ?",
            "correct_answer": "52 Seconds"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "correct_answer": "mars"
        },
        {
            "question": "Who is the prime minister of india in the year 2022 ?",
            "correct_answer": "Narendra modi"
        },
        {
            "question": "Who is the founder of Microsoft?",
            "correct_answer": "BillGates"
        },
        {
            "question": "Whom we call the God of cricket?",
            "correct_answer": "SachinTendulkar"
        }
    ]
    return quiz_questions

def display_welcome_message_blanks():
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of fill in the blanks questions.")
    print("give the correct answer for each question.")

def present_quiz_questions_blanks(questions):
    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question['question']}")

def evaluate_user_answer_blanks(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def display_feedback_blanks(is_correct, correct_answer):
    if is_correct:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

def calculate_final_score_blanks(score, total_questions):
    return f"\nYour final score is: {score}/{total_questions}"

def play_quiz_game_blanks():
    
    questions = load_quiz_questions_blanks()
    total_questions = len(questions)
    score = 0

    display_welcome_message_blanks()
    present_quiz_questions_blanks(questions)

    for question in questions:
        user_answer = input("\nenter u r ans ")
        is_correct = evaluate_user_answer_blanks(user_answer, question['correct_answer'])
        display_feedback_blanks(is_correct, question['correct_answer'])
        if is_correct:
            score += 1
    print(calculate_final_score_blanks(score, total_questions))

def mcq():
    print("its in the mcq block ")
    play_quiz_game_mcq()


    
def fill_in_the_blanks():
    print("its in the fill in the blanks")
    play_quiz_game_blanks()



if __name__ == "__main__":
    while True:
        ans=input(" Enter (a)For MCQ TYPE, (b)For FILL IN THE BLANKS : ")
        if ans == "a":
            mcq()
        elif ans=="b":
            fill_in_the_blanks()
        else:
            print("please Enter a valid key either (a) or (b) ")
            pass    
    
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing. Goodbye!")
            break   