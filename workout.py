from exercise import Exercise


class Workout:
    def __init__(self, name):
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise, sets, reps, rest_time):
        self.exercises.append({'exercise': exercise, 'sets': sets, 'reps': reps, 'rest_time': rest_time})

    def remove_exercise(self, exercise_name):
        self.exercises = [ex for ex in self.exercises if ex['exercise'].name != exercise_name]

    def view_workout(self):
        print(f"Workout: {self.name}")
        for ex in self.exercises:
            print(f"{ex['exercise'].name}: {ex['sets']} sets, {ex['reps']} reps, {ex['rest_time']} seconds rest")


workout_library = [
    Workout("Chest and biceps"),
    Workout("Back and triceps"),
    Workout("Legs and shoulders"),
]

chest_and_biceps = workout_library[0]
chest_and_biceps.add_exercise(Exercise("Bench press"), 5, 10, 60)
chest_and_biceps.add_exercise(Exercise("Incline dumbbell press"), 3, 12, 90)
chest_and_biceps.add_exercise(Exercise("Chest Fly"),5, 12, 60)
chest_and_biceps.add_exercise(Exercise("Dumbbell curls"), 3, 12, 90)
chest_and_biceps.add_exercise(Exercise("Cable Row"), 3, 12, 90)

back_and_triceps = workout_library[1]
back_and_triceps.add_exercise(Exercise("Pull-ups"), 5, 10, 60)
back_and_triceps.add_exercise(Exercise("Dumbbell rows"), 3, 12, 90)
back_and_triceps.add_exercise(Exercise("Dumbbell lunges"), 3, 12, 90)
back_and_triceps.add_exercise(Exercise("Overhead Tricep Extension"), 3, 12, 90)
back_and_triceps.add_exercise(Exercise("Tricep dips"), 3, 12, 90)


legs_and_shoulders = workout_library[2]
legs_and_shoulders.add_exercise(Exercise("Squats"), 5, 10, 60)
legs_and_shoulders.add_exercise(Exercise("Lunges"), 3, 12, 90)
legs_and_shoulders.add_exercise(Exercise("Deadlifts"), 3, 12, 90)
legs_and_shoulders.add_exercise(Exercise("Glute bridges"), 3, 12, 90)
legs_and_shoulders.add_exercise(Exercise("Bicycle crunches"), 3, 12, 90)
legs_and_shoulders.add_exercise(Exercise("Shoulder press"), 3, 12, 90)
legs_and_shoulders.add_exercise(Exercise("Shrugs"), 3, 12, 90)