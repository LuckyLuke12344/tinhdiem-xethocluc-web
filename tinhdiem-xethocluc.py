def xep_loai_hoc_luc():
    print("=== Ứng dụng Xếp loại Học lực (Python) ===")
    ten = input("Nhập họ tên học sinh: ")

    # Nhập điểm các môn
    try:
        toan = float(input("Điểm Toán: "))
        van = float(input("Điểm Văn: "))
        anh = float(input("Điểm Anh: "))
        khtn = float(input("Điểm KHTN: "))
        su_dia = float(input("Điểm Sử - Địa: "))
        gdcd = float(input("Điểm GDCD: "))
        tin = float(input("Điểm Tin học: "))
        cn = float(input("Điểm Công nghệ: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập số hợp lệ cho các điểm.")
        return

    # Nhận xét đạt hay không
    print("\nCác môn nhận xét của bạn có đạt hết không?")
    print("1. Có (Tất cả đạt)")
    print("2. Không (Có 1, 2... môn không đạt)")
    nhanxet = input("Chọn (1 hoặc 2): ")

    if nhanxet != "1" and nhanxet != "2":
        print("Lỗi: Vui lòng chọn 1 hoặc 2.")
        return

    tat_ca_diem = [toan, van, anh, khtn, su_dia, gdcd, tin, cn]
    dtb = sum(tat_ca_diem) / len(tat_ca_diem)

    # Xét học lực
    loai = "Kém"  # Mặc định
    if nhanxet == "2":
        loai = "Yếu"
    elif dtb >= 8.0 and (toan >= 8.0 or van >= 8.0) and all(d >= 6.5 for d in tat_ca_diem):
        loai = "Giỏi"
    elif dtb >= 6.5 and (toan >= 6.5 or van >= 6.5) and all(d >= 5.0 for d in tat_ca_diem):
        loai = "Khá"
    elif dtb >= 5.0 and (toan >= 5.0 or van >= 5.0) and all(d >= 3.5 for d in tat_ca_diem):
        loai = "Trung bình"
    elif dtb >= 3.5 and all(d >= 2.0 for d in tat_ca_diem):
        loai = "Yếu"

    # Kết quả
    print("\n--- Kết quả ---")
    print(f"Học sinh: {ten}")
    print(f"Điểm trung bình: {dtb:.2f}")
    print(f"Xếp loại học lực: {loai}")

# Gọi hàm chạy
xep_loai_hoc_luc()
