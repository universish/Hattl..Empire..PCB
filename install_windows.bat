@echo off
chcp 65001 >nul
echo =======================================================
echo   KiCad AI PCB Copilot - 1-Tikla Windows Kurulum Araci
echo =======================================================
echo.

set PLUGIN_NAME=kicad_ai_copilot
set INSTALLED=0

echo -^> Building High-Performance Rust Engine...
cargo --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Cargo (Rust) is not installed. Please install it first.
    pause
    exit /b 1
)

cd plugins\engine
set RUSTFLAGS=-C target-cpu=native
cargo build --release
cd ..\..

if exist "%APPDATA%\kicad\10.0" (
    set TARGET_DIR="%APPDATA%\kicad\10.0\scripting\plugins\%PLUGIN_NAME%"
    echo [1/2] KiCad 10.0 bulundu. Hedef: %TARGET_DIR%
    mkdir %TARGET_DIR% 2>nul
    xcopy plugins %TARGET_DIR%\ /E /I /Y >nul
    echo       Dosyalar basariyla kopyalandi.
    set INSTALLED=1
)

if %INSTALLED%==0 (
    echo [BILGI] Varsayilan KiCad 10.0 dizinine kuruluyor...
    set TARGET_DIR="%APPDATA%\kicad\10.0\scripting\plugins\%PLUGIN_NAME%"
    mkdir %TARGET_DIR% 2>nul
    xcopy plugins %TARGET_DIR%\ /E /I /Y >nul
)

echo.
echo =======================================================
echo   Kurulum Tamamlandi!
echo =======================================================
echo KiCad PCB Duzenleyiciyi acin, "Araclar" -> "Dis Eklentiler"
echo -> "Eklentileri Yenile"ye basin.
echo.
pause
