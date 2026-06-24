import streamlit as st

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="VTrack", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- 1. THANH ĐIỀU HƯỚNG MỎNG GỌN ---
nav = st.columns([0.6, 5.0, 1.1, 1.1, 1.1, 1.1])

with nav[0]:
    st.image("logo.png", width=50)

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
    st.image("best_notification.png", use_container_width=True)

    # --- NGHỆ SĨ PHỔ BIẾN ---
    st.write("## Nghệ sĩ phổ biến")
    art_cols = st.columns(5)
    artists = [
        ("Sơn Tùng M-TP", "A1.png"), ("SOOBIN", "A2.png"), 
        ("bùi trường linh", "A3.png"), ("Trang Pháp", "A4.png"), 
        ("Xem thêm", "A5.png")
    ]
    for i, (name, file_name) in enumerate(artists):
        with art_cols[i]:
            st.image(file_name, caption=name, use_container_width=True)

    # --- ALBUM NỔI BẬT ---
    st.write("## Album nổi bật")
    alb_cols = st.columns(6)
    albums = ["B1.png", "B2.png", "B3.png", "B4.png", "B5.png", "B6.png"]
    for i, file_name in enumerate(albums):
        with alb_cols[i]:
            st.image(file_name, use_container_width=True)

    # --- BXH BÀI HÁT NỔI BẬT THÁNG NÀY ---
    st.write("## BXH bài hát nổi bật *Tháng này*")
    
    bxh_l, bxh_r = st.columns([3.5, 6.5])
    
    with bxh_l:
        # Ảnh bìa lớn hiển thị bài hát #1 Come My Way
        st.image("BXH_nhac_si_nghe_si.png", use_container_width=True)
            
    with bxh_r:
        # Danh sách từ số 2 đến số 10 chuẩn xác theo ảnh của bạn
        songs = [
            {"rank": "2", "title": "Em", "artist": "Binz"},
            {"rank": "3", "title": "Nếu như ta chẳng còn", "artist": "RPT MCK"},
            {"rank": "4", "title": "IDK", "artist": "RPT MCK"},
            {"rank": "5", "title": "Nguyễn Văn Mười", "artist": "RPT MCK"},
            {"rank": "6", "title": "người còn thương em không", "artist": "Tóc Tiên"},
            {"rank": "7", "title": "LÁ NGỌC CÀNH VÀNG", "artist": "Kiều Anh"},
            {"rank": "8", "title": "Có công mài “sắc” Afrobeats", "artist": "Ngô Lan Hương"},
            {"rank": "9", "title": "Tây Thi", "artist": "RPT MCK"},
            {"rank": "10", "title": "toidaidot", "artist": "GREY D"}
        ]
        
        for s in songs:
            # Chia cột thẳng hàng dọc: Số thứ tự | Tên bài hát | Ca sĩ
            row_cols = st.columns([1, 6, 3])
            
            row_cols[0].write(s['rank'])
            row_cols[1].write(s['title'])
            row_cols[2].write(s['artist'])
            
            # Đường kẻ ngang mỏng phân tách giữa các bài hát
            st.write("---")

elif st.session_state.page == "Nghệ sĩ":
    if st.button("⬅ Quay lại"): st.session_state.page = "Home"
    st.write("---")
    l, r = st.columns([4, 6])
    with l: st.image("trang_phap.png", use_container_width=True)
    with r:
        st.write("# Trang Pháp và hành trình")
        st.write("▶ Phát tất cả | 7 bài hát")

elif st.session_state.page == "Thư viện":
    st.image("thu_vien_yeu_thich.png", use_container_width=True)
