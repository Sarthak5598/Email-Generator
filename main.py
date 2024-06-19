import streamlit as st

st.set_page_config(page_title="Email Generator", page_icon=":email:")
st.header("Email Generator")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Here you can improve your mails , sound more professional ,make a better impression on your boss , Send cold mails to recruiters , Force them to get back to you")
with col2:
    st.image(image="kratos.png")

st.markdown("Enter your Email Idea")

col1, col2 = st.columns(2)

with col1:
    option_tone = st.selectbox(
        "Tone",
        ("Formal", "Informal")
    )
with col2:
    option_dialect=st.selectbox(
        'Which English dialect would you like',
        ('American English','British English')
    )

def get_text():
    input_text =st.text_area(label="",placeholder="Your email.....",key="email_input" )
    return input_text

email_input = get_text()
