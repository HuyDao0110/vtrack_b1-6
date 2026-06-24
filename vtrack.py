import streamlit as st
import os

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="YTrack - Ứng dụng nghe nhạc", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- HÀM TỰ ĐỘNG KHỚP FILE (Bất chấp viết hoa/thường) ---
def lay_anh(ten_file_goc):
    ten_thap = ten_file_goc.lower()
    if os.path.exists(ten_file_goc):
        return ten_file_goc
    for f in os.listdir("."):
        if f.lower() == ten_thap:
            return f
    return ten_file_goc

# --- 1. THANH ĐIỀU HƯỚNG SIÊU MỎNG ---
# Thu nhỏ cột tìm kiếm một chút và gom nút để không sinh khoảng đệm dọc dư thừa
nav = st.columns([0.6, 4.6, 1.2, 1.2, 1.2, 1.2])

with nav[0]:
    st.image(lay_anh("logo.png"), width=55) # Logo nhỏ tinh tế

with nav[1]:
    st.text_input("Tìm kiếm...", label_visibility="collapsed")

with nav[2]:
    if st.button("🏠 Home", use_container_width=True): st.session_state.page = "Home"
with nav[3]:
    if st.button("📚 Thư viện", use_container_width=True): st.session_state.page = "Thư viện"
with nav[4]:
    if st.button("Đăng nhập", use_container_width=True): st.session_state.page = "Đăng nhập"
with nav[5]:
    if st.button("Đăng ký", use_container_width=True): st.session_state.page = "Đăng ký"

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

    # --- BXH BÀI HÁT NỔI BẬT THÁNG NÀY (ĐỦ TỪ 1 ĐẾN 10) ---
    st.write("## BXH bài hát nổi bật *Tháng này*")
    bxh_l, bxh_r = st.columns([3.5, 6.5])
    with bxh_l:
        st.image(lay_anh("come_my_way.png"), use_container_width=True)
            
    with bxh_r:
        # Danh sách đã điền đầy đủ từ hạng 1 đến hạng 10
        songs = [
            {"rank": "1", "title": "Come My Way", "artist": "Nghệ sĩ"},
            {"rank": "2", "title": "Em", "artist": "Binz"},
            {"rank": "3", "title": "Nếu như ta chẳng còn", "artist": "RPT MCK"},
            {"rank": "4", "title": "IDK", "artist": "RPT MCK"},
            {"rank": "5", "title": "Nguyễn Văn Mười", "artist": "RPT MCK"},
            {"rank": "6", "title": "người còn thương em không", "artist": "Tóc Tiên"},
            {"rank": "7", "title": "LÁ NGỌC CÀNH VÀNG", "artist": "Kiều Anh"},
            {"rank": "8", "title": "Có công mài “sắc” Afrobeats", "artist": "Ngô Lan Hương"},
            {"rank": "9", "title": "Tây Thi, "artist": "RPT MCK"},
            {"rank": "10", "title": "toidaidot", "artist": "GREY D"}
        ]
        for s in songs:
            sl, sr = st.columns([8, 2])
            if s['rank'] == "1":
                sl.write(f"**{s['rank']}. {s['title']}**")
                sr.write(f"**{s['artist']}**")
            else:
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
