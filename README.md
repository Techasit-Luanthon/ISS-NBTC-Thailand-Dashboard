# ISS + NBTC Public Information Dashboard

A Python + Streamlit educational dashboard that:
- Displays the publicly available ISS latitude, longitude, altitude, and orbital speed.
- Shows a sample NBTC dataset from CSV.
- Accepts and validates a CSV dataset intended for public use.

**Important:** This is not an official NASA or NBTC application. The included NBTC CSV contains illustrative sample data, not official statistics. It does not connect to NBTC internal systems.

## Requirements
- Windows 10/11 (64-bit recommended)
- Python 3.10 or newer
- Visual Studio Community 2026 with the Python development workload
- Internet access for the ISS API

## Open in Visual Studio Community 2026
1. Extract the ZIP file.
2. Open Visual Studio Community 2026.
3. Select **Open a local folder** and choose the extracted `ISS-NBTC-Dashboard` folder.
4. Install the **Python development** workload through Visual Studio Installer if Python tools are unavailable.
5. Open a terminal in the project folder (View > Terminal, if available).

## Create environment and install packages

In PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks environment activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

## Run

```powershell
streamlit run app.py
```

Open the local address shown in the terminal, usually `http://localhost:8501`.

## Project structure

```text
ISS-NBTC-Dashboard/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── modules/
│   ├── __init__.py
│   ├── iss_monitor.py
│   └── nbtc_data.py
├── data/
│   └── nbtc_sample.csv
└── assets/
```

## Use an NBTC public dataset
Replace `data/nbtc_sample.csv` with a dataset from an official public NBTC publication. Keep these columns:

`date,topic,value,unit,source_url`

Check the dataset's publication date, licence, definitions, and methodology. Do not describe sample, estimated, or unverified data as official.

## Upload to GitHub

Create an empty repository on GitHub. In the project folder, run:

```powershell
git init
git add .
git commit -m "Initial ISS NBTC public dashboard"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your own repository URL.

## Data sources
- ISS position API: https://api.wheretheiss.at/v1/satellites/25544
- NBTC official website: https://www.nbtc.go.th/
