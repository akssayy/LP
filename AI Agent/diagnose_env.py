import sys, sysconfig, platform, ssl
try:
    import certifi
except Exception:
    certifi = None

print('platform:', sys.platform)
print('executable:', sys.executable)
print('python_version:', sys.version.replace('\n',' '))
print('sysconfig.get_platform():', sysconfig.get_platform())
print('ssl.OPENSSL_VERSION:', getattr(ssl, 'OPENSSL_VERSION', 'unknown'))
print('certifi:', certifi.where() if certifi else 'missing')

print('\nTip: If you see paths containing "msys", "ucrt64", or "mingw", recreate your venv using the Windows Python launcher `py -3 -m venv venv` and then run `resetup_venv.ps1`.')