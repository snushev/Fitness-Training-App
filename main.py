from user import User
from exercise import Exercise, exercise_library
from workout import Workout
from progress import ProgressTracker


def create_user(users_dict):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = int(input("Enter your weight: "))
    height = int(input("Enter your height: "))
    goal = input("Enter your goal: ")
    user_id = len(users_dict) + 1  # Generate unique ID for each user
    users_dict[f"user_{user_id}"] = User(name, age, weight, height, goal)
    print(f"User {user_id} created successfully!\n")


def show_users(users_dict):
    if users_dict:
        print("Current users:")
        for user_id, user in users_dict.items():
            print(f"{user_id}: {user}")
    else:
        print("No users found.\n")


def main():
    users_dict = {}  # Dictionary to store users with unique keys
    while True:
        print("\nMenu:")
        print("1. Create a new user")
        print("2. Show all users")
        print("3. Display exercises")
        choice = input("Choose an option: ")

        if choice == "1":
            create_user(users_dict)
        elif choice == "2":
            show_users(users_dict)
        elif choice == "3":
            for exercise in exercise_library:
                print(exercise.display_exercise())
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()