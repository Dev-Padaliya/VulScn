import streamlit as st
import os

def run_webpwn(url):
    cmd = "python tool.py " + url
    output = os.popen(cmd).read()
    return output

def main():
    st.title("VulScn - Web Vulnerability Scanner")
    st.write("Enter the URL you want to scan:")
    url = st.text_input("URL")

    if st.button("Scan"):
        if url:
            st.write("Scanning URL:", url)
            output = run_webpwn(url)
            st.text_area("Scan Results", output, height=500)
        else:
            st.error("Please enter a valid URL.")

if __name__ == "__main__":
    main()
