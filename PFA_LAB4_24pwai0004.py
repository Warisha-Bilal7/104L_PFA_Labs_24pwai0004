import random
secret=random.randint(1,50)
attempts=0
max_tries=7
won=False
print("~~~~~~AI GUESSING GAME~~~~~~")
print(f"Goal: Guess the number (1-50) in {max_tries} attempts")
while attempts < max_tries:
    # Ask for user guess
    user_input = input(f"\n[Attempt {attempts + 1}/{max_tries}] Enter your guess: ")
    
    # Validate that input is a digit and within the 1-50 range
    if not user_input.isdigit() or not (1 <= int(user_input) <= 50):
        print(">> Invalid input! Please enter a whole number between 1 and 50.")
        continue
    
    guess = int(user_input)
    attempts += 1 # Increment the counter after a valid guess
    
    # 3. Use if/elif/else for logic and hints
    if guess == secret:
        # Success message with AI training level logic
        print(f"\n🎯 Result: You win in {attempts} attempts!")
        print(f"AI training level: Beginner {'→ Intermediate' if attempts > 1 else '→ PRO'}")
        won = True
        break # Exit the loop immediately when correct
    elif guess > secret:
        print(f"Lower! {guess} is Too high!")
    else:
        print(f"Higher! {guess} is Too low!")
    
    # 4. Show remaining attempts using f-strings
    remaining = max_tries - attempts
    if remaining > 0 and not won:
        print(f"Keep going! You have {remaining} attempts left.")

# 5. Final check: if the loop finishes without a win
if not won:
    print("\n" + "="*50)
    print(f"GAME OVER. The AI secret was: {secret}")
    print("Better luck next time – keep optimizing your logic!")