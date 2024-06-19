import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
template = """
     Below is an email that may be poorly worded
    your goal is to:
    - Properly format the email
    - Convert the inpput text to specified tone
    - Convert the input text to a specific Dialect

    Example of the tones:
    InFormal: We went to Barcelona for the weekend .Lots to tell you
    Formal: We went to Barcelona for the weekend .We have a lot of things to share.

    Here is the email and tone:
    EMAIL: {email}
    TONE: {tone}

    YOUR RESPONSE:
"""

prompt= PromptTemplate(
    input_variables=["email", "tone"],
    template=template,
)

def load_LLM():
    llm= OpenAI(temperature=0.5)
    return llm
llm=load_LLM()
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

def get_text():
    input_text =st.text_area(label="",placeholder="Your email.....",key="email_input" )
    return input_text

email_input = get_text()

st.markdown("Your Converted Email")

if email_input:
    prompt_with_email = prompt.format(email=email_input,tone=option_tone)
    formatted_email = llm(prompt_with_email)
    st.write(formatted_email)