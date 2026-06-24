# --- BXH BÀI HÁT NỔI BẬT THÁNG NÀY ---
    st.write("## BXH bài hát nổi bật *Tháng này*")
    
    bxh_l, bxh_r = st.columns([3.5, 6.5])
    
    with bxh_l:
        # Bạn nhớ đổi tên file ảnh bìa bài hát Come My Way thành "BXH_bai_hat.png" nhé
        st.image("BXH_bai_hat.png", use_container_width=True)
            
    with bxh_r:
        # Tiêu đề bảng xếp hạng
        cols_header = st.columns([1, 6, 3])
        cols_header[0].write("**#**")
        cols_header[1].write("**Tiêu đề**")
        cols_header[2].write("**Nghệ sĩ**")
        st.markdown("<hr style='margin: 5px 0px;'/>", unsafe_allow_html=True) # Chỉ dùng đường kẻ mảnh

        # Danh sách từ số 2 đến số 10 chuẩn 100% theo ảnh Figma của Huy
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
            # Tạo các cột để đẩy nội dung thẳng hàng dọc
            row_cols = st.columns([1, 6, 3])
            
            # Viết chữ trực tiếp vào cột, không dùng thêm st.write phụ để tránh bị nhảy dòng tạo khoảng trống
            row_cols[0].markdown(f"<p style='margin:0; padding:5px 0;'>{s['rank']}</p>", unsafe_allow_html=True)
            row_cols[1].markdown(f"<p style='margin:0; padding:5px 0;'><b>{s['title']}</b></p>", unsafe_allow_html=True)
            row_cols[2].markdown(f"<p style='margin:0; padding:5px 0; color: #aaa;'>{s['artist']}</p>", unsafe_allow_html=True)
            
            # Đường gạch ngang mỏng phân cách khít rịt giữa các bài hát
            st.markdown("<hr style='margin: 0px; border-top: 1px solid #222;'/>", unsafe_allow_html=True)
