# Define numerical and categorical columns
numerical_cols = [
    'distance', 'time', 'year', 'month', 'day', 'day_of_week'
]

categorical_cols = ['from', 'to', 'flightType', 'agency']

# Create a preprocessing pipeline for numerical and categorical features
preprocessor = ColumnTransformer(
    transformers=[
        # Standardize numerical features to a common scale
        ('num', StandardScaler(), numerical_cols),

        # Convert categorical features into numerical columns using One-Hot Encoding
        # Ignore categories not seen during training when transforming new data
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ]
)

# Fit the preprocessor on the training data and transform it
X_train_processed = preprocessor.fit_transform(X_train)

# Transform the test data using the same fitted preprocessor
X_test_processed = preprocessor.transform(X_test)

# Tune hidden layers, neurons, and learning rate to predict flight prices.

def build_model(hp):
    model = Sequential()

    # Tune number of hidden layers
    num_layers = hp.Choice('num_layers', [1, 2, 3])

    # First hidden layer
    model.add(Dense(
        hp.Choice('neurons_1', [32, 64, 128]),
        activation='relu',
        input_shape=(X_train_processed.shape[1],)
    ))
    model.add(Dropout(0.2))

    # Add second hidden layer if selected
    if num_layers >= 2:
        model.add(Dense(
            hp.Choice('neurons_2', [16, 32, 64]),
            activation='relu'
        ))
        model.add(Dropout(0.2))

    # Add third hidden layer if selected
    if num_layers >= 3:
        model.add(Dense(
            hp.Choice('neurons_3', [16, 32, 64]),
            activation='relu'
        ))
        model.add(Dropout(0.2))

    # Output layer
    model.add(Dense(1))

    # Compile model
    model.compile(
        optimizer=Adam(learning_rate=hp.Choice(
            'learning_rate', [0.001, 0.0005, 0.0001]
        )),
        loss='mse',
        metrics=['mae']
    )

    return model

# Stop training when validation performance stops improving
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

# Configure hyperparameter tuning
tuner = kt.RandomSearch(
    build_model,
    objective='val_mae',
    max_trials=15,
    executions_per_trial=1,
    directory='flight_tuning',
    project_name='price_prediction',
    overwrite=True
)

# Perform hyperparameter tuning to find the best neural network configuration
tuner.search(
    X_train_processed,
    y_train,

    validation_split=0.2,
    epochs=1,
    batch_size=32,

    callbacks=[early_stopping],
    verbose=1
)

# Retrieve the best hyperparameter configuration from the tuning results
best_hp = tuner.get_best_hyperparameters(num_trials=1)[0]

# Display the optimal number of neurons in the first hidden layer
print("Best first hidden-layer neurons:",
      best_hp.get('neurons_1'))

# Display the optimal number of hidden layers
print("Best number of hidden layers:",
      best_hp.get('num_layers'))

# Display the optimal learning rate
print("Best learning rate:",
      best_hp.get('learning_rate'))

# Display the optimal number of neurons in each additional hidden layer
for i in range(2, best_hp.get('num_layers') + 1):
    print(f"Layer {i} neurons:",
          best_hp.get(f'neurons_{i}'))

# Build the model using the best hyperparameters
best_model = build_model(best_hp)

# Train the model with early stopping
history = best_model.fit(
    X_train_processed,
    y_train,
    validation_split=0.2,
    epochs=1,
    batch_size=32,
    callbacks=[early_stopping],
    verbose=1
)