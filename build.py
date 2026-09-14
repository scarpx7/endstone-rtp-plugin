#!/usr/bin/env python3
"""
Build script for Endstone RTP Plugin
Creates .whl distribution package
"""

import os
import sys
import subprocess

def build_wheel():
    """Build the wheel distribution"""
    print("\n" + "="*60)
    print("Building Endstone RTP Plugin Wheel Distribution")
    print("="*60 + "\n")
    
    # Install build dependencies
    print("[1/3] Installing build dependencies...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", 
        "wheel", "setuptools", "--upgrade"
    ])
    print("✓ Dependencies installed\n")
    
    # Build wheel
    print("[2/3] Building wheel distribution...")
    subprocess.check_call([
        sys.executable, "setup.py", "bdist_wheel"
    ])
    print("✓ Wheel built successfully\n")
    
    # List generated files
    print("[3/3] Generated files:")
    dist_dir = "dist"
    if os.path.exists(dist_dir):
        for filename in os.listdir(dist_dir):
            filepath = os.path.join(dist_dir, filename)
            size = os.path.getsize(filepath) / 1024  # KB
            print(f"  ✓ {filename} ({size:.2f} KB)")
    
    print("\n" + "="*60)
    print("Build completed successfully!")
    print("Install with: pip install dist/endstone_rtp_plugin-*.whl")
    print("="*60 + "\n")

if __name__ == "__main__":
    try:
        build_wheel()
    except Exception as e:
        print(f"\n✗ Build failed: {e}")
        sys.exit(1)
