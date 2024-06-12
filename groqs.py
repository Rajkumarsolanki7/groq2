import streamlit as st
from groq import Groq

# Initialize the GROQ client
client = Groq(api_key=("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"))

def get_chat_response(user_message):
    """
    Sends a message to the GROQ API and returns the response.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

# Streamlit UI
st.title("Personal Assistent")

# User input for system role
system_role = st.text_input("Order Me :")

# User input for user message
user_message = st.text_input("Ask :")

# Submit button
if st.button("Send"):
    # Combine system role and user message
    combined_message = f"{system_role}\n{user_message}"
    
    # Get chat response
    response = get_chat_response(combined_message)
    
    # Display the response
    st.write(f"Response: {response}")
