<#
PowerShell script to create a Windows venv and install requirements with helpful fallbacks.
Run from project root as: `.esetup_venv.ps1` after adjusting execution policy if needed.

This script attempts to detect if your system Python is an MSYS/MinGW build (which often causes
missing prebuilt wheels and SSL/CA issues) and will prefer the Windows launcher `py -3` if available.
#>

function Get-PythonInfo {
    param($py)
    & $py -c "import sys, sysconfig, platform, ssl; import importlib; print('platform:'+sys.platform); print('exe:'+sys.executable); print('version:'+sys.version.replace('\n',' ')); print('get_platform:'+sysconfig.get_platform()); print('certifi:'+ (importlib.import_module('certifi').where() if importlib.util.find_spec('certifi') else 'missing'))" 2>&1
}

# Prefer the Windows py launcher when available
$preferred = 'py -3'
try {
    & $preferred -V | Out-Null
} catch {
    $preferred = 'python'
}

Write-Host "Using Python command: $preferred" -ForegroundColor Green

# Show diagnostics about the current system Python
Write-Host "--- System Python diagnostics ---" -ForegroundColor Cyan
Get-PythonInfo $preferred | ForEach-Object { Write-Host $_ }
Write-Host "---------------------------------" -ForegroundColor Cyan

# If the Python path suggests MSYS / ucrt64 / mingw, warn and try to use py -3 explicitly
$sysInfo = (& $preferred -c "import sys; print(sys.executable)").Trim()
if ($sysInfo -match 'msys|ucrt64|mingw') {
    Write-Warning "Detected MSYS/MinGW-like Python. This can cause missing wheels and build failures."
    if ($preferred -ne 'py -3') {
        try {
            Write-Host "Attempting to use 'py -3' to create the venv (official Windows Python)" -ForegroundColor Yellow
            & py -3 -V | Out-Null
            $preferred = 'py -3'
        } catch {
            Write-Warning "'py -3' not found. Please install official Python from https://www.python.org and re-run this script for best results."
        }
    }
}

# Recreate venv with preferred python
if (Test-Path .\venv) { Remove-Item -Recurse -Force .\venv }
Write-Host "Creating virtual environment 'venv' using: $preferred" -ForegroundColor Cyan
& $preferred -m venv venv

if (-not(Test-Path .\venv\Scripts\Activate.ps1)) {
    Write-Warning "Couldn't find the Windows activation script in the created venv. Installation may fail. Ensure you're using the official Windows Python." 
} else {
    Write-Host "Activating venv..." -ForegroundColor Cyan
    .\venv\Scripts\Activate.ps1
}

Write-Host "Upgrading packaging tools (pip, setuptools, wheel)..." -ForegroundColor Cyan
.\venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel

# Install certifi early to help with SSL cert issues
Write-Host "Installing certifi to provide a CA bundle for SSL verification..." -ForegroundColor Cyan
.\venv\Scripts\python.exe -m pip install certifi

# Set SSL_CERT_FILE for this PowerShell session to help avoid CERTIFICATE_VERIFY_FAILED
$certPath = & .\venv\Scripts\python.exe -c "import certifi; print(certifi.where())"
if ($certPath) { $env:SSL_CERT_FILE = $certPath; Write-Host "Set SSL_CERT_FILE to $certPath" -ForegroundColor Green }

Write-Host "Installing dependencies from requirements.txt..." -ForegroundColor Cyan
$installCmd = ".\venv\Scripts\python.exe -m pip install -r requirements.txt"
try {
    iex $installCmd
} catch {
    Write-Warning "Install failed. Retrying using --trusted-host (temporary workaround for SSL issues)..."
    iex ".\venv\Scripts\python.exe -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt"
}

Write-Host "If you encounter build failures for packages like 'pydantic-core' or 'numpy', see README.md for options: install Windows Python, or install Rust/CMake/Ninja and Visual C++ build tools." -ForegroundColor Yellow
Write-Host "Done." -ForegroundColor Green
Run from project root as: `.	ools\setup_windows_venv.ps1` or `.





































Write-Host "Done. If there were build failures requiring Rust/CMake, see README.md for instructions." -ForegroundColor Green}    iex ".\venv\Scripts\python.exe -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt"    Write-Warning "Install failed. Retrying using --trusted-host (temporary workaround for SSL issues)..."} catch {    iex $installCmdtry {$installCmd = ".\venv\Scripts\python.exe -m pip install -r requirements.txt"Write-Host "Installing dependencies from requirements.txt..." -ForegroundColor Cyan\venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel.Write-Host "Upgrading packaging tools..." -ForegroundColor Cyan}    .\venv\Scripts\Activate.ps1    Write-Host "Activating venv..." -ForegroundColor Cyan} else {    Write-Warning "Couldn't find the Windows activation script. Make sure you're running official Windows Python."if (-not(Test-Path .\venv\Scripts\Activate.ps1)) {& $pythonCmd -m venv venvWrite-Host "Creating virtual environment 'venv'..." -ForegroundColor Cyan# Create venvWrite-Host "Using Python command: $pythonCmd" -ForegroundColor Green}    $pythonCmd = "python"} catch {    & $pythonCmd -V | Out-Nulltry {$pythonCmd = "py -3"  # prefer Windows launcher#>esetup_venv.ps1` after adjusting execution policy if needed.