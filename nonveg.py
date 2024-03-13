from dependencies import *


def butt_func(item):
    if 'total_items' not in st.session_state:
        st.session_state.total_items = 0

    if item not in st.session_state:
        st.session_state[item] = 0

    st.session_state.total_items += 1
    st.session_state[item] += 1

    st.sidebar.write(st.session_state[item])
    st.sidebar.write(item)


def app():

    st.markdown("""
                <style>
                .st-emotion-cache-1v0mbdj > img{
                    border-radius: 6.1%;
    
                    }
                </style>
    
                """, unsafe_allow_html=True)

    custom_title("l", 50, "#253d44", "Non-Vegetarian<br><br>")
    db = Database()
    foods = db.get_data("nonveg")

    left, c1, mid, c2, right = st.columns([1, 2, 0.25, 2, 1])
    with c1:
        for i in foods[:9]:
            with st.container(height=540, border=True):
                if i[0] not in st.session_state:
                    st.session_state[i[0]] = 0
                custom_title("l", 40, "#253d44", f"{i[0]}")
                custom_title("l", 15, "black", f"{i[1]}")

                st.image(i[2], width=400)
                st.subheader(f"Price : {i[3]} ₹")
            st.button("Add to Cart", key=f"button1_{i[0]}", type="primary", use_container_width=True,
                      on_click=lambda item=i[0]: butt_func(item))

            st.markdown("###")

    with c2:
        for i in foods[9:]:
            with st.container(height=540, border=True):
                if i[0] not in st.session_state:
                    st.session_state[i[0]] = 0
                custom_title("l", 40, "#253d44", f"{i[0]}")
                custom_title("l", 15, "black", f"{i[1]}")
                st.image(i[2], width=400)
                st.subheader(f"Price : {i[3]} ₹")
            st.button("Add to Cart", key=f"button2_{i[0]}", type="primary", use_container_width=True,
                      on_click=lambda item=i[0]: butt_func(item))
            st.markdown("###")


    # print("\n")

