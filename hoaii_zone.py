# # streamlit run hoaii_zone.py
# # cd /Users/09987q/Downloads

import streamlit as st

st.set_page_config(
    page_title="This is Hoaii_Zone",
    page_icon="👋",
)

st.write('# Welcome to Hoaii_Zone 👋👋')

st.sidebar.success("选择一个demo😊")

st.markdown(
    """
    
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    
    ### Want to learn more?
    -  ###### Check out [streamlit.io](https://streamlit.io)
    -  ###### Jump into our [documentation](https://docs.streamlit.io)
    
    ### About ME 
    - ###### work | TNU
    - ###### study | python 
"""
)


