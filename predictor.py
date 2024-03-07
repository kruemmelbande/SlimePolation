import joblib
import numpy as np

class IMUPredictor:
    def __init__(self, model_path):
        # Load the trained model
        self.model = joblib.load(model_path)
        self.scaler = joblib.load('scaler.pkl')  # Load the scaler used for standardization

    def predict(self, data):
        # Convert input data to numpy array
        features = np.array(list(data.values()))
        # Flatten the array
        features_flat = features.flatten().reshape(1, -1)
        # Standardize the features using the scaler
        features_scaled = self.scaler.transform(features_flat)
        # Predict legr and legl
        prediction = self.model.predict(features_scaled)
        # Reshape the prediction to match the original format
        prediction = prediction.reshape(-1, 3)
        # Extract legr and legl
        legr = prediction[0]
        legl = prediction[1]
        return legr, legl
