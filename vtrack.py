import streamlit as st

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="V-track - Ứng dụng nghe nhạc", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- 1. THANH ĐIỀU HƯỚNG ---
nav = st.columns([1.5, 5, 2, 2])

with nav[0]:
    st.image("logo.png", width=90)

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
    st.image("best_notification.png", use_container_width=True)

    # --- NGHỆ SĨ PHỔ BIẾN ---
    st.write("## Nghệ sĩ phổ biến")
    art_cols = st.columns(5)
    artists = [
        ("Sơn Tùng M-TP", "A1.jpg"),
        ("SOOBIN", "A2.jpg"),
        ("bùi trường linh", "A3.png"),
        ("Trang Pháp", "A4.jpg"),
        ("Xem thêm", "A5.jpg")
    ]
    for i, (name, file_name) in enumerate(artists):
        with art_cols[i]:
            st.image(file_name, caption=name, use_container_width=True)

    # --- ALBUM NỔI BẬT ---
    st.write("## Album nổi bật")
    alb_cols = st.columns(6)
    albums = ["B1.jpg", "B2.jpg", "B3.jpg", "B4.jpg", "B5.jpg", "B6.jpg"]
    for i, file_name in enumerate(albums):
        with alb_cols[i]:
            st.image(file_name, use_container_width=True)

    # --- BXH BÀI HÁT NỔI BẬT THÁNG NÀY ---
    st.write("## BXH bài hát nổi bật *Tháng này*")
    bxh_l, bxh_r = st.columns([3.5, 6.5])
    
    with bxh_l:
        st.image("come_my_way.png", use_container_width=True)
            
   with bxh_r:
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
        
        # Tạo một container bật tính năng giảm khoảng cách tối đa
        with st.container():
            for s in songs:
                # Dùng đúng hàm st.columns thuần túy để chia hai bên trái/phải
                sl, sr = st.columns([8, 2])
                
                # Mẹo: Đưa \n--- trực tiếp vào cuối text để ép đường kẻ sát chân chữ mà không bị lỗi layout
                sl.write(f"{s['rank']}. {s['title']}\n\n---")
                sr.write(f"<p style='text-align: right; margin: 0; font-weight: bold;'>{s['artist']}</p>\n\n---", unsafe_allow_html=True)

elif st.session_state.page == "Nghệ sĩ":
    if st.button("⬅ Quay lại"): st.session_state.page = "Home"
    st.write("---")
    l, r = st.columns([4, 6])
    with l:
        st.image("A4.jpg", use_container_width=True)
    with r:
        st.write("# Trang Pháp và hành trình")
        st.write("▶ Phát tất cả | 7 bài hát")

elif st.session_state.page == "Thư viện":
    st.image("thu_vien_yeu_thich.png", use_container_width=True)
    if st.button("Trở về"): st.session_state.page = "Home"
