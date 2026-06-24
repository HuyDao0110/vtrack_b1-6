import streamlit as st

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="V-track", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- 1. THANH ĐIỀU HƯỚNG MỎNG GỌN ---
nav = st.columns([0.6, 0.4, 4.0, 0.4, 1.1, 1.1])

with nav[0]:
    st.image("logo.png", width=50)
with nav[1]:
    if st.button("⌂", use_container_width=True): st.session_state.page = "Home"
with nav[2]:
    st.text_input("Tìm kiếm...", label_visibility="collapsed")
with nav[3]:
    if st.button("☆", use_container_width=True): st.session_state.page = "Thư viện"
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
        (" ", "A1.png"), (" ", "A2.png"), 
        (" ", "A3.png"), (" ", "A4.png"), 
        (" ", "A5.png")
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

    # --- BXH NHẠC SĨ, NGHỆ SĨ TUẦN NÀY ---
    st.write("## BXH Nhạc sĩ, Nghệ sĩ *Tuần này*")
    st.image("BXH_nhac_si_nghe_si.png", use_container_width=True)
    # --- BXH BÀI HÁT NỔI BẬT THÁNG NÀY ---
    st.write("## BXH bài hát nổi bật *Tháng này*")
    
    # Tăng tỉ trọng cột trái (ảnh) lên 4.5 thay vì 3.5
    bxh_l, bxh_r = st.columns([4.8, 5.2])

    with bxh_l:
        # Ảnh sẽ tự động giãn ra để lấp đầy không gian cột mới
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
        
        for s in songs:
            # Chia cột để căn lề trái và phải
            col1, col2 = st.columns([0.7, 0.3])
            with col1:
                st.write(f"{s['rank']}. {s['title']}")
            with col2:
                # Dùng markdown để căn lề phải cho nghệ sĩ
                st.markdown(f"<p style='text-align: right; margin: 0;'>{s['artist']}</p>", unsafe_allow_html=True)
            
            # Đường kẻ ngang với margin bằng 0 để thu hẹp khoảng cách
            st.markdown("<hr style='margin: 5px 0px;'>", unsafe_allow_html=True)

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

elif st.session_state.page == "Đăng nhập":
    # Chia trang thành 3 cột: [1 phần trái, 2 phần giữa, 1 phần phải]
    col_left, col_center, col_right = st.columns([1, 2, 1])
    
    # Đặt họa tiết vào cột bên trái
    with col_left:
        st.image("left_pattern.png", use_container_width=True)
    
    # Form chính nằm ở cột giữa
    with col_center:
        st.write("# Chào mừng bạn quay trở lại")
        
        st.text_input("Tên tài khoản (Username)", placeholder="Nhập tên tài khoản")
        st.text_input("Mật khẩu (Password)", type="password", placeholder="Nhập mật khẩu")
        
        # Form đăng nhập cần các key riêng biệt để tránh lỗi DuplicateElementId
        c1, c2 = st.columns(2)
        if c1.button("Đăng nhập", use_container_width=True, key="login_submit_final"):
            st.success("Đang xử lý...")
        if c2.button("Đăng ký", use_container_width=True, key="reg_submit_final"):
            st.session_state.page = "Đăng ký"
            
    # Đặt họa tiết vào cột bên phải
    with col_right:
        st.image("right_pattern.png", use_container_width=True)

elif st.session_state.page == "Đăng ký":
    # Chia trang thành 3 cột để giữ bố cục thống nhất với trang Đăng nhập
    col_left, col_center, col_right = st.columns([1, 2, 1])
    
    with col_left:
        st.image("left_pattern.png", use_container_width=True)
    
    with col_center:
        st.write("# Đăng ký để bắt đầu")
        
        st.text_input("Tên tài khoản (Username)", placeholder="Nhập tên tài khoản")
        st.text_input("Địa chỉ email (Email address)", placeholder="Nhập địa chỉ email")
        
        # Chia cột nhỏ cho mật khẩu để gọn gàng hơn
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Mật khẩu", type="password", placeholder="Mật khẩu")
        with c2:
            st.text_input("Xác thực lại mật khẩu", type="password", placeholder="Nhập lại mật khẩu")
        
        # Nút hành động với key riêng biệt để tránh xung đột
        sub_c1, sub_c2 = st.columns(2)
        if sub_c1.button("Đăng ký", use_container_width=True, key="reg_submit_final_page"):
            st.success("Đang tạo tài khoản...")
        if sub_c2.button("Đăng nhập", use_container_width=True, key="login_nav_from_reg"):
            st.session_state.page = "Đăng nhập"
            
    with col_right:
        st.image("right_pattern.png", use_container_width=True)
