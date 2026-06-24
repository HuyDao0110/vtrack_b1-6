import streamlit as st

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="YTrack", layout="wide")

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
        # Bạn nhớ lưu ảnh bìa bài Come My Way tên là "BXH_bai_hat.png" trong thư mục nhé
        st.image("BXH_bai_hat.png", use_container_width=True)
            
    with bxh_r:
        # Sử dụng Markdown định dạng bảng thuần túy để tối ưu khoảng cách khít nhau
        bxh_content = """
| # | Tiêu đề | Nghệ sĩ |
| :--- | :--- | :--- |
| **2** | **Em** | Binz |
| **3** | **Nếu như ta chẳng còn** | RPT MCK |
| **4** | **IDK** | RPT MCK |
| **5** | **Nguyễn Văn Mười** | RPT MCK |
| **6** | **người còn thương em không** | Tóc Tiên |
| **7** | **LÁ NGỌC CÀNH VÀNG** | Kiều Anh |
| **8** | **Có công mài “sắc” Afrobeats** | Ngô Lan Hương |
| **9** | **Tây Thi** | RPT MCK |
| **10** | **toidaidot** | GREY D |
"""
        st.markdown(bxh_content)

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
