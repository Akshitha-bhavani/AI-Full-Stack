import ollama 
import streamlit as st
st.title(":rainbow[My ChatBot!!!🤖]")
with st.sidebar:
    personalities = {
        "Kid" : "Give the answers ike you are explaining to a 5 year old kid. Give answer in 2 lines only",
        "Professor" : "You are an IIT professor, Explain the topics using correct terminology. Give answers in 2 lines only.",
        "Majored in CSE" : "Tou are majored in CSE, Explain the topics as in the mentioned level. Give answers in 2 lines only."
    }
    personality = st.selectbox("Select a personality", personalities.keys())
    if st.button("Clear Chat"):
        st.session_state.messages=[]
        st.success("Chat cleared successfully..")
    st.header("ChatBot Settings")
    uploaded_file = st.file_uploader("Upload a file...")
    if uploaded_file:
        st.success("File uploaded sucessfully")
        with st.expander("Preview"):
            context = uploaded_file.read().decode("utf-8")
            st.text(context)

if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("What's on your mind 🤔: ")
if question:
    with st.chat_message("user"):
        st.write("User: ",question)
    st.session_state.messages.append(
        {"role": "user",
         "content": question}
    )
    with st.spinner("Thinking..."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages = [{
                "role" : "system", "content" : personalities[personality]
            }]+st.session_state.messages
        )
    st.session_state.messages.append({
        "role":"assistant",
        "content":response["message"]["content"]
    })
    with st.chat_message("assistant"):
        st.write("AI:",response["message"]["content"])
#st.snow()