import streamlit as st
from scrape import scrape_website, extract_cleaned_body_content, get_chunks
from parse import parse_with_ollama


st.title("AI WebScrapper")
url= st.text_input('Enter a Website URL: ')


if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    body_content = extract_cleaned_body_content(result)
    
    st.session_state.contents = body_content
    
    with st.expander('View Page Content'):
        st.text_area('Page Content', body_content, height=300)
        
if 'contents' in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")
    
    if st.button('Parse Content'):
        if parse_description:
            st.write('Parsing the content...')
            
            chunks_= get_chunks(st.session_state.contents)
            results = parse_with_ollama(chunks=chunks_, parse_description=parse_description)
            st.write(result)