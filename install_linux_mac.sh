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

echo "-> Building High-Performance Rust Engine (AVX2 / Fedora Optimized)..."
if command -v cargo &> /dev/null; then
    cd plugins/engine
    # Set RUSTFLAGS for AVX2 optimization on supported hardware
    RUSTFLAGS="-C target-cpu=native" cargo build --release
    cd ../../
    echo "   Rust build successful."
else
    echo "   [ERROR] Cargo (Rust) is not installed. Please install rustup: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"
    exit 1
fi

for VER in "10.0" "9.0" "8.0" "7.0"; do
    TARGET_VER_DIR="$BASE_DIR/$VER/scripting/plugins/$PLUGIN_NAME"
    if [ -d "$BASE_DIR/$VER" ]; then
        echo "-> KiCad $VER bulundu: $TARGET_VER_DIR"
        mkdir -p "$TARGET_VER_DIR"
        cp -r plugins/* "$TARGET_VER_DIR/"
        echo "   Dosyalar başarıyla kopyalandı."
        INSTALLED=1
    fi
done

if [ $INSTALLED -eq 0 ]; then
    echo "-> KiCad 10.0 dizini oluşturuluyor..."
    TARGET_VER_DIR="$BASE_DIR/10.0/scripting/plugins/$PLUGIN_NAME"
    mkdir -p "$TARGET_VER_DIR"
    cp -r plugins/* "$TARGET_VER_DIR/"
fi

echo ""
echo "======================================================="
echo "  Kurulum Başarıyla Tamamlandı!"
echo "======================================================="
echo "KiCad PCB Düzenleyici -> Araçlar -> Dış Eklentiler -> Eklentileri Yenile yapın."
echo ""
