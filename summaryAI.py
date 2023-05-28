import openai
import streamlit as st
import os
import PyPDF2

openai.api_key = st.secrets["pass"]


def main():
    st.title("TEXT EXTRACTION AND SUMMARIZATION")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf"])
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        st.write("File uploaded successfully")

        def extract_text(file_contents):
            file_extension = os.path.splitext(uploaded_file.name)[1]
            if file_extension == ".pdf":
                return extract_text_from_pdf(file_contents)

    else:
        return "Unsupported file format."

    def extract_text_from_pdf(file_contents):
        pdf_reader = PyPDF2.PdfFileReader(file_contents)
        num_pages = pdf_reader.numPages
        text = ""
        for page in range(num_pages):
            page_obj = pdf_reader.getPage(page)
            text += page_obj.extract_text()
            return text
        st.write("**Extracted Text:**")
        st.write(extract_text(file_contents))

        def generate_summary(file_contents):
            response = openai.Completion.create(
                engine="davinci",
                prompt=text,
                max_tokens=100,  # Adjust the summary length as per your requirement
                temperature=0.5,
                n=1,
                stop=None,
            )
            summary = response.choices[0].text.strip()
            return summary

        st.write("**Summary:**")
        st.write(generate_summary(uploaded_file))
        if __name__ == "__main__":
            main()
