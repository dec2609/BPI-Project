# BPI Project

Project repository for Business Process Intelligence / Data Analytics workflows.

## Directory Structure
- `data/`: Dataset storage (`raw/`, `interim/`, `processed/`)
- `src/`: Core Python modules and pipeline scripts
- `notebooks/`: Jupyter notebooks for exploratory data analysis
- `tests/`: Automated unit tests
- `docs/`: Project documentation and guidelines

## Quickstart
1. Set up a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   # source .venv/bin/activate # Linux/macOS
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place incoming datasets in `data/raw/` and run processing pipelines from `src/`.
