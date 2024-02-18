from dependencies import *
import nonveg
st.set_page_config(page_title="SRM-Goodfoods", page_icon="🍔", layout="wide")

option = option_menu(
                menu_title=None,
                options=["Home", "Snacks", "Vegetarian", "Non-Vegetarian"],
                orientation="horizontal",
                icons=["house", "egg", "tree", "egg-fried"],
                default_index=0,
            )

if option == "Non-Vegetarian":
    nonveg.app()

if option == "Vegetarian":
    pass
    # nonveg.app()

if option == "Snacks":
    pass
    # nonveg.app()

if option == "Home":
    custom_title("k", 40, "#253d44", "<br><br><br>Order your food in canteen using this web-application")
    # nonveg.app()


with st.sidebar:

    # with st.empty():
    custom_title("s", 35,"black", "Cart 🛒", "center")
    c1, c2 = st.columns([3, 1])
    # skip_count = 0
    for i in st.session_state:

        if i.startswith("button") or i.startswith("total") or st.session_state[i] == 0 and not i.startswith("___"):
            pass
        else:
            print(i)

            c1.info(i)
            c2.error(str(st.session_state[i]))
    custom_title("s", 35, "green", f"Total Items : {st.session_state['total_items']}", "center")
