#!/usr/bin/env bash
# KiCad AI PCB Copilot & Auto-Router Installer (Linux & macOS)
set -e

PLUGIN_NAME="kicad_ai_copilot"
echo "======================================================="
echo "  KiCad AI PCB Copilot - Linux / macOS Kurulum Aracı"
echo "======================================================="
echo ""

if [[ "$OSTYPE" == "darwin"* ]]; then
    BASE_DIR="$HOME/Library/Application Support/kicad"
else
    BASE_DIR="$HOME/.local/share/kicad"
fi

INSTALLED=0

for VER in "8.0" "7.0"; do
    TARGET_VER_DIR="$BASE_DIR/$VER/scripting/plugins/$PLUGIN_NAME"
    if [ -d "$BASE_DIR/$VER" ]; then
        echo "-> KiCad $VER bulundu: $TARGET_VER_DIR"
        mkdir -p "$TARGET_VER_DIR"
        cp plugins/* "$TARGET_VER_DIR/"
        echo "   Dosyalar başarıyla kopyalandı."
        INSTALLED=1
    fi
done

if [ $INSTALLED -eq 0 ]; then
    echo "-> KiCad 8.0 dizini oluşturuluyor..."
    TARGET_VER_DIR="$BASE_DIR/8.0/scripting/plugins/$PLUGIN_NAME"
    mkdir -p "$TARGET_VER_DIR"
    cp plugins/* "$TARGET_VER_DIR/"
fi

echo ""
echo "======================================================="
echo "  Kurulum Başarıyla Tamamlandı!"
echo "======================================================="
echo "KiCad PCB Düzenleyici -> Araçlar -> Dış Eklentiler -> Eklentileri Yenile yapın."
echo ""
