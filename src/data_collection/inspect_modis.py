
from pathlib import Path
import rasterio

ROOT = Path(__file__).resolve().parents[2]
SATELLITE_DIR = ROOT / "data" / "raw" / "satellite"

files = sorted(SATELLITE_DIR.glob("MOD13Q1.*.h20v05.*.hdf"))

if not files:
    raise FileNotFoundError("No MODIS HDF files found.")

sample = files[0]

print("Testing file:", sample.name)

try:
    with rasterio.open(sample) as dataset:

        print("\nDriver:", dataset.driver)
        print("Main dimensions:", dataset.width, dataset.height)

        print("\nAvailable subdatasets:")

        for subdataset in dataset.subdatasets:
            print(subdataset)

except Exception as error:
    print("\nCould not read HDF file.")
    print("Error:", error)
