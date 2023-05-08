import os

import gradio as gr
import openai

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "##"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today? "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history

def clear(chatbot,message):
                chatbot=""
                message=""
                return chatbot,message
"""def moud(block):
    block(css=".gradio-container {background-color: red}")
    return block """
            
            


block = gr.Blocks(css="#chatb {height: 300px} footer {visibility: hidden}")  #"footer {visibility: hidden}"


with block:
    gr.Markdown("""<h1><center>ChatGPT with OpenAI API & Gradio</center></h1>
    """)
   
    with gr.Row():
        with gr.Column(scale=1,min_width=100):
            gr.Textbox(show_label=False,placeholder="New chat")
            clear1=gr.Button("Clear Conversation")
            
            Mode1=gr.Button("Light Mode")
            #Mode1.click(moud,inputs=[block], outputs=[block])
            gr.Button("OpenAi Discord")
            gr.Button("Log Out")


        with gr.Column(scale=4, min_width=600):
            chatbot = gr.Chatbot(elem_id="chatb")
           
            message = gr.Textbox(placeholder=prompt,elem_id="mass")
            state = gr.State()
                
            submit = gr.Button("SEND",elem_id="btn")
            submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])
                
            clear1.click(clear, inputs=[chatbot, message], outputs=[chatbot, message])
            
           
             
                
               
    


block.launch(debug = True,show_api=False,auth = ('user','admin'), auth_message= "Enter your username and password that you received in on Slack",)
#inf.launch(auth = ('user','admin'), auth_message= "Enter your username and password that you received in on Slack")
#auth = ('user','admin'), auth_message= "Enter your username and password that you received in on Slack",
