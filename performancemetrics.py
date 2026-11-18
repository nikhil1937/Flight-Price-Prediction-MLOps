from sklearn.metrics import mean_absolute_percentage_error
# Predict flight prices
y_pred = best_model.predict(X_test_processed).flatten()

# Calculate evaluation metrics
mape = mean_absolute_percentage_error(y_test, y_pred) * 100
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Test MAPE:", round(mape, 2), "%")
print("Test RMSE:", round(rmse, 2))
print("Test R² Score:", round(r2, 4))

# Create a figure to visualize actual versus predicted flight prices
plt.figure(figsize=(7, 5))

# Plot actual prices against predicted prices
plt.scatter(y_test, y_pred, alpha=0.5)

# Label the x-axis and y-axis
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')

# Add a title to the plot
plt.title('Actual vs Predicted Flight Prices')

# Reference line representing perfect predictions
# Points on this line have predicted prices equal to actual prices
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--'
)

# Display the plot
plt.show()