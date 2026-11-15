# Data Sources – Happy Farm 🌱

This document describes the external data sources used in the Happy Farm project, including their providers, access methods, geographic coverage, temporal coverage, and intended use.

The project combines climate, satellite, soil, and agricultural datasets to support data-driven crop suitability analysis and crop rotation recommendations in Egypt.

---

## 1. NASA POWER – Climate Data

**Provider:** NASA Langley Research Center

**Website:** https://power.larc.nasa.gov/

**API Documentation:** https://power.larc.nasa.gov/docs/

**Dataset Type:** Climate and meteorological data

**Purpose:**

NASA POWER provides meteorological and solar radiation data that can help us understand environmental conditions affecting agricultural production.

**Data Collected:**
- Air temperature
- Precipitation
- Relative humidity
- Wind speed
- Solar radiation

**Geographic Coverage:** Egypt (project-specific locations)

**Temporal Coverage:** To be specified according to the API request.

**Access Method:** NASA POWER API

**Collection Script:** `src/data_collection/nasa_power.py`

**Storage Location:** `data/raw/climate/`

**Agricultural Applications:**
- Climate suitability analysis.
- Rainfall and temperature monitoring.
- Understanding seasonal climate patterns.
- Supporting crop selection and planning.

---

## 2. NASA MODIS – Satellite Data

**Provider:** NASA

**Website:** https://modis.gsfc.nasa.gov/

**Data Access:** https://search.earthdata.nasa.gov/

**Dataset Type:** Satellite remote sensing observations

**Purpose:**

MODIS provides satellite observations that can help monitor vegetation and land surface conditions over time.

**Geographic Coverage:** Mansoura, Egypt

**Temporal Coverage:** January 2024 – December 2024

**Access Method:** NASA Earthdata / Earthaccess

**Collection Script:** `src/data_collection/modis.py`

**Storage Location:** `data/raw/satellite/`

**Downloaded Data:**
- 24 HDF granule files.
- Approximately 3.07 GB total size.
- Selected tiles: H20V05 (verify against actual granule metadata).

**MODIS Product ID:** To be specified after confirming the exact product used.

**Agricultural Applications:**
- Vegetation monitoring.
- Tracking land surface changes.
- Supporting agricultural condition analysis.

**Note:** The specific variables and bands depend on the MODIS product selected. Refer to the product documentation before interpreting the downloaded files.

---

## 3. SoilGrids – Soil Properties

**Provider:** ISRIC – World Soil Information

**Website:** https://soilgrids.org/

**Documentation:** https://www.isric.org/explore/soilgrids

**Dataset Type:** Global soil information

**Purpose:**

SoilGrids provides spatial information about soil properties at different depths.

**Potential Variables:**
- Soil pH.
- Soil organic carbon.
- Soil texture (sand, silt, clay).
- Soil bulk density.
- Cation exchange capacity.

**Geographic Coverage:** Egypt (project-specific locations)

**Temporal Coverage:** Static or modeled soil information, depending on the selected dataset.

**Access Method:** To be specified according to the selected access service.

**Collection Script:** `src/data_collection/soilgrids.py`

**Storage Location:** `data/raw/soil/`

**Agricultural Applications:**
- Understanding soil characteristics.
- Evaluating crop suitability.
- Identifying soil-related agricultural constraints.

---

## 4. Agricultural Reference Data

**Provider:** To be determined.

**Dataset Type:** Agricultural and crop-related information.

**Potential Information:**
- Crop growing seasons.
- Water requirements.
- Temperature requirements.
- Soil preferences.
- Crop rotation compatibility.
- Nutrient requirements.

**Geographic Coverage:** Egypt.

**Access Method:** To be determined.

**Storage Location:** `data/raw/agriculture/`

**Agricultural Applications:**
- Defining crop requirements.
- Evaluating crop suitability.
- Developing crop rotation recommendations.

---

## 5. Data Collection and Reproducibility

All data collection scripts are maintained in:

`src/data_collection/`

To reproduce the data collection process:

1. Clone the repository.
2. Install the required Python dependencies.
3. Configure any required authentication credentials.
4. Run the corresponding collection script.
5. Verify that the downloaded files are stored in the expected directory.

### Important Notes

- Raw datasets are not stored in GitHub because some files are very large.
- Each team member should retrieve the required datasets using the provided scripts.
- Authentication credentials must never be committed to the repository.
- Original downloaded data should remain unchanged.
- Processed datasets should be stored separately under `data/processed/`.

---

## 6. References

- NASA POWER: https://power.larc.nasa.gov/
- NASA Earthdata: https://www.earthdata.nasa.gov/
- MODIS: https://modis.gsfc.nasa.gov/
- ISRIC SoilGrids: https://soilgrids.org/