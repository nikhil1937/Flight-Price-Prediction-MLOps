import pandas as pd

# Read datasets
flights_df = pd.read_csv("C:/Users/Ashish/OneDrive/Desktop/Docs/flights.csv")
users_df = pd.read_csv("C:/Users/Ashish/OneDrive/Desktop/Docs/users.csv")
hotels_df = pd.read_csv("C:/Users/Ashish/OneDrive/Desktop/Docs/hotels.csv")

# Create a copy of the dataset
flights_df_copy=flights_df.copy()
users_df_copy=users_df.copy()
hotels_df_copy=hotels_df.copy()
