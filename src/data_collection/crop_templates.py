
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = ROOT / "data" / "raw" / "agriculture"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# Candidate Egyptian crops.
# These are candidate records, not validated crop recommendations.
crops = [
    ("Wheat", "Poaceae", "Winter"),
    ("Barley", "Poaceae", "Winter"),
    ("Faba bean", "Fabaceae", "Winter"),
    ("Lentils", "Fabaceae", "Winter"),
    ("Berseem clover", "Fabaceae", "Winter"),
    ("Maize", "Poaceae", "Summer"),
    ("Rice", "Poaceae", "Summer"),
    ("Cotton", "Malvaceae", "Summer"),
    ("Soybean", "Fabaceae", "Summer"),
    ("Sunflower", "Asteraceae", "Summer"),
    ("Peanut", "Fabaceae", "Summer"),
    ("Sugar beet", "Amaranthaceae", "Winter")
]

crop_columns = [
    "crop",
    "family",
    "season",
    "duration_days",
    "min_temperature_c",
    "max_temperature_c",
    "water_requirement",
    "soil_ph_min",
    "soil_ph_max",
    "nitrogen_requirement",
    "planting_month",
    "harvesting_month",
    "source",
    "verified"
]

crop_df = pd.DataFrame(
    crops,
    columns=["crop", "family", "season"]
)

# Add fields that need research and validation.
for column in crop_columns[3:]:
    crop_df[column] = None

crop_df = crop_df[crop_columns]

crop_df.to_csv(
    OUTPUT_DIR / "crop_requirements.csv",
    index=False
)


# Crop rotation rules.
rotation_columns = [
    "previous_crop",
    "next_crop",
    "allowed",
    "reason",
    "source",
    "verified"
]

rotation_df = pd.DataFrame(
    columns=rotation_columns
)

rotation_df.to_csv(
    OUTPUT_DIR / "crop_rotation_rules.csv",
    index=False
)


# Historical farm records.
history_columns = [
    "farm_id",
    "latitude",
    "longitude",
    "year",
    "season",
    "crop",
    "irrigation_type",
    "water_availability"
]

history_df = pd.DataFrame(
    columns=history_columns
)

history_df.to_csv(
    OUTPUT_DIR / "farm_history.csv",
    index=False
)


print("Agricultural templates created!")

print("1. crop_requirements.csv")
print("2. crop_rotation_rules.csv")
print("3. farm_history.csv")
