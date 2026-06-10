# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
import gradio as gr

demo = gr.Interface(
    fn=lambda x: x,
    inputs=[gr.Textbox(label="Input")],
    outputs=[gr.Textbox(label="Output")],
    title="techisavan",
    description="Made with GrishteSync | Suryasticsai | suryasticsai@gmail.com <br> <img src='https://i.ibb.co/RGmb4FKk/1781072041102.png' width="50" height="50">"
)
demo.launch(server_name='0.0.0.0', server_port=7860)