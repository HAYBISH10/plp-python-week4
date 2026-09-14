score = int(input("Enter your score (0-100): "))

# Validate that the score is within the allowed range.
if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
else:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"A score of {score} earns grade: {grade}")
