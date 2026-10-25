import streamlit as st


def footer_home():
    
    st.markdown(f"""
        <div style="display:flex; gap:6px; justify-content:center; margin-top:2 rem; items-align: center">
           <p style = "font-weight: bold; color: white;"> Created by Roshan ❤️</p> 
        </div>   
                
                """, unsafe_allow_html=True)

def footer_dashboard():
    
    st.markdown(f"""
        <div style="display:flex; gap:6px; justify-content:center; margin-top:2 rem; items-align: center">
           <p style = "font-weight: bold; color: black;"> Created by Roshan ❤️</p> 
        </div>   
                
                """, unsafe_allow_html=True)

