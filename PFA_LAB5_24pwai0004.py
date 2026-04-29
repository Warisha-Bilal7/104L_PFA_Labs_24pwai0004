def check_password():
    attempts=5
    while attempts > 0:
        user_input=input("Enter your password: ")
        conditions_met=0
        if len(user_input) >= 8:
            conditions_met +=1
        if any(char.isdigit() for char in user_input):
            conditions_met +=1
        if any(char.isupper() for char in user_input):
            conditions_met +=1
        if conditions_met == 3:
            print(f"Feedback: Strong\n Password Created is strong.")
            break
            # print(f"Password Created is Strong")
        elif conditions_met ==2:
            print(f"The password is of Moderate Strength.")
        elif conditions_met ==1:
            print(f"Password is a very weak one.")
        else:
            print(f"Password not accepted as it is very weak.")
        attempts -=1
        #Sow remaining attempts
        if attempts > 0:
            print(f" Remaining number of attempts: {attempts}")
        else:
            print("Final Verdict: Password is extremely weak")
check_password()