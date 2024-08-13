import streamlit as st
import os
import numpy as np
import pandas as pd

#Configeration
st.set_page_config(
   page_title="NameSpin Cool App",
   page_icon="🎲",
   layout="wide",
)

current_dir = os.path.dirname(os.path.abspath(__file__))

indian_celebs_path = os.path.join(current_dir, "Data Files", "Indian_Celbs.csv")
international_celebs_path = os.path.join(current_dir, "Data Files", "International_Celbs.csv")
cartoon_char_path = os.path.join(current_dir, "Data Files", "Cartoon_Characters.csv")

Indian_Celebs_df = pd.read_csv(r"Data Files\Indian_Celbs.csv")
International_Celebs_df = pd.read_csv(r"Data Files\International_Celebs.csv")
Cartoon_Char_df = pd.read_csv(r"Data Files\Cartoon_Characters.csv")

# Streamlit Code
st.write("---")
st.header("NameSpin: Spin the Wheel of Fame")
st.write("---")

st.write(" ")
Operation_choice = st.radio(label="Choose which operation you want to perform:", options= ["Get Random Celebrity Names", "View Available Celebrities"], horizontal=True, index=None)

st.write("---")

if Operation_choice:
    if Operation_choice == "Get Random Celebrity Names":
        with st.form("get_random_names"):
            col1, col2, col3 = st.columns(3)

            with col1:
                no_ind_celebs = int(st.number_input("Select Number for Indian Celebrities", 0, len(Indian_Celebs_df), step=1, value=0))
            with col2:
                no_int_celebs = int(st.number_input("Select Number for Iternational Celebrities", 0, len(International_Celebs_df), step=1, value=0))
            with col3:
                no_cartoon_char = int(st.number_input("Select Number for Cartoon Celebrities", 0, len(Cartoon_Char_df), step=1, value=0))

            submitted = st.form_submit_button("Submit")

        if submitted:

            Index_ind_list = list(np.random.choice(len(Indian_Celebs_df), no_ind_celebs, replace=False))
            Index_int_list = list(np.random.choice(len(International_Celebs_df), no_int_celebs, replace=False))
            Index_cartoon_list = list(np.random.choice(len(Cartoon_Char_df), no_cartoon_char, replace=False))

            final_ind_list = list(Indian_Celebs_df[Indian_Celebs_df.index.isin(Index_ind_list)].iloc[:, 0])
            final_int_list = list(International_Celebs_df[International_Celebs_df.index.isin(Index_int_list)].iloc[:, 0])
            final_cartoon_list = list(Cartoon_Char_df[Cartoon_Char_df.index.isin(Index_cartoon_list)].iloc[:, 0])
            dict_series = {
                "Indian Celebrities": pd.Series(final_ind_list),
                "International Celebrities": pd.Series(final_int_list),
                "Cartoon Characters": pd.Series(final_cartoon_list),
            }
            df_to_show = pd.DataFrame(dict_series)

            st.write(df_to_show)

    
    else:
        view_dict = {
            "Indian Celebrities":Indian_Celebs_df.iloc[:, 0],
            "International Celebrities":International_Celebs_df.iloc[:, 0],
            "Cartoon Characters": Cartoon_Char_df.iloc[:,0],
        }

        view_df = pd.DataFrame(view_dict)

        st.write(view_df)