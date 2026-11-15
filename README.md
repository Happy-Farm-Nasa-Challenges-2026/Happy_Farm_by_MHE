# 🌱 Happy Farm
### AI-Powered Agricultural Decision Support System

Happy Farm is a Data Science and AI project developed for the **NASA Space Apps Challenge 2026**.

The project aims to support smarter agricultural decision-making in Egypt by analyzing climate conditions, satellite observations, and soil properties to help identify suitable crops and develop intelligent crop rotation recommendations.

---

## 🎯 Project Objectives

- Collect environmental and agricultural data from reliable sources.
- Analyze climate conditions and soil characteristics.
- Monitor vegetation and land surface conditions using satellite data.
- Identify relationships between environmental factors and crop suitability.
- Develop data-driven crop rotation recommendations.
- Support more sustainable and informed agricultural decisions.

## 🛰️ Data Sources

The project uses data from the following sources:

| Source | Data | Purpose |
|---|---|---|
| [NASA POWER](https://power.larc.nasa.gov/) | Climate and meteorological data | Analyze temperature, rainfall, humidity, and solar radiation |
| [NASA MODIS](https://modis.gsfc.nasa.gov/) | Satellite observations | Monitor vegetation and land surface conditions |
| [SoilGrids](https://soilgrids.org/) | Soil properties | Understand soil characteristics |
| Agricultural Reference Data | Crop information | Understand crop requirements and rotation constraints |

For detailed dataset descriptions, variables, units, and agricultural relevance, see [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md).

## 📁 Repository Structure

```text
Happy-Farm/
│
├── data/
│   ├── raw/
│   │   ├── climate/
│   │   ├── satellite/
│   │   ├── soil/
│   │   └── agriculture/
│   │
│   └── processed/
│
├── docs/
│   ├── DATA_DICTIONARY.md
│   └── DATA_SOURCES.md
│
├── notebooks/
│
├── src/
│   ├── data_collection/
│   ├── preprocessing/
│   ├── models/
│   └── utils/
│
├── app/
├── tests/
│
├── .gitignore
├── requirements.txt
└── README.md
```

### Folder Responsibilities

| Directory | Description |
|---|---|
| `data/raw/` | Original datasets downloaded from external sources |
| `data/processed/` | Cleaned and transformed datasets |
| `docs/` | Project documentation and dataset descriptions |
| `notebooks/` | Exploratory Data Analysis (EDA) and experiments |
| `src/data_collection/` | Scripts for retrieving data from external sources |
| `src/preprocessing/` | Data cleaning and feature engineering |
| `src/models/` | Machine Learning models and training pipelines |
| `src/utils/` | Shared utility functions |
| `app/` | Application and user interface |
| `tests/` | Project tests |

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Happy-Farm
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Credentials

Some NASA data services may require authentication.

Create a local `.env` file if required by the scripts.

Never commit your passwords, access tokens, or other credentials to GitHub.

Follow the authentication instructions in the relevant data collection script.

## ▶️ Running the Project

Run the data collection scripts from the repository root.

For example:

```bash
python -m src.data_collection.modis
```

For other data sources, execute their corresponding scripts:

```bash
python -m src.data_collection.nasa_power
```

```bash
python -m src.data_collection.soilgrids
```

Note: Only run scripts that have actually been implemented. The commands above assume those module names exist.

Downloaded datasets are stored locally under the corresponding directories in `data/raw/`.

**Important:** Raw datasets are excluded from Git tracking because of their large file sizes. Each team member should retrieve the required data using the collection scripts.

## 📊 Data Documentation

The `docs/` directory contains documentation about:

- Data sources and access methods.
- Dataset descriptions and variable meanings.
- Measurement units and spatial/temporal resolutions.
- How each dataset contributes to the project.

See [`DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md) for details.

## 🚧 Project Development Status

The project is being developed incrementally.

- [x] Initial data collection scripts.
- [ ] Complete data collection pipeline.
- [ ] Data exploration and visualization.
- [ ] Data preprocessing and integration.
- [ ] Feature engineering.
- [ ] Crop suitability analysis.
- [ ] Crop rotation recommendation model.
- [ ] Application development.
- [ ] Testing and evaluation.

Items should be updated as the team completes each stage.

## 👥 Team Collaboration

Contributions are welcome!

1. Clone the repository.
2. Create a separate branch for your task.
3. Implement your changes.
4. Commit your work with meaningful messages.
5. Push your branch and open a Pull Request.

Example:

```bash
git checkout -b feature/data-preprocessing

git add .

git commit -m "Add climate data preprocessing"

git push origin feature/data-preprocessing
```

## 📜 License

To be determined.