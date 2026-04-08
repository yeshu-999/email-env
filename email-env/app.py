import gradio as gr
from inference import run_inference

def process_email(text):
    result = run_inference(text)
    return result

demo = gr.Interface(
    fn=process_email,
    inputs=gr.Textbox(lines=6, label="📧 Enter Email"),
    outputs=gr.Textbox(label="📊 Analysis Result"),
    title="🚀 AI Email Analyzer",
    description="Spam Detection | Email Scoring | AI Reply Generator"
)

demo.launch()