@echo off
echo ========================================
echo    DICOM Viewer Pro - Build Script
echo    Copyright (c) 2025 @Tins
echo ========================================
echo.

echo [1/4] Cleaning previous builds...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "__pycache__" rmdir /s /q "__pycache__"
echo ✓ Cleaned previous builds

echo.
echo [2/4] Installing PyInstaller...
pip install pyinstaller
echo ✓ PyInstaller installed

echo.
echo [3/4] Building executable...
pyinstaller --clean dicom_viewer.spec
echo ✓ Build completed

echo.
echo [4/4] Checking result...
if exist "dist\DICOM_Viewer_Pro.exe" (
    echo ✓ SUCCESS: DICOM_Viewer_Pro.exe created!
    echo.
    echo File location: dist\DICOM_Viewer_Pro.exe
    echo File size: 
    dir "dist\DICOM_Viewer_Pro.exe" | findstr "DICOM_Viewer_Pro.exe"
    echo.
    echo 🎉 Ready to distribute to customers!
    echo 💡 The .exe file is completely standalone - no installation required!
) else (
    echo ❌ ERROR: Build failed!
    echo Please check the error messages above.
)

echo.
echo Press any key to exit...
pause >nul
