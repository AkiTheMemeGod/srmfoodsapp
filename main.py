from dependencies import *
import nonveg
st.set_page_config(page_title="SRM-Goodfoods", page_icon="🍔", layout="wide")



option = option_menu(
                menu_title=None,
                options=["Home", "Snacks", "Vegetarian", "Non-Vegetarian"],
                orientation="horizontal",
                icons=["house","egg", "tree", "egg-fried"],
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
    st.session_state
