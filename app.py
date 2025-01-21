from groq import Groq
import os
from dotenv import load_dotenv
import gradio as gr

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# Function to generate a diet plan
def generate_diet_plan(user_input: str) -> str:
    """
    Generate a personalized diet plan based on user input using Groq.
    """
    prompt = (
        "You are a personal diet assistant. Provide a tailored diet plan based on the user's input. "
        "Be specific, actionable, and include meals, snacks, and tips if applicable. "
        "User's input: " + user_input
    )

    try:
        # Query the Groq model
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",  # Replace with the desired model
            messages=[
                {"role": "system", "content": "You are an assistant who specializes in creating personalized diet plans."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract and return the generated response
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Gradio Interface
def diet_plan_interface(user_input):
    """
    Wrapper for Gradio to handle user input and display the generated diet plan.
    """
    return generate_diet_plan(user_input)

# Define the Gradio UI
with gr.Blocks() as diet_assistant_ui:
    gr.Markdown(
        """
        # 🍎 Personal Diet Assistant
        Welcome! This assistant provides tailored diet advice based on your goals and preferences.
        Enter your details below, and get a personalized meal plan.
        """
    )

    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(
                label="Enter your goals/preferences",
                placeholder="E.g., I want to lose 2 kgs in one week. I am vegetarian.",
                lines=2,
            )
            submit_button = gr.Button("Get Diet Plan")
        with gr.Column():
            output = gr.Textbox(
                label="Your Personalized Diet Plan",
                interactive=False,
                lines=10,
            )

    # Link the button to the function
    submit_button.click(diet_plan_interface, inputs=user_input, outputs=output)

# Launch the Gradio app
if __name__ == "__main__":
    diet_assistant_ui.launch()

