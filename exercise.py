class Exercise:
    def __init__(self, name, description, difficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def display_exercise(self):
        return f"{self.name} ({self.difficulty}): {self.description}"


exercise_library = [
    Exercise("Squats", "A lower-body exercise that primarily targets the thighs, hips, and buttocks.", "Intermediate"),
    Exercise("Push-Ups", "An upper-body exercise that targets the chest, shoulders, and triceps.", "Beginner"),
    Exercise("Lunges", "A lower-body exercise that targets the glutes, hamstrings, and quads.", "Intermediate"),
    Exercise("Burpees", "A full-body exercise that combines a squat, push-up, and jump.", "Advanced"),
    Exercise("Plank", "An isometric core exercise that targets the abdominal muscles.", "Beginner"),
    Exercise("Mountain Climbers", "A cardio exercise that also strengthens the arms, shoulders, and core.",
             "Intermediate"),
    Exercise("Pull-Ups", "An upper-body exercise that targets the back, shoulders, and biceps.", "Advanced"),
    Exercise("Bench Press", "A strength exercise that targets the chest, shoulders, and triceps.", "Intermediate"),
    Exercise("Deadlift", "A compound movement that targets the back, glutes, hamstrings, and core.", "Advanced"),
    Exercise("Leg Press", "A machine-based exercise focusing on the quadriceps, hamstrings, and glutes.",
             "Intermediate"),
    Exercise("Lat Pulldown", "A machine exercise targeting the latissimus dorsi and upper back muscles.", "Beginner"),
    Exercise("Cable Row", "A machine exercise focusing on the back and biceps.", "Intermediate"),
    Exercise("Shoulder Press", "A shoulder exercise that targets the deltoids and triceps.", "Intermediate"),
    Exercise("Bicep Curl", "An isolation exercise targeting the biceps.", "Beginner"),
    Exercise("Leg Extension", "A machine exercise that isolates the quadriceps.", "Beginner"),
    Exercise("Incline Dumbbell Press", "A chest exercise that emphasizes the upper chest and shoulders.",
             "Intermediate"),
    Exercise("Hack Squat", "A machine-based squat exercise targeting the quadriceps.", "Advanced"),
    Exercise("Seated Calf Raise", "Targets the calf muscles, focusing on the gastrocnemius and soleus.", "Beginner"),
    Exercise("Tricep Dips", "A bodyweight exercise that targets the triceps, chest, and shoulders.", "Intermediate"),
    Exercise("T-Bar Row", "A rowing movement that strengthens the middle back and lats.", "Advanced"),
    Exercise("Smith Machine Squat", "A machine-based squat that targets the quads and glutes with more stability.",
             "Intermediate"),
    Exercise("Preacher Curl", "An isolation exercise focusing on the biceps using the preacher bench.", "Beginner"),
    Exercise("Leg Curl", "A machine exercise that isolates the hamstrings.", "Beginner"),
    Exercise("Chest Fly", "A machine or dumbbell exercise targeting the chest, specifically the pectoral muscles.",
             "Intermediate"),
    Exercise("Overhead Tricep Extension", "Targets the triceps, specifically the long head.", "Intermediate"),
    Exercise("Hammer Curl", "An alternative bicep curl that also engages the forearms.", "Beginner"),
    Exercise("Hip Thrust", "An exercise targeting the glutes, often performed with a barbell.", "Advanced"),
    Exercise("Pec Deck Machine", "Isolates the pectoral muscles, providing a controlled chest workout.", "Beginner"),
    Exercise("Shrugs", "A shoulder exercise targeting the trapezius muscles.", "Beginner"),
    Exercise("Face Pull", "A cable exercise focusing on the rear deltoids and upper back.", "Intermediate")
]
