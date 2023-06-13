import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
from hugchat.login import Login
import os
os.environ['CURL_CA_BUNDLE'] = ''


sign = Login('anandatul502@gmail.com', 'Atul_7535')
cookies = sign.login()
sign.saveCookies()
 

st.set_page_config(page_title="An LLM Powered Chatbot")

#Creating Visuals for Web Page
with st.sidebar:
    st.title('🤯 HugChat App')
    st.markdown('''
    This app is an LLM-powered chatbot built using:
    - [HugChat](<https://github.com/Soulter/hugging-chat-api>)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](<https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor>) LLM model


    💡 Highlight: No API key required 🥳

    ''')
    add_vertical_space(3)
    st.write('Made by: Atul Anand (<https://www.linkedin.com/in/atul-anand-356319163/) (<https://medium.com/@atulanand7535>)') 

#Creating list to store generated and past response

if 'generated' not in st.session_state:
    st.session_state['generated']=['Hi, How may I help you?']

#past stores user's ques
if 'past' not in st.session_state:
    st.session_state['past']=['Hi']

input_container=st.container()
colored_header(label='',description='',color_name='blue-30')
response_container=st.container()

def get_text():
    input_text=st.text_input("You: ","",key="input")
    return input_text

with input_container:
    user_input=get_text()


def generate_response(prompt):
    chatbot=hugchat.ChatBot(cookies=cookies.get_dict())
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    conversation_list = chatbot.get_conversation_list()
    response = chatbot.chat(prompt)
    return response

with response_container:
    if user_input:
        response=generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)


    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))
