# NBTC × ISS Thailand — Demo Login
A local Flask learning dashboard with a demo access-code login and public ISS position data.

## Privacy and scope
- This is not an official NBTC login or integration.
- It does not connect to NBTC internal systems or accounts.
- The personal identifier in the request is deliberately NOT embedded in this project. Do not use a Thai national ID, passport number, or personal password as a login code. Choose a separate random demo code.
- Never upload credentials or `.env` files to GitHub. `.env` is ignored.

## Run on Windows / VS Code PowerShell
```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
$env:APP_LOGIN_CODE = "your-own-random-demo-code"
$env:FLASK_SECRET_KEY = "your-own-long-random-secret"
python app.py
```
Open http://127.0.0.1:5000 and enter the demo code you set above.

If activation is blocked:
```powershell
.venv\\Scripts\\python.exe -m pip install -r requirements.txt
$env:APP_LOGIN_CODE = "your-own-random-demo-code"
$env:FLASK_SECRET_KEY = "your-own-long-random-secret"
.venv\\Scripts\\python.exe app.py
```

## GitHub upload
1. Create https://github.com/new with repository name `NBTC-ISS-Thailand-Demo`.
2. Extract the ZIP and upload its contents using Add file → Upload files.
3. Commit as `Add NBTC ISS educational demo login`.
4. Check that no secrets or personal identifiers were uploaded.

Git alternative:
```bash
git init
git add .
git commit -m "Add NBTC ISS educational demo login"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/NBTC-ISS-Thailand-Demo.git
git push -u origin main
```

ISS data source: https://api.wheretheiss.at/v1/satellites/25544
This is a development prototype, not production authentication. Do not expose Flask's development server publicly.
