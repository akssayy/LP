# AI Agent — Setup Notes

💡 **Goal:** Get a working Python environment on Windows that can successfully install dependencies from `requirements.txt`.

## Recommended steps (Windows) ✅
1. Install the official Python installer from https://www.python.org/downloads/ (choose the latest 3.11/3.12 and check "Add Python to PATH").
2. From the project root, create a venv: `py -3 -m venv venv`
3. Activate in PowerShell: `.\\venv\\Scripts\\Activate.ps1` (or in CMD: `.\\venv\\Scripts\\activate.bat`).
4. Upgrade packaging tools: `python -m pip install --upgrade pip setuptools wheel`.
5. Install dependencies: `python -m pip install -r requirements.txt`.

> ⚠️ If you encounter SSL certificate errors when pip downloads packages, try one of these:
> - Use `python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt` (temporary workaround).
> - Ensure your system Python has a valid certificate store (install official Windows Python), or set the `SSL_CERT_FILE` environment variable pointing to a CA bundle (e.g., from the `certifi` package).

## Notes on common errors 🔧
- If you see build errors for `pydantic-core` or `numpy` mentioning Rust or CMake, it usually means pip is building from source because a compatible prebuilt wheel isn't available for your Python/OS combination. Using the official Windows Python (not MSYS/MinGW) usually resolves this because wheels are available for that platform.
- If you must build from source, install build tools: Rust toolchain (for pydantic-core), `cmake`/`ninja` (for numpy), and system compilers.

---

If you want, I can add a small PowerShell script to automate these Windows setup steps. ✅

## Troubleshooting: MSYS / MinGW Python issues ⚠️
- Symptom: install fails with messages like "Unsupported platform: 311" or errors while building `pydantic-core` (maturin/Rust) or `numpy` (CMake/Ninja). This usually means your Python is an MSYS/MinGW build (e.g., paths containing `msys` or `ucrt64`) where prebuilt wheels aren't available.

- Fix options:
  1. Preferred: Install official Windows Python from https://www.python.org and recreate the venv with `py -3 -m venv venv`. Then run the setup script `.
esetup_venv.ps1` in PowerShell. ✅
  2. If you must keep the current Python, install the required toolchain: Rust toolchain (for maturin), `cmake` and `ninja`, and Visual C++ build tools. This is more work and error-prone. 🔧
  3. Use Conda/Mamba to install binary packages if you prefer managing native dependencies that way. 🐍

- Quick diagnostics: run the included `diagnose_env.py` with your venv Python to print platform/executable info and cert details:

  `.
venv\Scripts\python.exe diagnose_env.py`

If you'd like, run `.
esetup_venv.ps1` now and I can review the output with you.
