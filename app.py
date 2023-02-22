import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plost


st.set_page_config(layout='wide',initial_sidebar_state='expanded')

# Hide hurmburger Menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style',unsafe_allow_html=True)

st.sidebar.markdown("""---""")
st.sidebar.subheader('Dashboard ')

# 1. Sidebar Menu
with st.sidebar:
    selected=option_menu(
        menu_title="Main Menu",
        options=["Dashboard","Analytics"],
        default_index=0,
    )
if selected=="Dashboard":
    #st.title(f"Welcome To {selected} Page")
    st.sidebar.markdown("""---""")
    #st.markdown("""---""")
    st.sidebar.subheader('Heat map parameter')
    time_hist_color=st.sidebar.selectbox('Color by',('temp_min','temp_max'))

    st.sidebar.subheader('Donut chart parameter')
    donut_theta=st.sidebar.selectbox('Select data',('q2','q3'))

    st.sidebar.subheader('Line chart parameter')
    plot_data=st.sidebar.multiselect('Select data',['temp_min','temp_max'],['temp_min', 'temp_max'])
    plot_height=st.sidebar.slider('Specify plot height',-200,500,250)
    
    st.sidebar.markdown("<br>",unsafe_allow_html=True)
    st.sidebar.markdown('''Created by Khulekani Matsebula''')

    #Row A
    st.markdown('### Metrics')
    col1,col2,col3 = st.columns(3)
    col1.metric("Temperature",f"{plot_height} °F",f"{plot_height} °F")
    col2.metric("Wind","9 mph","-8%")
    col3.metric("Humidity","86%","4%")

    # Row B
    seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
    stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')
    
    c1,c2=st.columns((7,3))
    with c1:
        st.markdown('### Heatmap')
        plost.time_hist(
            data=seattle_weather,
            date='date',
            x_unit='week',
            y_unit='day',
            color=time_hist_color,
            aggregate='median',
            legend=None,
            height=345,
            use_container_width=True
        )
    with c2:
        st.markdown('### Donut Chart')
        plost.donut_chart(
            data=stocks,
            theta=donut_theta,
            color='company',
            legend='button',
            use_container_width=True
        )

else:
    st.title(f"Welcome To {selected} Page")