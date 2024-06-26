Objectives:-


Create a Chat Interface: Develop a user-friendly chat interface where users can input their system role and message, and receive a response.

Integrate with GROQ API: Utilize the GROQ API to generate responses based on user input.

Web Application: Deploy the chat interface as a web application using Streamlit.

Tools and Technologies:-

Streamlit: A Python library used for creating web applications. It provides the UI components and layout for the chat interface.

GROQ API: An external API used for generating chat responses. The project uses a specific model, llama3-70b-8192, to generate these responses.

Python: The primary programming language used to write the script.

CSS: Used for styling the chat interface, including the layout, input fields, buttons, and response display.
Detailed Breakdown

Streamlit Functions:-

st.title: Sets the title of the web application.

st.markdown: Adds custom HTML and CSS for styling.

st.container: Creates a container for grouping input fields.

st.text_input: Creates text input fields for the system role and user message.

st.button: Creates a button to submit the input and generate a response.

GROQ API Functions:-

Groq: Initializes the GROQ client using an API key.
client.chat.completions.create: Sends a message to the GROQ API and retrieves the response.
