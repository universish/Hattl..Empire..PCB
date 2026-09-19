@echo off
chcp 65001 >nul
echo =======================================================
echo   KiCad AI PCB Copilot - 1-Tikla Windows Kurulum Araci
echo =======================================================
echo.

set PLUGIN_NAME=kicad_ai_copilot
set INSTALLED=0

if exist "%APPDATA%\kicad\8.0" (
    set TARGET_DIR=%APPDATA%\kicad\8.0\scripting\plugins\%PLUGIN_NAME%
    echo [1/2] KiCad 8.0 bulundu. Hedef: %TARGET_DIR%
    mkdir "%TARGET_DIR%" 2>nul
    copy plugins\*.* "%TARGET_DIR%\" /Y >nul
    echo       Dosyalar basariyla kopyalandi.
    set INSTALLED=1
)

if exist "%APPDATA%\kicad\7.0" (
    set TARGET_DIR=%APPDATA%\kicad\7.0\scripting\plugins\%PLUGIN_NAME%
    echo [2/2] KiCad 7.0 bulundu. Hedef: %TARGET_DIR%
    mkdir "%TARGET_DIR%" 2>nul
    copy plugins\*.* "%TARGET_DIR%\" /Y >nul
    echo       Dosyalar basariyla kopyalandi.
    set INSTALLED=1
)

if %INSTALLED%==0 (
    echo [BILGI] Varsayilan KiCad 8.0 dizinine kuruluyor...
    set TARGET_DIR=%APPDATA%\kicad\8.0\scripting\plugins\%PLUGIN_NAME%
    mkdir "%TARGET_DIR%" 2>nul
    copy plugins\*.* "%TARGET_DIR%\" /Y >nul
)

echo.
echo =======================================================
echo   Kurulum Tamamlandi!
echo =======================================================
echo KiCad PCB Duzenleyiciyi acin, "Araclar" -> "Dis Eklentiler"
echo -> "Eklentileri Yenile"ye basin.
echo.
pause
