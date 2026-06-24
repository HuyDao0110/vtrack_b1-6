import streamlit as st
from datetime import datetime

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="V-track", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- 1. THANH ĐIỀU HƯỚNG MỎNG GỌN ---
nav = st.columns([0.6, 0.3, 2.5, 0.3, 0.3, 1.1, 1.1])

with nav[0]:
    st.image("logo.png", width=50)
with nav[1]:
    if st.button("🏠", use_container_width=True): st.session_state.page = "Home"
with nav[2]:
    st.text_input("Tìm kiếm...", label_visibility="collapsed")
with nav[3]:
    if st.button("☆", use_container_width=True): st.session_state.page = "Thư viện"
with nav[4]:
    if st.button("🌐", use_container_width=True): st.session_state.page = "Ngôn ngữ"
with nav[5]:
    if st.button("Đăng nhập", use_container_width=True): st.session_state.page = "Đăng nhập"
with nav[6]:
    if st.button("Đăng ký", use_container_width=True): st.session_state.page = "Đăng ký"

st.write("---")

# --- 2. QUẢN LÝ CÁC TRANG ---
if st.session_state.page == "Home":
    now = datetime.now()
    # Định dạng theo kiểu Việt Nam: Thứ..., ngày DD/MM/YYYY
    # Lưu ý: Python mặc định trả về thứ bằng tiếng Anh, ta sẽ map sang tiếng Việt
    days = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
    day_name = days[now.weekday()]
    date_str = now.strftime(f"*{day_name}, %d-%m-%Y*")
    
    # Hiển thị lời chào
    st.markdown("## Nghe gì hôm nay, User?")
    st.write(f"#####       Hôm nay là **{date_str}**")
    if st.button("Thông tin nghệ sĩ (Xử lý phần giao diện)", use_container_width=True): st.session_state.page = "Thông tin nghệ sĩ: Trang Pháp"
    st.image("best_notification.png", use_container_width=True)

    # --- NGHỆ SĨ PHỔ BIẾN ---
    col_title, col_btn = st.columns([5, 1])
    
    with col_title:
        st.write("## Nghệ sĩ *Phổ biến*") # Ví dụ: ## Nghệ sĩ Phổ biến
    with col_btn:
        # Nút bấm không kèm logic xử lý, chỉ để hiển thị cho đẹp
        st.button("Thêm", key="btn_more_unique_id", use_container_width=True)
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
    col_title, col_btn = st.columns([5, 1])
    with col_title:
        st.write("## Album *Nổi bật*") 
    with col_btn:
        # Thay đổi key thành 'btn_more_albums' để không trùng với nghệ sĩ
        st.button("Thêm", key="btn_more_albums", use_container_width=True)
    alb_cols = st.columns(6)
    albums = ["B1.png", "B2.png", "B3.png", "B4.png", "B5.png", "B6.png"]
    for i, file_name in enumerate(albums):
        with alb_cols[i]:
            st.image(file_name, use_container_width=True)

    # --- BXH NHẠC SĨ, NGHỆ SĨ TUẦN NÀY ---
    header_col, buttons_col = st.columns([2, 1])

    with header_col:
        st.write("## BXH nhạc sĩ, nghệ sĩ *Tuần này*")
    
    with buttons_col:
        # Chia nhỏ cụm nút bên phải
        time_nav = st.columns(4)
        # Tùy chỉnh để nút nằm gọn gàng, không bị dãn rộng ra
        with time_nav[0]:
            if st.button("Ngày", key="btn_day_final"): st.session_state.time_filter = "Ngày"
        with time_nav[1]:
            if st.button("Tuần", key="btn_week_final"): st.session_state.time_filter = "Tuần"
        with time_nav[2]:
            if st.button("Tháng", key="btn_month_final"): st.session_state.time_filter = "Tháng"
        with time_nav[3]:
            if st.button("Năm", key="btn_year_final"): st.session_state.time_filter = "Năm"
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
        st.write("#  ")
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
        st.write("#  ")
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

elif st.session_state.page == "Ngôn ngữ":
    languages_list = [
        "Ả Rập", "Azerbaijan", "Bengali", "Bulgaria", "Bồ Đào Nha",
        "Czech", "Đan Mạch", "Đức", "English", "Español",
        "Estonia", "Phần Lan", "Français", "Hy Lạp", "Hungary",
        "Indonesia", "Ấn Độ", "Iceland", "Italino", "Hebrew",
        "Nhật Bản", "Hàn Quốc", "Lithuania", "Latvia", "Mã Lai",
        "Hà Lan", "Na Uy", "Ba Lan", "Romania", "Nga",
        "Thụy Điển", "Thái Lan", "Thổ Nhĩ Kỳ", "Ukraina", "Tiếng Việt",
        "Trung Quốc", "Hồng Kông"
    ]
    
    # Chia thành 5 cột
    num_cols = 5
    cols = st.columns(num_cols)
    
    # Phân bổ danh sách vào từng cột
    # Sử dụng toán tử chia lấy dư để rải đều ngôn ngữ vào các cột
    for i, lang in enumerate(languages_list):
        with cols[i % num_cols]:
            st.write(f"{lang}")

elif st.session_state.page == "Thông tin nghệ sĩ: Trang Pháp":
    # Nút quay lại
    if st.button("⬅ Quay lại"): 
        st.session_state.page = "Home"
    
    st.write("---")

    # Sử dụng container để bọc toàn bộ nội dung trang nghệ sĩ
    with st.container():
        # 1. BỐ CỤC CHÍNH (Ảnh và thông tin nghệ sĩ)
        l, r = st.columns([3, 7])
        
        with l:
            st.image("trang_phap.png", use_container_width=True)
            
        with r:
            st.markdown("# Trang Pháp và hành trình trong CHENGFENG 2026")
            
            # Đảm bảo các nút nằm gọn trên một hàng
            c_btn, c_info = st.columns([1, 3])
            with c_btn:
                st.button("▶ Phát danh sách")
            with c_info:
                st.write("7 bài hát • 24 phút 42 giây")
            
            st.write("➕ ... (Thêm/Tùy chọn)")

    # 2. DANH SÁCH BÀI HÁT (Sử dụng CSS để đường kẻ sắc nét hơn)
            st.write("---")
            songs = [
                "1. MOONLIGHT", "2. Nghệ Thuật Gia Vĩ Đại", "3. Là Anh", 
                "4. Ego-holic", "5. Nghịch Chiến", "6. Sổ Tay Rèn Luyện Thanh Xuân", "7. DNA"
            ]
            
            for song in songs:
                # Dùng markdown với h3 để font chữ cân đối với tiêu đề
                st.markdown(f"{song}")
                # Đường kẻ ngang tối màu, nằm sát dưới mỗi bài hát
                #st.markdown("<hr style='margin-top: 0.3px; margin-bottom: 0.3px; border: 0.5px solid #333;'>", unsafe_allow_html=True)

    # 3. PHẦN DƯỚI: Tiểu sử
    st.write("### Tiểu sử")
    st.write("Trang Pháp (Nguyễn Thùy Trang, sinh năm 1989) là một nữ nghệ sĩ toàn năng...")
    
    # 4. PHẦN: Có thể bạn thích
    st.write("## Có thể bạn thích")
    rec_cols = st.columns(4)
    rec_images = ["ChiPu.png", "Suni.png", "LonelyDance.png", "Next.png"]
    for i, img in enumerate(rec_images):
        rec_cols[i].image(img, use_container_width=True)

# Thêm một chút khoảng cách phía dưới
st.write("---")
