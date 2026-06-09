from datetime import datetime
import pytz

def main():
    # Định vị giờ Việt Nam
    tz = pytz.timezone('Asia/Ho_Chi_Minh')
    gio_hien_tai = datetime.now(tz).hour
    
    # Chọn file mẫu tương ứng với khung giờ
    if 7 <= gio_hien_tai < 12:
        file_mau = "sáng.m3u8"
        tien_to = "sáng"
    else:
        file_mau = "tối.m3u8"
        tien_to = "tối"

    # Đọc file mẫu để lấy danh sách các đoạn video .ts
    with open(file_mau, "r") as f:
        lines = f.readlines()

    # Sửa đường dẫn tĩnh trong file thành link Raw tuyệt đối của GitHub
    link_goc_git = "https://raw.githubusercontent.com/vchessdev/m3u8/main/"
    
    new_lines = []
    for line in lines:
        if line.startswith(tien_to) and line.strip().endswith(".ts"):
            # Chuyển tên file cục bộ thành link GitHub công cộng
            new_lines.append(link_goc_git + line)
        else:
            new_lines.append(line)

    # Ghi đè vào file live.m3u8 chính thức
    with open("live.m3u8", "w") as f:
        f.writelines(new_lines)

    print("Đã tráo ruột luồng phát thành công!")

if __name__ == "__main__":
    main()
