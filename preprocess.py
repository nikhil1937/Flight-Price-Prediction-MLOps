import pandas as pd

flights_df_copy = pd.read_csv("flights_copy.csv")
hotels_df_copy = pd.read_csv("hotels_copy.csv")

for df in [flights_df_copy, hotels_df_copy]:
    df['date'] = pd.to_datetime(
        df['date'], format='mixed', errors='coerce'
    )

flights_df_copy.to_parquet("flights_processed.parquet", index=False)
hotels_df_copy.to_parquet("hotels_processed.parquet", index=False)

# Extract useful features from the date column
flights_df_copy['year'] = flights_df_copy['date'].dt.year
flights_df_copy['month'] = flights_df_copy['date'].dt.month
flights_df_copy['day'] = flights_df_copy['date'].dt.day
flights_df_copy['day_of_week'] = flights_df_copy['date'].dt.dayofweek

# Remove the original datetime column after feature extraction
flights_df_copy.drop(columns=['date'], inplace=True)

# Preserve unique identifiers
identifiers = flights_df_copy[['travelCode', 'userCode']].copy()

# Remove unique identifiers from model features
df_flights = flights_df_copy.drop(
    columns=['travelCode', 'userCode']
)

# Separate input features and target variable
X = df_flights.drop(columns=['price'])
y = df_flights['price']

print("Data preprocessing completed!")