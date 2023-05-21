import streamlit as st


st.markdown("<h1><span style='color: red;'>CHÀO MỪNG THẦY ĐÃ ĐẾN VỚI PROJECT CUỐI KỲ MÔN HỌC MÁY  CỦA CHÚNG EM</span></h1>", unsafe_allow_html=True)

#thiet lap thong tin tieu de 
st.sidebar.title(" LÊ ANH DUY - 19146167  và Đặng Hữu Hiếu - 20146464")
#thiết lập hình nền bên trái cho sidebar 
st.sidebar.markdown(
	f"""
	 <style>
	 [data-testid="stSidebar"] > div:first-child {{
         background-image: url(https://images.unsplash.com/photo-1682547095741-b147eccfc848?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60)



	 }}
	 </style>
	 """,
	 unsafe_allow_html=True
) 

#thiết lập background bên phải cho web
st.markdown(
	f'''<style>
	.stApp{{
         background-image: url(https://images.unsplash.com/photo-1661956602153-23384936a1d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHw2fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60)
         


	 }}
	 </style>''',
	 unsafe_allow_html=True
)
