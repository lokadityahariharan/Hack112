import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Step 1: Load the CSV
data = pd.read_csv('asl_data.csv', header=None)
#data = data.dropna()  # remove rows with any missing values
#data.to_csv('asl_data_clean.csv', index=False, header=False)

# Step 2: Split features (X) and labels (y)
X = data.iloc[:, :-1]  # first 63 columns = landmark features
y = data.iloc[:, -1]   # last column = label (A–Y)

# Step 3: Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Step 4: Train a model (K-Nearest Neighbors)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Step 5: Evaluate accuracy
accuracy = model.score(X_test, y_test)
print(f"✅ Model trained with {accuracy*100:.2f}% accuracy!")

# Step 6: Save model to a file
joblib.dump(model, 'asl_knn_model.pkl')
print("🧠 Model saved as 'asl_knn_model.pkl'")