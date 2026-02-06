# Small robust installer helper
# Run: powershell -ExecutionPolicy Bypass -File .\fix_env.ps1

$preferred = 'py -3'
try { & $preferred -V | Out-Null } catch { $preferred = 'python' }
Write-Host "Using Python command: $preferred"

Write-Host "Python info:"; & $preferred -c "import sys; print(sys.executable, sys.version.replace('\n',' '), sys.platform)"

if (Test-Path .\venv) { Remove-Item -Recurse -Force .\venv }
& $preferred -m venv venv
Write-Host "Created venv using: $preferred"

# Detect venv layout
if (Test-Path .\venv\Scripts\python.exe) {
    $vp = ".\venv\Scripts\python.exe"
} elseif (Test-Path .\venv\bin\python.exe) {
    $vp = ".\venv\bin\python.exe"
} else {
    Write-Error "Couldn't find a python executable in the venv (Scripts/ or bin/)."
    exit 1
}

& $vp -m pip install --upgrade pip setuptools wheel

# Install certifi to avoid SSL errors
& $vp -m pip install certifi
$certPath = & $vp -c "import certifi; print(certifi.where())"
if ($certPath) { $env:SSL_CERT_FILE = $certPath.Trim(); Write-Host "Set SSL_CERT_FILE to $env:SSL_CERT_FILE" }

# Try installing requirements
try {
    & $vp -m pip install -r requirements.txt
} catch {
    Write-Warning "Install failed; retrying with --trusted-host pypi.org --trusted-host files.pythonhosted.org"
    & $vp -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
}

Write-Host "Finished. If build failures persist (pydantic-core/numpy), install official Windows Python from python.org or install Rust/CMake/Ninja and Visual C++ build tools." -ForegroundColor Yellow