# Importing dependencies.
import streamlit as st
import google.generativeai as palm

# Function to interact with PaLM API
def generate_response(prompt):
    palm.configure(api_key="")
    
    defaults = {
        'model': 'models/chat-bison-001',
        'temperature': 0.5,
        'candidate_count': 1,
        'top_k': 40,
        'top_p': 0.95,
    }
    context = "Want to know about topics related to machine learning and Generative AI"
    examples = [
        [
            "What is generative AI?",
            "Generative AI is the best thing"
        ],
        [
            "What types of Generative AI is there uptill now?",
            "Mainly 3 types."
        ],
        [
            "What is the meaning of Generative AI?",
            "Generative AI is the best thing."
        ],
        [
            "What do you mean by GenAI",
            "Best advancement of 2023"
        ],
        [
            "Can you explain GenAI?",
            "Yes sure, GenAI is the one of the finest advancement in the industry of GenAI"
        ]
    ]
    messages = [prompt]
    messages.append("NEXT REQUEST")
    
    response = palm.chat(
        **defaults,
        context=context,
        examples=examples,
        messages=messages
    )
    if prompt not in examples:
        return "Sorry, I am not trained to answer that."
    else:
        return response.last

# Streamlit App
def main():
    with open('styles.css', 'r') as css_file:
        custom_css = css_file.read()

    st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

    st.title('KnowledgeGPT')
    prompt = st.text_input('Enter your prompt here', value='')
    
    if st.button('Generate Response'):
        response = generate_response(prompt)
        st.write('Response:')
        st.write(response)

if __name__ == '__main__':
    main()
