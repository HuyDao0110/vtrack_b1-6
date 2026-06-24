import streamlit as st
import os

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="YTrack - Ứng dụng nghe nhạc", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- HÀM THÔNG MINH TỰ ĐỘNG KHỚP FILE (Bất chấp viết hoa/thường) ---
def lay_anh(ten_file_goc):
    # Tìm xem trong thư mục có file nào trùng tên (không phân biệt hoa thường) không
    ten_thap = ten_file_goc.lower()
    if os.path.exists(ten_file_goc):
        return ten_file_goc
    # Quét phòng hờ trường hợp file trên GitHub bị đổi thành chữ HOA (.PNG hoặc .JPG)
    for f in os.listdir("."):
        if f.lower() == ten_thap:
            return f
    return ten_file_goc

# --- 1. THANH ĐIỀU HƯỚNG (Ép mỏng tối đa, fix lỗi logo to) ---
# Đặt cột đầu tiên là 0.5 để ép khung logo nhỏ lại, không làm phình menu
nav = st.columns([0.5, 6.0, 1.7, 1.8])

with nav[0]:
    st.image(lay_anh("logo.png"), width=60) # Ép logo về hẳn bản nhỏ gọn

with nav[1]:
    st.text_input("Tìm kiếm...", label_visibility="collapsed")

with nav[2]:
    c1, c2 = st.columns(2)
    if c1.button("🏠 Home", use_container_width=True): st.session_state.page = "Home"
    if c2.button("📚 Thư viện", use_container_width=True): st.session_state.page = "Thư viện"

with nav[3]:
    c3, c4 = st.columns(2)
    if c3.button("Đăng nhập", use_container_width=True): st.session_state.page = "Đăng nhập"
    if c4.button("Đăng ký", use_container_width=True): st.session_state.page = "Đăng ký"

st.write("---")

# --- 2. QUẢN LÝ CÁC TRANG ---
if st.session_state.page == "Home":
    st.write("# Nghe gì hôm nay, User?")
    
    st.image(lay_anh("best_notification.png"), use_container_width=True)

    # --- NGHỆ SĨ PHỔ BIẾN ---
    st.write("## Nghệ sĩ phổ biến")
    art_cols = st.columns(5)
    artists = [
        ("Sơn Tùng M-TP", "A1.png"),
        ("SOOBIN", "A2.png"),
        ("bùi trường linh", "A3.png"),
        ("Trang Pháp", "A4.png"),
        ("Xem thêm", "A5.png")
    ]
    for i, (name, file_name) in enumerate(artists):
        with art_cols[i]:
            st.image(lay_anh(file_name), caption=name, use_container_width=True)

    # --- ALBUM NỔI BẬT ---
    st.write("## Album nổi bật")
    alb_cols = st.columns(6)
    albums = ["B1.png", "B2.png", "B3.png", "B4.png", "B5.png", "B6.png"]
    for i, file_name in enumerate(albums):
        with alb_cols[i]:
            st.image(lay_anh(file_name), use_container_width=True)

    # --- BXH BÀI HÁT NỔI BẬT THÁNG NÀY ---
    st.write("## BXH bài hát nổi bật *Tháng này*")
    bxh_l, bxh_r = st.columns([3.5, 6.5])
    with bxh_l:
        st.image(lay_anh("come_my_way.png"), use_container_width=True)
            
    with bxh_r:
        songs = [
            {"rank": "2", "title": "Em", "artist": "Binz"},
            {"rank": "3", "title": "Nếu như ta chẳng còn", "artist": "RPT MCK"},
            {"rank": "4", "title": "IDK", "artist": "RPT MCK"},
            {"rank": "5", "title": "Nguyễn Văn Mười", "artist": "RPT MCK"}
        ]
        for s in songs:
            sl, sr = st.columns([8, 2])
            sl.write(f"{s['rank']}. {s['title']}")
            sr.write(f"**{s['artist']}**")

elif st.session_state.page == "Nghệ sĩ":
    if st.button("⬅ Quay lại"): st.session_state.page = "Home"
    st.write("---")
    l, r = st.columns([4, 6])
    with l:
        st.image(lay_anh("trang_phap.png"), use_container_width=True)
    with r:
        st.write("# Trang Pháp và hành trình")
        st.write("▶ Phát tất cả | 7 bài hát")

elif st.session_state.page == "Thư viện":
    st.image(lay_anh("thu_vien_yeu_thich.png"), use_container_width=True)
    if st.button("Trở về"): st.session_state.page = "Home"
