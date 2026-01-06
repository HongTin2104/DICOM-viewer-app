# DICOM to PNG Converter

This Python application converts DICOM (.dcm) files to PNG images with a user-friendly graphical interface.

## Features

- Convert DICOM files to PNG
- **Batch processing** - Process multiple files at once
- Simple and intuitive GUI
- Option to normalize pixel values (0-255)
- Option to invert colors
- Adjust PNG quality
- Supports both grayscale and color images
- Progress bar and status notifications
- Command line interface with batch mode

## System Requirements

- Python 3.7 or above
- Windows/Linux/macOS

## Installation

1. **Clone or download the project:**
   ```bash
   git clone <repository-url>
   cd DICOM-viewer-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install pydicom Pillow numpy
   ```

## Usage

### Option 1: Run GUI Application

```bash
python dicom_to_png_converter.py
```

### Option 2: Use the Command Line

#### Single File Mode:
```bash
python cli_converter.py input.dcm output.png
```

#### Batch Processing Mode:
```bash
python cli_converter.py --batch --input-dir folder_input --output-dir folder_output
```

## GUI Usage Guide

1. **Launch the Application:**
   - Run `python dicom_to_png_converter.py`
   - The graphical interface will appear.

2. **Select DICOM Files:**
   - **Single File:** Click "Select Single File" to choose one DICOM file.
   - **Multiple Files:** Click "Select Multiple Files" to choose multiple DICOM files at once.
   - The selected files will appear in the list box.
   - You can remove individual items or clear all files.

3. **Select the Output Folder:**
   - Click the "Browse" button next to "Output PNG Folder."
   - Choose the folder to save PNG files.

4. **Customization Options:**
   - **Normalize Pixel Values:** Normalize pixel values to a 0-255 range (recommended to enable).
   - **Invert Colors:** Option to invert colors (optional).
   - **PNG Quality:** Adjust from 50-100%.

5. **Convert Files:**
   - Click the "Convert DICOM to PNG" button.
   - The progress bar will show the processing progress.
   - The status label will update with the current file being processed.
   - Wait for the process to complete.
   - PNG files will be saved in the selected output folder.

## Project Structure

```
DICOM-viewer-app/
├── dicom_to_png_converter.py    # GUI script with batch processing
├── cli_converter.py             # CLI script with batch mode
├── test_batch.py                # Batch processing test script
├── simple_test.py               # Simple test script
├── requirements.txt             # Dependencies list
├── README.md                    # This guide
└── run_gui.bat                  # Windows batch script
```

## Common Issues

### "ModuleNotFoundError" Error
```bash
pip install -r requirements.txt
```

### "DICOM file not found" Error
- Verify the file path is correct.
- Ensure the file has a .dcm extension.

### "Unsupported Image Format" Error
- The DICOM file might have an unsupported format.
- Try enabling the "Normalize Pixel Values" option.

### Output Image is Too Dark or Bright
- Try toggling the "Invert Colors" option.
- Ensure "Normalize Pixel Values" is enabled.

## API Reference

### Class DICOMToPNGConverter

#### Methods:
- `browse_input_file()`: Select input DICOM file.
- `browse_output_dir()`: Select output folder for PNG files.
- `normalize_pixel_array(pixel_array)`: Normalize pixel array values.
- `convert_dicom_to_png()`: Perform file conversion.

## Contributing

If you wish to contribute to the project:

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to your branch.
5. Create a Pull Request.

## License

MIT License - See the LICENSE file for details.

## Contact

For issues or questions, please open an issue on GitHub.

---

**Note:** This application is designed for educational and research purposes. For commercial medical applications, ensure compliance with DICOM and medical regulations.