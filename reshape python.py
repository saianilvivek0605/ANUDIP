import numpy as np
# Create a 2D NumPy array representing exam scores for 10 students in 3 subjects
exam_scores = np.array([[85, 90, 78],
[92, 88, 95],
[77, 80, 82],
[65, 70, 68],
[88, 85, 90],
[72, 78, 75],
[95, 92, 96],
[68, 70, 75],
[88, 85, 89],
[78, 82, 80]])
# Print the original exam_scores array
print("Original exam_scores array:")
print(exam_scores)
first_student_scores = exam_scores[0]
print("\nScores of the first student:")
print(first_student_scores)
math_scores = exam_scores[:, 0]
print("\nMath scores for all students:")
print(math_scores)
array_shape = exam_scores.shape
print("\nShape of the exam_scores array:")
print(array_shape)
reshaped_scores = exam_scores.reshape(3, 10)
print("\nReshaped exam_scores array:")
print(reshaped_scores)
