import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
data = pd.read_csv('traffic_data.csv')

# Normalize the features
features = data[['time', 'x', 'y', 'speed']]
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(features)
normalized_df = pd.DataFrame(normalized_data, columns=['time', 'x', 'y', 'speed'])

# Build the autoencoder
input_dim = normalized_df.shape[1]  # This should be 4, but we need to pass it as (4,)
autoencoder = models.Sequential([
    layers.InputLayer(input_shape=(input_dim,)),  # Specify shape as a tuple
    layers.Dense(8, activation='relu'),
    layers.Dense(4, activation='relu'),
    layers.Dense(8, activation='relu'),
    layers.Dense(input_dim, activation='linear')
])

autoencoder.compile(optimizer='adam', loss='mse')

# Train the autoencoder
history = autoencoder.fit(normalized_df, normalized_df, epochs=50, batch_size=16, shuffle=True, validation_split=0.1)

# Get reconstruction errors
reconstructions = autoencoder.predict(normalized_df)
errors = tf.reduce_mean(tf.math.squared_difference(normalized_df, reconstructions), axis=1)

# Set a threshold for anomalies (e.g., top 5% errors)
threshold = tf.math.top_k(errors, k=int(len(errors) * 0.05)).values[-1].numpy()

# Flag anomalies
data['anomaly'] = errors > threshold

# Save the DataFrame with anomalies back to a CSV file
data.to_csv('traffic_data_with_anomalies.csv', index=False)

# Optionally, print anomalies
print(data[data['anomaly'] == True])
