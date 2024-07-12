#Automated Web Developer
#Overview
The Automated Web Developer project leverages advanced language models and AI tools to automate the creation and modification of web pages based on user prompts. This project aims to streamline the web development process by integrating natural language processing and machine learning models to understand user requirements and generate appropriate HTML and CSS code.

Features
Natural Language Processing: Utilizes advanced NLP models to interpret user prompts and extract relevant information.
Automated Code Generation: Automatically generates HTML and CSS code based on user specifications.
Interactive User Interface: Allows users to input their prompts and receive generated web pages.
Content Modification: Provides functionality for users to modify the generated content based on feedback.
Pre-trained Models Integration: Integrates pre-trained models for Named Entity Recognition (NER) and sentence similarity to identify and replace sections in the generated code.
Web Page Preview: Enables users to preview the generated web pages directly in their browser.
Streamlit Integration: Uses Streamlit to create an interactive and user-friendly interface for prompt input and feedback.
Technology Stack
Python: The primary programming language used for the project.
Streamlit: For creating the web-based user interface.
LangChain Google Generative AI: Used for generating text based on user prompts.
DuckDuckGoSearchRun: For search functionalities.
Transformers and Sentence Transformers: For natural language processing and similarity detection.
Web Browser: For opening and previewing generated web pages.
Installation
To set up the project locally, follow these steps:

Clone the Repository:
git clone https://github.com/yourusername/AutomatedWebDeveloper.git
cd AutomatedWebDeveloper
Create a Virtual Environment:

python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
Install Dependencies:

pip install -r requirements.txt
Run the Streamlit Application:

streamlit run app.py
Usage
Enter Your Prompt: Use the provided text area to input your combined HTML and CSS development prompt.
Generate Webpage: Click the "Generate Webpage" button to create the HTML and CSS code based on your input.
Modify Content: Provide feedback to modify the generated content and see the changes in real-time.
Preview Webpage: The generated webpage will be saved and opened in your default web browser for preview.
Example Prompt
css

Create a responsive web page with a header containing a logo and navigation links, a main section with a hero image and call-to-action button, and a footer with contact information. Use a red color scheme for the primary elements.

#Contributing
We welcome contributions to the project. If you have any suggestions or improvements, feel free to create a pull request or open an issue on GitHub.

#License
This project is licensed under the MIT License. See the LICENSE file for details.
