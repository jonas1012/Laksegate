import requests
import pandas as pd
from datetime import datetime, timedelta

# Settings
base_url = "https://dmigw.govcloud.dk/v2/metObs/collections/observation/items"
api_key = "API_KEY"
station_id = "06180"
parameter_id = "visibility"

# Define date range
start_date = datetime.strptime("2023-01-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
end_date = datetime.strptime("2023-12-31T23:59:59Z", "%Y-%m-%dT%H:%M:%SZ")
step_days = 5

# Initialize empty DataFrame
all_observations = pd.DataFrame()

# Loop over 5-day intervals
current_start = start_date

while current_start < end_date:
    current_end = min(current_start + timedelta(days=step_days) - timedelta(seconds=1), end_date)

    datetime_range = f"{current_start.strftime('%Y-%m-%dT%H:%M:%SZ')}/{current_end.strftime('%Y-%m-%dT%H:%M:%SZ')}"
    full_url = (
        f"{base_url}?api-key={api_key}"
        f"&stationId={station_id}"
        f"&datetime={datetime_range}"
        f"&parameterId={parameter_id}"
    )

    response = requests.get(full_url)

    if response.status_code == 200:
        json_data = response.json()
        features = json_data.get("features", [])

        if features:
            temp_obs = pd.json_normalize([f["properties"] for f in features])
            all_observations = pd.concat([all_observations, temp_obs], ignore_index=True)
            print(f"✓ Retrieved data from {current_start} to {current_end}")
        else:
            print(f"No data from {current_start} to {current_end}")
    else:
        print(f"Failed for interval: {current_start} to {current_end}")

    # Move to next interval
    current_start = current_end + timedelta(seconds=1)

# Convert datetime and sort
all_observations['observed'] = pd.to_datetime(all_observations['observed'], format="%Y-%m-%dT%H:%M:%SZ", utc=True)
all_observations = all_observations.sort_values(by='observed')

# Preview
print(all_observations.head())

# Export to Excel (Remove hashtag in order to save the observations in excel file)
#all_observations.to_excel("visibility_observations (2023).xlsx", index=False)
