
from pathlib import Path
import earthaccess
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = ROOT / "data" / "raw" / "satellite"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# Mansoura, Dakahlia
LATITUDE = 31.04
LONGITUDE = 31.38

# Pilot period: one year only
START_DATE = "2024-01-01"
END_DATE = "2024-12-31"

PRODUCT = "MOD13Q1"
VERSION = "061"

# Expected MODIS tile for the pilot location
EXPECTED_TILE = "h20v05"


def get_granule_filename(granule):
    """Get the HDF filename from a granule's download links."""

    links = granule.data_links(access="external")

    if not links:
        return None

    return Path(urlparse(links[0]).path).name



def download_modis():

    print("Connecting to NASA Earthdata...")

    # Login interactively
    earthaccess.login()


    print("\nSearching MODIS data for Mansoura...")
    print(f"Coordinates: {LATITUDE}, {LONGITUDE}")
    print(f"Period: {START_DATE} to {END_DATE}")


    
   # Search by one point instead of the entire Nile Delta
    results = earthaccess.search_data(
        short_name=PRODUCT,
        version=VERSION,
        point=(LONGITUDE, LATITUDE),
        temporal=(START_DATE, END_DATE),
        count=100
    )

    print(f"\nGranules found: {len(results)}")


    # # Nile Delta bounding box:
    # # west, south, east, north
    # bbox = (29.5, 30.0, 32.5, 31.8)

    # print("Searching MODIS MOD13Q1 data...")

    # results = earthaccess.search_data(
    #     short_name="MOD13Q1",
    #     version="061",
    #     bounding_box=bbox,
    #     temporal=("2024-01-01", "2025-12-31"),
    #     count=100
    # )

    # print(f"Found {len(results)} granules")

    if not results:
        print("No satellite data found.")
        return

     # Keep only the expected MODIS tile
    selected = []

    for granule in results:

        filename = get_granule_filename(granule)

        if filename and EXPECTED_TILE in filename:
            selected.append(granule)

    print(f"Granules matching {EXPECTED_TILE}: {len(selected)}")

    if not selected:
        print("No granules matched the expected tile.")
        print("Check the returned granule names before downloading.")
        for granule in results[:10]:
            print(granule.data_links(access="external"))
        return

    # Show download plan before starting
    estimated_size = sum(g.size for g in selected) / 1024

    print("\nDownload plan:")
    for granule in selected:
        print(get_granule_filename(granule))

    print(f"\nApproximate total size: {estimated_size:.2f} GB")

    # Remove only empty temporary files
    for file in OUTPUT_DIR.glob("partial_*"):
        if file.is_file() and file.stat().st_size == 0:
            file.unlink()

    print("\nStarting download...")
    print("Existing completed files will not be downloaded again.")

    downloaded = earthaccess.download(
        selected,
        local_path=str(OUTPUT_DIR),
        threads=2,
        show_progress=True,
        force=False
    )

    print("\nDownload process finished!")
    print(f"Files returned: {len(downloaded)}")


if __name__ == "__main__":
    download_modis()
