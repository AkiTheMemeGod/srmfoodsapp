from dependencies import *

st.set_page_config(page_title="SRM-Goodfoods", page_icon="🍔", layout="wide")

st.markdown("""
            <style>
            .st-emotion-cache-1v0mbdj > img{
                border-radius: 6.1%;

                }
            </style>

            """, unsafe_allow_html=True)

custom_title("l", 50, "#253d44", "SRM FOODS<br><br>")
db = Database()
foods = db.get_data("nonveg")
left, c1, mid, c2, right = st.columns([1, 2, 0.25, 2, 1])
with c1:
    for i in foods[:2]:
        with st.container(height=540, border=True):
            custom_title("l", 45, "#253d44", f"{i[0]}")
            st.subheader(i[1])
            st.image(i[2], width=400)
            st.header(f"Price : {i[3]}")
        st.button("Add to Cart", key=i[0], type="primary", use_container_width=True)
        st.markdown("###")

with c2:
    for i in foods[2:]:
        with st.container(height=540, border=True):
            custom_title("l", 45, "#253d44", f"{i[0]}")
            st.subheader(i[1])
            st.image(i[2], width=400)
            st.header(f"Price : {i[3]}")
        st.button("Add to Cart", key=i[0], type="primary", use_container_width=True)
        st.markdown("###")


