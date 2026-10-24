import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Khoa học Màu sắc", layout="wide"
)

# Trang chính: chỉ cập nhật thông tin sinh viên và logo.
thu_muc = Path(__file__).resolve().parent
col_truong, col_tieu_de, col_cong_ty = st.columns([2.4, 5.0, 1.8])

with col_truong:
    st.image(str(thu_muc / "logo_truong.png"), width=230)

with col_tieu_de:
    st.markdown("## KHOA HỌC MÀU SẮC")
    st.write("Project môn Ứng dụng MATLAB trong Công nghệ In")

with col_cong_ty:
    st.image(str(thu_muc / "logo_ict.png"), width=110)

st.divider()
st.write("### Thông tin sinh viên")
st.write("**Họ và tên:** Quách Thanh Tùng")
st.write("**Mã số sinh viên:** 23458021")
st.write("**Lớp:** 23VL58CT1")
