import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(page_title="V-track", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"

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

#home
if st.session_state.page == "Home":
    #lời chào
    now = datetime.now()
    days = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
    day_name = days[now.weekday()]
    date_str = now.strftime(f"*{day_name}, %d-%m-%Y*")
    st.markdown("## Nghe gì hôm nay, User?")
    st.write(f"#####       Hôm nay là **{date_str}**")
    st.image("best_notification.png", use_container_width=True)

    # ==================== NGHỆ SĨ PHỔ BIẾN ====================
    col_title, col_btn = st.columns([5, 1])
    
    with col_title:
        st.write("## Nghệ sĩ *Phổ biến*") 
    with col_btn:
        st.button("Thêm", key="btn_more_unique_id", use_container_width=True)
        
    art_cols = st.columns(5)
    
    artists = [
        ("Sơn Tùng M-TP", "A1.png"), 
        ("SOOBIN", "A2.png"),  
        ("bùi trường linh", "A3.png"), 
        ("Trang Pháp", "A4.png"), 
        ("Ẩn", "A5.png") # Ô ảnh mờ dần cuối cùng
    ]
    
    for i, (name, file_name) in enumerate(artists):
        with art_cols[i]:
            st.image(file_name, use_container_width=True)
            
            # Chỉ hiển thị nút "Xem chi tiết" cho 4 ô nghệ sĩ đầu tiên
            if name != "Ẩn":
                if st.button("Xem chi tiết", key=f"btn_art_{i}", use_container_width=True):
                    if name == "Trang Pháp":
                        st.session_state.page = "Thông tin nghệ sĩ: Trang Pháp"
                        st.rerun()
                    elif name == "Sơn Tùng M-TP":
                        st.session_state.page = "Thông tin nghệ sĩ: Sơn Tùng M-TP"
                        st.rerun()
                    else:
                        st.toast(f"Tính năng xem thông tin của nghệ sĩ {name} đang được phát triển!")


    # ==================== ALBUM NỔI BẬT ====================
    col_title, col_btn = st.columns([5, 1])
    with col_title:
        st.write("## Album *Nổi bật*") 
    with col_btn:
        st.button("Thêm", key="btn_more_albums", use_container_width=True)
    
    alb_cols = st.columns(6)
    
    albums = [
        "M-TP Album", "Ai Cũng Phải Bắt Đầu Từ Đâu Đó", "Album 3", "Bật Lên", "Từng Ngày Như", "Ẩn"
    ]
    alb_images = ["B1.png", "B2.png", "B3.png", "B4.png", "B5.png", "B6.png"] # B6.png là ảnh mờ
    
    for i in range(6):
        with alb_cols[i]:
            st.image(alb_images[i], use_container_width=True)
            
            # Chỉ hiện nút "Xem chi tiết" cho 5 album đầu, ô thứ 6 (ảnh mờ) sẽ bỏ qua
            if albums[i] != "Ẩn":
                if st.button("Xem chi tiết", key=f"btn_alb_{i}", use_container_width=True):
                    st.toast(f"Chứ năng mở Album '{albums[i]}' đang được phát triển!")

    #bxh nhạc nghệ sĩ
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
    #bxh bài hát
    st.write("## BXH bài hát nổi bật *Tháng này*")
    bxh_l, bxh_r = st.columns([4.8, 5.2])

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
        
        for s in songs:
            col1, col2 = st.columns([0.7, 0.3])
            with col1:
                st.write(f"{s['rank']}. {s['title']}")
            with col2:
                st.markdown(f"<p style='text-align: right; margin: 0;'>{s['artist']}</p>", unsafe_allow_html=True)
            st.markdown("<hr style='margin: 5px 0px;'>", unsafe_allow_html=True)

#thư viện
elif st.session_state.page == "Thư viện":
    st.image("thu_vien_yeu_thich.png", use_container_width=True)

#đăng nhập
elif st.session_state.page == "Đăng nhập":
    col_left, col_center, col_right = st.columns([1, 2, 1])

    with col_left:
        st.image("left_pattern.png", use_container_width=True)
    with col_center:
        st.write("#  ")
        st.write("# Chào mừng bạn quay trở lại")
        
        st.text_input("Tên tài khoản (Username)", placeholder="Nhập tên tài khoản")
        st.text_input("Mật khẩu (Password)", type="password", placeholder="Nhập mật khẩu")
        
        c1, c2 = st.columns(2)
        if c1.button("Đăng nhập", use_container_width=True, key="login_submit_final"):
            st.success("Đang xử lý...")
        if c2.button("Đăng ký", use_container_width=True, key="reg_submit_final"):
            st.session_state.page = "Đăng ký"
            
    with col_right:
        st.image("right_pattern.png", use_container_width=True)

#đăng ký
elif st.session_state.page == "Đăng ký":
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

#ngôn ngữ
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
    
    num_cols = 5
    cols = st.columns(num_cols)
    
    for i, lang in enumerate(languages_list):
        with cols[i % num_cols]:
            st.write(f"{lang}")

# nghệ sĩ Trang Pháp
elif st.session_state.page == "Thông tin nghệ sĩ: Trang Pháp":
    # Khởi tạo trạng thái phát nhạc nếu chưa có
    if "play_music" not in st.session_state:
        st.session_state.play_music = False

    # nút quay lại
    if st.button("⬅ Quay lại"): 
        st.session_state.page = "Home"
        st.rerun()
    
    st.write("---") # danh sách phát
    with st.container():
        l, r = st.columns([1, 1])
        
        with l:
            # Sửa lại width phù hợp hoặc use_container_width để ảnh không bị vỡ/quá to
            st.image("trang_phap.png", use_container_width=True)
            
        with r:
            st.markdown("# Trang Pháp và hành trình trong CHENGFENG 2026")
            c_btn, c_info = st.columns([1, 3])
            
            with c_btn:
                # Khi bấm nút sẽ kích hoạt trạng thái phát nhạc
                if st.button("▶ Phát danh sách", key="btn_play_playlist"):
                    st.session_state.play_music = True
                    st.rerun()
                    
            with c_info:
                st.write("7 bài hát • 25 phút 42 giây")

            # HIỂN THỊ THANH PHÁT NHẠC KHI ĐÃ BẤM NÚT
            if st.session_state.play_music:
                st.write("🎵 *Đang phát: Toàn bộ danh sách CHENGFENG 2026*")
                # Gọi file mp3 của bạn
                try:
                    st.audio("1tphapcf.mp3", format="audio/mp3", autoplay=True)
                except Exception as e:
                    st.error("Không tìm thấy file âm thanh 'tphapcf.mp3'. Vui lòng kiểm tra lại thư mục nguồn.")
                
                # Thêm nút nhỏ để tắt nhạc nếu muốn
                if st.button("⏹ Dừng phát", key="btn_stop_playlist"):
                    st.session_state.play_music = False
                    st.rerun()
                    
            st.write("") # Khoảng cách nhỏ

            songs = [
                "1. MOONLIGHT", "2. Nghệ Thuật Gia Vĩ Đại", "3. Là Anh", 
                "4. Ego-holic", "5. Nghịch Chiến", "6. Sổ Tay Rèn Luyện Thanh Xuân", "7. DNA"
            ]
            
            for song in songs:
                st.markdown(f"{song}")

    # tiểu sử
    st.write("### Tiểu sử")
    st.write("Trang Pháp (Nguyễn Thùy Trang, sinh năm 1989) là một nữ nghệ sĩ toàn năng của showbiz Việt, nổi bật với vai trò ca sĩ, nhạc sĩ và nhà sản xuất âm nhạc.")
    st.write("Sau một thời gian lui về hậu trường làm sản xuất, cô đã có màn tái xuất bùng nổ tại chương trình Chị Đẹp Đạp Gió Rẽ Sóng 2023. ")
    st.write("Bằng các kỹ năng âm nhạc toàn diện, cô xuất sắc giành ngôi vị Quán quân, khẳng định vị thế của một nghệ có tư duy văn minh và tầm ảnh hưởng lớn trong làng nhạc Việt hiện đại.")
    
    # đề xuất
    st.write("## Có thể bạn thích")
    c1, c2, c3, c4 = st.columns([1, 1, 2, 1])
    rec_images = ["C1.png", "C2.png", "C3.png", "C4.png"]
    
    cols = [c1, c2, c3, c4]
    
    for i, col in enumerate(cols):
        with col:
            st.image(rec_images[i], use_container_width=True)
            st.markdown(f"<div style='text-align: center; margin-top: -10px;'></div>", unsafe_allow_html=True)

# nghệ sĩ Sơn Tùng M-TP
elif st.session_state.page == "Thông tin nghệ sĩ: Sơn Tùng M-TP":
    # Nút quay lại
    if st.button("◀ Back", key="btn_back_sontung"): 
        st.session_state.page = "Home"
        st.rerun()
    
    st.write("---")
    
    # Chia 2 cột tỷ lệ đẹp cho giao diện
    col_img, col_info = st.columns([1, 1.2])
    
    with col_img:
        # Ảnh Sơn Tùng M-TP chính
        st.image("A1.png", use_container_width=True) 
        
    with col_info:
        st.markdown("# Sơn Tùng M-TP cùng màn Comeback với COME MY WAY")
        st.write("") 
        
        # MẸO: Dùng ảnh chụp MV (hoặc ảnh thumbnail) làm mock video
        # Bạn thay "come_my_way.png" hoặc "A1.png" bằng ảnh thumbnail MV của bạn
        st.image("comemyway.png", use_container_width=True)
        
        # Link dẫn trực tiếp tới video YouTube thực tế khi click
        st.markdown(
            "🔗 **Xem video trên Youtube:** [https://www.youtube.com/watch?v=SIQR9iu09bQ](https://www.youtube.com/watch?v=SIQR9iu09bQ)"
        )

    st.write("---")
    
    # Phần bài viết mô tả bên dưới
    st.markdown(
        """
        > *"Come My Way" đánh dấu màn tái xuất bùng nổ của Sơn Tùng M-TP qua sự kết hợp cùng rapper Tyga. 
        Thể hiện hoàn toàn bằng tiếng Anh, bài hát mang giai điệu Hip-hop/Pop hiện đại kết hợp cùng MV độc đáo, 
        lồng ghép tinh tế văn hóa Việt Nam vào nền nghệ thuật thị giác đương đại.*
        """
    )

st.write("---")
