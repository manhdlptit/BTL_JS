# seed_data.py
import app  # Import biến app trực tiếp từ file app.py của bạn
from app.blueprints.model import db, Movies, Showtimes

# Cần bọc trong app_context để SQLAlchemy hiểu cấu hình Database cấu hình trong Flask
with app.app_context():
    # 1. Lấy toàn bộ 9 bộ phim đang có trong database của bạn
    danh_sach_phim = Movies.query.all()
    
    if not danh_sach_phim:
        print("❌ Không tìm thấy phim nào trong Database. Vui lòng thêm phim trước!")
    else:
        # 2. Định nghĩa các khung giờ mẫu bạn muốn tạo cho từng phim
        khung_gio_mau = ["08:30", "11:15", "14:00", "16:45", "19:30", "22:15"]
        
        so_suat_them = 0
        
        # 3. Duyệt qua từng bộ phim để chèn suất chiếu tương ứng
        for phim in danh_sach_phim:
            for gio in khung_gio_mau:
                # Kiểm tra trùng lặp trước khi thêm để tránh bị kích lỗi lặp dữ liệu
                trung_lap = Showtimes.query.filter_by(showtime=gio, id_movie=phim.id_movie).first()
                
                if not trung_lap:
                    suat_chieu_moi = Showtimes(showtime=gio, id_movie=phim.id_movie)
                    db.session.add(suat_chieu_moi)
                    so_suat_them += 1
        
        # 4. Xác nhận lưu thay đổi vào file user.db
        if so_suat_them > 0:
            db.session.commit()
            print(f"🎉 Thành công! Đã tự động chèn thêm {so_suat_them} suất chiếu cho {len(danh_sach_phim)} bộ phim.")
        else:
            print("✨ Toàn bộ các suất chiếu đã tồn tại sẵn, không cần chèn thêm dữ liệu.")