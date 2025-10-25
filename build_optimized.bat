@echo off
echo ========================================
echo    DICOM Viewer Pro - Optimized Build
echo    Copyright (c) 2025 @Tins
echo ========================================
echo.

echo [1/5] Cleaning previous builds...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "__pycache__" rmdir /s /q "__pycache__"
echo ✓ Cleaned previous builds

echo.
echo [2/5] Installing PyInstaller and UPX...
pip install pyinstaller
echo ✓ PyInstaller installed

echo.
echo [3/5] Building optimized executable...
pyinstaller --clean --onefile --windowed --optimize=2 --strip ^
    --exclude-module matplotlib ^
    --exclude-module scipy ^
    --exclude-module pandas ^
    --exclude-module jupyter ^
    --exclude-module IPython ^
    --exclude-module notebook ^
    --exclude-module tornado ^
    --exclude-module zmq ^
    --exclude-module sqlite3 ^
    --exclude-module unittest ^
    --exclude-module test ^
    --exclude-module tests ^
    --exclude-module distutils ^
    --exclude-module setuptools ^
    --exclude-module pip ^
    --exclude-module wheel ^
    --exclude-module pkg_resources ^
    --name "DICOM_Viewer_Pro" ^
    dicom_to_png_converter.py
echo ✓ Optimized build completed

echo.
echo [4/5] Checking result...
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
echo [5/5] Creating distribution package...
if exist "dist\DICOM_Viewer_Pro.exe" (
    if not exist "Distribution" mkdir "Distribution"
    copy "dist\DICOM_Viewer_Pro.exe" "Distribution\"
    copy "HUONG_DAN_SU_DUNG.txt" "Distribution\"
    echo ✓ Distribution package created in 'Distribution' folder
    echo.
    echo 📦 Files ready for customer:
    echo    - DICOM_Viewer_Pro.exe (Main application)
    echo    - HUONG_DAN_SU_DUNG.txt (User guide)
)

echo.
echo Press any key to exit...
pause >nul
