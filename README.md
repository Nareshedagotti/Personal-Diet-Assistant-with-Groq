# Personal Diet Assistant

## Overview

Welcome to the **Personal Diet Assistant** project! This is a Python-based application that helps users generate personalized diet plans tailored to their needs. Powered by **Groq API** and **Gradio**, the application allows users to input dietary goals, preferences, and restrictions to receive customized meal suggestions and tips. The app is designed to be easy to use and accessible through an interactive web interface.

## Features

- **Personalized Diet Plans**: Get nutrition advice based on user-specific goals, such as weight loss, muscle gain, or maintaining a healthy lifestyle.
- **User-friendly Interface**: The app features a Gradio interface for easy interaction with the assistant.
- **Powered by Groq API**: The assistant leverages Groq’s language model to generate accurate diet plans and advice.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7+**
- **Groq API Key**: You will need an API key from Groq to make requests to their language model.
- **Required Python Libraries**: The necessary libraries will be installed using `pip`.

### Install Dependencies

```bash
pip install gradio python-dotenv groq
```

### Setup Instructions

1. **Clone the repository**:

   Clone the project to your local machine:

   ```bash
   git clone https://github.com/Nareshedagotti/Personal-Diet-Assistant-with-Groq.git
   ```

2. **Set up the Environment Variables**:

   Create a `.env` file in the root of the project directory and add your **Groq API Key**:

   ```bash
   GROQ_API_KEY=your-groq-api-key-here
   ```

3. **Run the Application**:

   Once the environment is set up, run the Python script to launch the app:

   ```bash
   python app.py
   ```

   This will launch the Gradio app in your browser. You can follow the link in the terminal to interact with the assistant.
