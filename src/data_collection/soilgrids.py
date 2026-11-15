
import requests
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = ROOT / "data" / "raw" / "soil"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# SoilGrids WCS services
SOIL_PROPERTIES = [
    "phh2o",           # soil pH in water
    "soc",             # soil organic carbon
    "clay",            # clay content
    "sand",            # sand content
    "silt"             # silt content
]

# Approximate regional bounding boxes in longitude/latitude
# Keep the areas small for efficient requests.
LOCATIONS = {
    "Mansoura": (31.30, 30.98, 31.46, 31.10),
    "Ismailia": (32.18, 30.52, 32.36, 30.68),
    "Minya": (30.66, 28.03, 30.84, 28.20)
}


def download_soil_property(
    property_name,
    location,
    bbox
):

    west, south, east, north = bbox

    url = (
        f"https://maps.isric.org/mapserv"
        f"?map=/map/{property_name}.map"
    )

    # Use the median prediction at 0-5 cm depth
    coverage_id = f"{property_name}_0-5cm_Q0.5"

    params = {
        "SERVICE": "WCS",
        "VERSION": "2.0.1",
        "REQUEST": "GetCoverage",
        "COVERAGEID": coverage_id,
        "FORMAT": "GEOTIFF_INT16",

        # Geographic bounding box
        "SUBSET": [
            f"Long({west},{east})",
            f"Lat({south},{north})"
        ],

        "SUBSETTINGCRS":
            "http://www.opengis.net/def/crs/EPSG/0/4326",

        "OUTPUTCRS":
            "http://www.opengis.net/def/crs/EPSG/0/4326"
    }

    print(
        f"Downloading {property_name} for {location}"
    )

    response = requests.get(
        url,
        params=params,
        timeout=180
    )

    response.raise_for_status()

    # Check that the server returned a raster
    content_type = response.headers.get(
        "Content-Type", ""
    )

    if "tiff" not in content_type.lower() and not (
        response.content[:4] in (b"II*\x00", b"MM\x00*")
    ):
        raise RuntimeError(
            f"Expected GeoTIFF but received: {content_type}. "
            "Check WCS coverage ID and service response."
        )

    output_file = (
        OUTPUT_DIR
        / f"{location.lower()}_{property_name}.tif"
    )

    output_file.write_bytes(response.content)

    print(f"Saved: {output_file}")


def main():

    for location, bbox in LOCATIONS.items():

        for property_name in SOIL_PROPERTIES:

            try:
                download_soil_property(
                    property_name,
                    location,
                    bbox
                )

            except Exception as error:
                print(
                    f"Failed: {location} "
                    f"{property_name}: {error}"
                )


if __name__ == "__main__":
    main()
