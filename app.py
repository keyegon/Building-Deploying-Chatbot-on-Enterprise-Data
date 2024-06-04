import PyPDF2
import openai
import streamlit as st

# Set up your OpenAI API key
openai.api_key = 'sk-proj-XIPxm8TPimWEwV54XNRWT3BlbkFJ7Ejx70nYJiyI12L6rdLX'

# Function to get a response from the OpenAI API
def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

# Full function to handle user questions
def ask_question(pdf_text, question):
    # Create a prompt with the PDF text and the user's question
    prompt = f"{pdf_text}\n\nQuestion: {question}\nAnswer:"

    # Get the response from the OpenAI API
    answer = get_openai_response(prompt)
    return answer

# Load the PDF file
file_path = 'NipponIndia-Short-Term-Fund-Jan-2024.pdf'
pdf_file = open(file_path, 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from each page
pdf_text = ""
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    pdf_text += page.extract_text()

pdf_file.close()

# Streamlit app
st.title("Nippon India Short Term Fund QA System")

st.write("Ask questions about the Nippon India Short Term Fund:")

question = st.text_input("Enter your question here:")

if st.button("Get Answer"):
    if question:
        answer = ask_question(pdf_text, question)
        st.write(f"**Question:** {question}")
        st.write(f"**Answer:** {answer}")
    else:
        st.write("Please enter a question.")
