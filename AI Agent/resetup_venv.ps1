<#
PowerShell script to create a Windows venv and install requirements with helpful fallbacks.
Run from project root as: `.esetup_venv.ps1` after adjusting execution policy if needed.
#>

$preferred = 'py -3'
try { & $preferred -V | Out-Null } catch { $preferred = 'python' }
Write-Host "Using Python command: $preferred"

Write-Host "Python info:"; & $preferred -c "import sys; print(sys.executable, sys.version.replace('\n',' '), sys.platform)"

if (Test-Path .\venv) { Remove-Item -Recurse -Force .\venv }
& $preferred -m venv venv
Write-Host "Created venv using: $preferred"

# Use the venv python directly for installs
$vp = ".\venv\Scripts\python.exe"
& $vp -m pip install --upgrade pip setuptools wheel

# Install certifi and set SSL_CERT_FILE to help with certificate verification
& $vp -m pip install certifi
$certPath = & $vp -c "import certifi; print(certifi.where())"
if ($certPath) { $env:SSL_CERT_FILE = $certPath.Trim(); Write-Host "Set SSL_CERT_FILE to $env:SSL_CERT_FILE" }

# Install requirements with a fallback to --trusted-host if SSL or network errors occur
try {
    & $vp -m pip install -r requirements.txt
} catch {
    Write-Warning "Install failed; retrying with --trusted-host pypi.org --trusted-host files.pythonhosted.org"
    & $vp -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
}

Write-Host "Done. If packages fail to build (maturin/Rust or numpy/CMake errors), install official Windows Python or the required toolchain (Rust/CMake/Ninja/Visual C++)." -ForegroundColor Yellow


































# Minimal venv reset + installer script (robust/simple)
# Run from project root: powershell -ExecutionPolicy Bypass -File .\resetup_venv.ps1

$preferred = 'py -3'
try { & $preferred -V | Out-Null } catch { $preferred = 'python' }
Write-Host "Using Python command: $preferred"

Write-Host "Python info:"; & $preferred -c "import sys; print(sys.executable, sys.version.replace('\n',' '), sys.platform)"

if (Test-Path .\venv) { Remove-Item -Recurse -Force .\venv }
& $preferred -m venv venv
Write-Host "Created venv using: $preferred"

# Use the venv python directly for installs
$vp = ".\venv\Scripts\python.exe"
& $vp -m pip install --upgrade pip setuptools wheel

# Install certifi and set SSL_CERT_FILE to help with certificate verification
& $vp -m pip install certifi
$certPath = & $vp -c "import certifi; print(certifi.where())"
if ($certPath) { $env:SSL_CERT_FILE = $certPath.Trim(); Write-Host "Set SSL_CERT_FILE to $env:SSL_CERT_FILE" }

# Install requirements with a fallback to --trusted-host if SSL or network errors occur
try {
    & $vp -m pip install -r requirements.txt
} catch {
    Write-Warning "Install failed; retrying with --trusted-host pypi.org --trusted-host files.pythonhosted.org"
    & $vp -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
}

Write-Host "Done. If packages fail to build (maturin/Rust or numpy/CMake errors), install official Windows Python or the required toolchain (Rust/CMake/Ninja/Visual C++)." -ForegroundColor Yellow
