import numpy as np

#Task 1: Create a dataset of 10 students(Maths, Science, English, Computer marks and a result)
data=np.array([[78,76,89,67,1],
                [56,67,68,60,1],
                [60,60,60,60,1],
                [54,64,65,67,1],
                [45,67,56,67,0],
                [88,90,99,87,1],
                [45,56,23,34,0],
                [78,65,54,34,0],
                [23,34,45,56,0],
                [78,89,67,56,1],
                [56,78,67,54,1]])

#Task 2: Separate features(X) and Labels(Y)
x=data[:,0:4]
y=data[:,4]

#Task 3: Calculate Statistics(Average, High and low marks)
Average_marks=np.mean(x,axis=0)
Highest_marks=np.max(x,axis=0)
Lowest_marks=np.min(x,axis=0)

#Task 4: Find Number of students who passed and failed
passed=np.sum(y==1)
failed=np.sum(y==0)

#Task 5: Identify students scoring above 80 and below 50.
above_80=np.sum(x>=80)
below_50=np.sum(x<=50)

#Task 6: Normalize the features using Min-Max Normalization
normalized_features=(x-Lowest_marks)/(Highest_marks-Lowest_marks)

#Task 7: Simple Prediction(Predict 1 if average score >50, else 0)
Prediction=(np.mean(x,axis=1)>50).astype(int)

#Task 8: Accuracy calculation
accuracy=np.mean(y==Prediction)*100

# --- Print Results ---
print("Dataset Shape:", data.shape)
print("-" * 30)
print(f"Average Marks (M, S, E, C): {Average_marks}")
print(f"Global Max: {Highest_marks} | Global Min: {Lowest_marks}")
print(f"Students Passed: {passed} | Students Failed: {failed}")
print(f"Number of students with any score > 80: {above_80}")
print(f"Number of students with all scores < 50: {below_50}")
print("-" * 30)
print("Normalized Features (First 2 rows):\n", normalized_features[:2])
print("-" * 30)
print(f"Prediction Accuracy: {accuracy}%")