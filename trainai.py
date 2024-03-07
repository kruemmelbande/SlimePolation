import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
import joblib

# Load data from JSON file
with open('captured_data.json', 'r') as f:
    data = json.load(f)

# Extract features and labels from the data
features = []
labels = []
for entry in data:
    feetl = entry['feetl']
    feetr = entry['feetr']
    hip = entry['hip']
    chest = entry['chest']
    legr = entry['legr']
    legl = entry['legl']
    features.append(feetl + feetr + hip + chest)
    labels.append(legr + legl)

# Convert lists to numpy arrays
X = np.array(features)
y = np.array(labels)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a neural network model
model = MLPRegressor(hidden_layer_sizes=(100, 100), activation='relu', solver='adam', max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate the model
train_score = model.score(X_train_scaled, y_train)
test_score = model.score(X_test_scaled, y_test)
print(f"Training Score: {train_score:.4f}")
print(f"Testing Score: {test_score:.4f}")

# Save the trained model
joblib.dump(model, 'imu_model.pkl')
joblib.dump(scaler, 'scaler.pkl')