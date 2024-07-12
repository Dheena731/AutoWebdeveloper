import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew, Process
from langchain.tools import DuckDuckGoSearchRun
import webbrowser

# Set gemini pro as llm
llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=0.5, google_api_key="***")

# Create searches
tool_search = DuckDuckGoSearchRun()

# Define Agents
manager = Agent(
    role='Project Manager',
    goal='Manage the web development project',
    backstory='Experienced in coordinating web development tasks.',
    verbose=True,
    allow_delegation=True,
    llm=llm,
    tools=[tool_search]
)

developer = Agent(
    role='Developer',
    goal='Develop the webpage based on specifications',
    backstory='An expert in web development with a focus on user-friendly interfaces.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

combined_prompt = st.text_area("Enter your combined HTML and CSS development prompt:")

combined_task = Task(
    description=f"Develop HTML and CSS content based on the user's prompt: {combined_prompt}",
    agent=developer,
    expected_output="HTML and CSS development completed successfully",
    subtasks=[
        "1. Design and implement the header section with a logo and navigation.",
        "2. Create a responsive layout for the main content area.",
        "3. Integrate a contact form in the footer for user inquiries.",
        "4. Apply the user-specified theme, such as using red as the primary color.",
        "5. Optimize the webpage for performance and load times.",
        "6. Generate CSS file based on the user's prompt and  Integrate CSS into the HTML file."
    ]
)

web_development_crew = Crew(
    agents=[manager, developer],
    tasks=[combined_task],
    verbose=True,
    process=Process.sequential
)

st.title("Web Development Task Manager")

temp_file_name = "trial_page.html"

if st.button("Generate Webpage"):
    combined_output = web_development_crew.kickoff()

    with open(temp_file_name, "w") as trial_file:
        trial_file.write(combined_output)

    st.success(f"Webpage saved to {temp_file_name}")


    st.write("Opening the trial content in the default web browser...")
    webbrowser.open(temp_file_name)

# User Feedback and Iteration
user_feedback = st.text_area("Provide feedback on the trial webpage (type 'done' when satisfied, 'modify' to provide modifications): ")

if user_feedback.lower() == 'modify':
    # Allow the user to modify the HTML and CSS content
    modified_prompt = st.text_area("Enter your modified combined HTML and CSS prompt: ")
    combined_task.description = f"Modify HTML and CSS content based on the user's prompt: {modified_prompt}"
    combined_output = web_development_crew.kickoff()

    # Save the modified content to the temporary file
    with open(temp_file_name, "w") as trial_file:
        trial_file.write(combined_output)

    st.success(f"Modified webpage saved to {temp_file_name}")

# Finalization and Deployment (if needed)
final_combined_output = combined_prompt
st.write("Crew: Finalizing Web Content")
st.code(final_combined_output)
