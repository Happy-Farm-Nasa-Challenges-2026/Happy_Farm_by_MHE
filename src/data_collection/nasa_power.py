
import requests
import pandas as pd
from pathlib import Path

# Project root
ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = ROOT / "data" / "raw" / "climate"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# NASA POWER Daily API
API_URL = (
    "https://power.larc.nasa.gov/"
    "api/temporal/daily/point"
)

PARAMETERS = [  
    "T2M",      # daily mean temperature (°C)
    "T2M_MAX",  # daily maximum temperature (°C)
    "T2M_MIN",  # daily minimum temperature (°C)
    "PRECTOTCORR", # daily precipitation (mm/day)
    "RH2M",  # daily mean relative humidity (%)
    "ALLSKY_SFC_SW_DWN"  # daily total sky radiance (W/m²)
]

# Representative locations in Egypt
LOCATIONS = {
    "Mansoura": {
        "latitude": 31.04,
        "longitude": 31.38
    },
    "Ismailia": {
        "latitude": 30.60,
        "longitude": 32.27
    },
    "Minya": {
        "latitude": 28.11,
        "longitude": 30.75
    }
}

def collect_climate(location, coordinates):

    params = {
        "parameters": ",".join(PARAMETERS),
        "community": "AG",
        "longitude": coordinates["longitude"],
        "latitude": coordinates["latitude"],
        "start": "20210101",
        "end": "20251231",
        "format": "JSON",
        "time-standard": "UTC"
    }

    print(f"Downloading climate data: {location}")

    response = requests.get(
        API_URL,
        params=params,
        timeout=120
    )

    response.raise_for_status()

    result = response.json()

    # Extract daily measurements
    measurements = result["properties"]["parameter"]

    df = pd.DataFrame(measurements)

    df.index.name = "date"
    df = df.reset_index()

    # Convert date
    df["date"] = pd.to_datetime(
        df["date"],
        format="%Y%m%d"
    )

    # Replace missing-value indicators
    df.replace(-999, pd.NA, inplace=True)

    df["location"] = location
    df["latitude"] = coordinates["latitude"]
    df["longitude"] = coordinates["longitude"]

    # Save individual location data
    output_file = OUTPUT_DIR / f"{location.lower()}_climate.csv"

    df.to_csv(output_file, index=False)

    print(f"Saved: {output_file}")

    return df


def main():

    all_data = []

    for location, coordinates in LOCATIONS.items():

        try:
            df = collect_climate(location, coordinates)
            all_data.append(df)

        except Exception as error:
            print(f"Error for {location}: {error}")

    if all_data:

        combined = pd.concat(
            all_data,
            ignore_index=True
        )

        combined.to_csv(
            OUTPUT_DIR / "all_locations_climate.csv",
            index=False
        )

        print("\nClimate collection completed!")
        print(combined.head())


if __name__ == "__main__":
    main()
