import streamlit as st
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title="Futuristic LMS", layout="wide")

    # Custom CSS for a futuristic look
    st.markdown("""
    <style>
    .main {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .stButton>button {
        color: #00FFFF;
        border-color: #00FFFF;
        background-color: transparent;
    }
    .stTextInput>div>div>input {
        color: #00FFFF;
        background-color: #2D2D2D;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar for navigation
    with st.sidebar:
        selected = option_menu(
            menu_title="Navigation",
            options=["Dashboard", "Courses", "Assignments", "Grades", "Messages"],
            icons=["house", "book", "clipboard", "graph-up", "envelope"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": "#2D2D2D"},
                "icon": {"color": "#00FFFF", "font-size": "25px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#3D3D3D"},
                "nav-link-selected": {"background-color": "#3D3D3D"},
            }
        )

    # Main content area
    if selected == "Dashboard":
        st.title("Welcome to Your Futuristic LMS")
        st.write("This is your personalized dashboard. Here you can see an overview of your courses, upcoming assignments, and recent grades.")

    elif selected == "Courses":
        st.title("Your Courses")
        st.write("Here you can view and manage your enrolled courses.")

    elif selected == "Assignments":
        st.title("Assignments")
        st.write("View your upcoming and past assignments here.")

    elif selected == "Grades":
        st.title("Grades")
        st.write("Check your grades and academic progress in this section.")

    elif selected == "Messages":
        st.title("Messages")
        st.write("Communicate with your instructors and peers in this messaging center.")

if __name__ == "__main__":
    main()
