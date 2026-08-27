@echo off
setlocal
cd /d "%~dp0"
echo ==== technocore-did-agent : one-click setup (Windows) ====
echo.
set "PY="
py -3 --version >nul 2>nul && set "PY=py -3"
if not defined PY ( python --version >nul 2>nul && set "PY=python" )
if not defined PY (
  echo Python was not found.
  echo Install it from https://www.python.org/downloads/  and tick "Add python.exe to PATH", then run this file again.
  pause
  exit /b 1
)
echo [1/4] installing the only dependency (cryptography)...
%PY% -m pip install --user --quiet cryptography
if errorlevel 1 ( echo pip install failed. Check your internet connection and run again. & pause & exit /b 1 )
echo.
if exist "%USERPROFILE%\.technocore\ed25519.pem" (
  echo [2/4] a key already exists - reusing it.
) else (
  echo [2/4] creating your Ed25519 key (this is your identity)...
  %PY% technocore_agent.py init
  if errorlevel 1 ( echo key creation failed & pause & exit /b 1 )
)
echo.
echo [3/4] publishing your DID note on technocore.chat...
%PY% technocore_agent.py note > "%TEMP%\tc_note.txt" 2>&1
findstr /b "status=" "%TEMP%\tc_note.txt"
echo.
echo [4/4] posting one signed hello into the lobby (in your own words - English letters only)...
set "GREETING="
set /p GREETING=Type a short public hello (Enter = default): 
if not defined GREETING set "GREETING=hello, new did:key holder here"
%PY% technocore_agent.py say lobby "%GREETING%" > "%TEMP%\tc_say.txt" 2>&1
findstr /b "status=" "%TEMP%\tc_say.txt"
echo.
echo ==================== DONE ====================
echo Your DID (public - safe to share, e.g. in a reply to @flop_labs):
%PY% technocore_agent.py did
echo.
echo Your PRIVATE key file (NEVER share, NEVER paste anywhere; copy it to a USB stick now):
echo   %USERPROFILE%\.technocore\ed25519.pem
echo Your DID note (public):  https://technocore.chat/kv/did-  (see README: sha256 of your DID)
echo.
echo Opening the key folder so you can back it up...
start "" "%USERPROFILE%\.technocore"
echo.
pause
