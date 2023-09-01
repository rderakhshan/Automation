import pickle
from pathlib import Path

import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
from streamlit_extras.app_logo import add_logo  # pip install streamlit-extras

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
# st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="centered")

# --- USER AUTHENTICATION ---
names = ["Peter Parker", "Rebecca Miller"]
usernames = ["Vahid", "Roham"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days = 0)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:

    st.write("# Welcome to MoRMAT! 👋")

    # Read the svg file as a string
    with open("logo.svg", "r") as f:
        logo = f.read()

    # Add the logo to the sidebar using st.markdown and raw HTML
    st.markdown(f'<div style="text-align: center">{logo}</div>', unsafe_allow_html=True)

    st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """)



    # ---- SIDEBAR ----
    # Add the logo to the sidebar using st.markdown and raw HTML

    # st.sidebar.title(f"Welcome to the MoRMAT")
    authenticator.logout("Logout", "sidebar")

    # st.sidebar.header("Please Filter Here:")

    
    # city = st.sidebar.multiselect(
    #     "Select the City:",
    #     options=df["City"].unique(),
    #     default=df["City"].unique()
    # )

    # customer_type = st.sidebar.multiselect(
    #     "Select the Customer Type:",
    #     options=df["Customer_type"].unique(),
    #     default=df["Customer_type"].unique(),
    # )

    # gender = st.sidebar.multiselect(
    #     "Select the Gender:",
    #     options=df["Gender"].unique(),
    #     default=df["Gender"].unique()
    # )

    # df_selection = df.query(
    #     "City == @city & Customer_type ==@customer_type & Gender == @gender"
    # )

    # ---- MAINPAGE ----
    # st.title(":bar_chart: Sales Dashboard")
    # st.markdown("##")

    # TOP KPI's
    # total_sales = int(df_selection["Total"].sum())
    # average_rating = round(df_selection["Rating"].mean(), 1)
    # star_rating = ":star:" * int(round(average_rating, 0))
    # average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

    # left_column, middle_column, right_column = st.columns(3)
    # with left_column:
        # st.subheader("Total Sales:")
        # st.subheader(f"US $ {total_sales:,}")
    # with middle_column:
        # st.subheader("Average Rating:")
        # st.subheader(f"{average_rating} {star_rating}")
    # with right_column:
        # st.subheader("Average Sales Per Transaction:")
        # st.subheader(f"US $ {average_sale_by_transaction}")

    st.markdown("""---""")

    # SALES BY PRODUCT LINE [BAR CHART]
    # sales_by_product_line = (
        # df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
    # )
    # fig_product_sales = px.bar(
    #     sales_by_product_line,
    #     x="Total",
    #     y=sales_by_product_line.index,
    #     orientation="h",
    #     title="<b>Sales by Product Line</b>",
    #     color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    #     template="plotly_white",
    # )
    # fig_product_sales.update_layout(
    #     plot_bgcolor="rgba(0,0,0,0)",
    #     xaxis=(dict(showgrid=False))
    # )

    # # SALES BY HOUR [BAR CHART]
    # sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]
    # fig_hourly_sales = px.bar(
    #     sales_by_hour,
    #     x=sales_by_hour.index,
    #     y="Total",
    #     title="<b>Sales by hour</b>",
    #     color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    #     template="plotly_white",
    # )
    # fig_hourly_sales.update_layout(
    #     xaxis=dict(tickmode="linear"),
    #     plot_bgcolor="rgba(0,0,0,0)",
    #     yaxis=(dict(showgrid=False)),
    # )


    # left_column, right_column = st.columns(2)
    # left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
    # right_column.plotly_chart(fig_product_sales, use_container_width=True)


    # # ---- HIDE STREAMLIT STYLE ----
    # hide_st_style = """
    #             <style>
    #             #MainMenu {visibility: hidden;}
    #             footer {visibility: hidden;}
    #             header {visibility: hidden;}
    #             </style>
    #             """
    # st.markdown(hide_st_style, unsafe_allow_html=True)
