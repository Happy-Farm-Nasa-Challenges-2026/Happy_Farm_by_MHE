
import rasterio

print("Rasterio version:", rasterio.__version__)

with rasterio.Env() as env:
    drivers = env.drivers()

    hdf_drivers = {
        name: description
        for name, description in drivers.items()
        if "HDF" in name.upper()
    }

    print("\nAvailable HDF drivers:")

    for name, description in hdf_drivers.items():
        print(name, ":", description)

    if not hdf_drivers:
        print("No HDF drivers found.")
