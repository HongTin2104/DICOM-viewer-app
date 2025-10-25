# DICOM to PNG Converter

Ứng dụng Python để chuyển đổi file DICOM (.dcm) thành ảnh PNG với giao diện đồ họa thân thiện.

## Tính năng

- ✅ Chuyển đổi file DICOM thành PNG
- ✅ **Batch processing** - Xử lý nhiều file cùng lúc
- ✅ Giao diện GUI đơn giản và dễ sử dụng
- ✅ Tùy chọn chuẩn hóa pixel values (0-255)
- ✅ Tùy chọn đảo ngược màu sắc
- ✅ Điều chỉnh chất lượng PNG
- ✅ Hỗ trợ cả ảnh grayscale và color
- ✅ Progress bar và thông báo trạng thái
- ✅ Command line interface với batch mode

## Yêu cầu hệ thống

- Python 3.7 trở lên
- Windows/Linux/macOS

## Cài đặt

1. **Clone hoặc tải về project:**
   ```bash
   git clone <repository-url>
   cd DICOM-viewer-app
   ```

2. **Cài đặt các thư viện cần thiết:**
   ```bash
   pip install -r requirements.txt
   ```

   Hoặc cài đặt thủ công:
   ```bash
   pip install pydicom Pillow numpy
   ```

## Sử dụng

### Cách 1: Chạy ứng dụng GUI

```bash
python dicom_to_png_converter.py
```

### Cách 2: Sử dụng từ command line

#### Single file mode:
```bash
python cli_converter.py input.dcm output.png
```

#### Batch processing mode:
```bash
python cli_converter.py --batch --input-dir folder_input --output-dir folder_output
```

## Hướng dẫn sử dụng GUI

1. **Mở ứng dụng:**
   - Chạy `python dicom_to_png_converter.py`
   - Giao diện sẽ hiện ra

2. **Chọn file DICOM:**
   - **Chọn file đơn**: Nhấn "Chọn file đơn" để chọn một file DICOM
   - **Chọn nhiều file**: Nhấn "Chọn nhiều file" để chọn nhiều file DICOM cùng lúc
   - Danh sách file đã chọn sẽ hiển thị trong Listbox
   - Có thể xóa file đã chọn hoặc xóa tất cả

3. **Chọn thư mục xuất:**
   - Nhấn nút "Browse" bên cạnh "Thư mục xuất PNG"
   - Chọn thư mục để lưu file PNG

4. **Tùy chỉnh:**
   - **Normalize pixel values**: Chuẩn hóa giá trị pixel về khoảng 0-255 (khuyến nghị bật)
   - **Invert colors**: Đảo ngược màu sắc (tùy chọn)
   - **Chất lượng PNG**: Điều chỉnh từ 50-100%

5. **Chuyển đổi:**
   - Nhấn nút "Convert DICOM to PNG"
   - Progress bar sẽ hiển thị tiến trình xử lý
   - Status label sẽ cập nhật file đang xử lý
   - Chờ quá trình chuyển đổi hoàn tất
   - File PNG sẽ được lưu trong thư mục đã chọn

## Cấu trúc project

```
DICOM-viewer-app/
├── dicom_to_png_converter.py    # Script GUI với batch processing
├── cli_converter.py             # Script CLI với batch mode
├── test_batch.py               # Script test batch processing
├── simple_test.py              # Script test đơn giản
├── requirements.txt            # Danh sách thư viện cần thiết
├── README.md                   # Hướng dẫn này
└── run_gui.bat                # Script batch Windows
```

## Xử lý lỗi thường gặp

### Lỗi "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Lỗi "File DICOM không tồn tại"
- Kiểm tra đường dẫn file có đúng không
- Đảm bảo file có extension .dcm

### Lỗi "Unsupported image format"
- File DICOM có thể có định dạng không được hỗ trợ
- Thử bật tùy chọn "Normalize pixel values"

### Ảnh xuất ra bị tối hoặc sáng quá
- Thử bật/tắt tùy chọn "Invert colors"
- Đảm bảo "Normalize pixel values" được bật

## API Reference

### Class DICOMToPNGConverter

#### Methods:
- `browse_input_file()`: Chọn file DICOM đầu vào
- `browse_output_dir()`: Chọn thư mục xuất PNG
- `normalize_pixel_array(pixel_array)`: Chuẩn hóa mảng pixel
- `convert_dicom_to_png()`: Thực hiện chuyển đổi

## Đóng góp

Nếu bạn muốn đóng góp vào project:

1. Fork repository
2. Tạo branch mới cho tính năng của bạn
3. Commit các thay đổi
4. Push lên branch
5. Tạo Pull Request

## License

MIT License - Xem file LICENSE để biết thêm chi tiết.

## Liên hệ

Nếu có vấn đề hoặc câu hỏi, vui lòng tạo issue trên GitHub.

---

**Lưu ý:** Ứng dụng này được thiết kế cho mục đích giáo dục và nghiên cứu. Đối với các ứng dụng y tế thương mại, vui lòng đảm bảo tuân thủ các quy định về DICOM và y tế.
