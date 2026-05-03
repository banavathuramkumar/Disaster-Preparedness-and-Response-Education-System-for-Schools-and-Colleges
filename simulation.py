import random

def run_simulation():
    print("\n--- Disaster Simulation ---")
    
    scenarios = [
        {
            "question": "You feel an earthquake. What do you do?",
            "options": ["Run outside immediately", "Use elevator", "Drop, Cover, Hold"],
            "answer": 3
        },
        {
            "question": "Fire breaks out in a building. What is correct?",
            "options": ["Use lift", "Stay low and exit", "Hide in room"],
            "answer": 2
        },
        {
            "question": "Flood warning issued. What should you do?",
            "options": ["Go to basement", "Move to higher ground", "Ignore"],
            "answer": 2
        }
    ]

    score = 0
    random.shuffle(scenarios)

    for scenario in scenarios:
        print("\n" + scenario["question"])
        
        for i, option in enumerate(scenario["options"], 1):
            print(f"{i}. {option}")
        
        user_ans = int(input("Enter your choice: "))
        
        if user_ans == scenario["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    print(f"\nYour Score: {score}/{len(scenarios)}")
    
    if score == len(scenarios):
        print("Excellent! You are well prepared.")
    else:
        print("You need more practice.")