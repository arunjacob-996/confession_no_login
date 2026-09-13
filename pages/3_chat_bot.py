import streamlit as st

st.set_page_config(
    page_title="College Confession Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 College Confession Chatbot")

st.write("Click the button below to open the College Confession Chatbot.")

chatbot_url = "https://college-confession-chatbot-8xrtxp32mxmamob8gwtnd6.streamlit.app/"

st.link_button(
    "💬 Open College Confession Chatbot",
    chatbot_url,
    use_container_width=True
)