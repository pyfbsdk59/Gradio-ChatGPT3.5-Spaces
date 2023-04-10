import gradio as gr
import os, openai


conversation = []

class ChatGPT:  
    

    def __init__(self):
        self.api_key = ""
        self.messages = conversation
        self.model = os.getenv("OPENAI_MODEL", default = "gpt-3.5-turbo")

    def save_api_key(self, user_input0):
        self.api_key = user_input0

    def get_response(self, user_input):
        openai.api_key = self.api_key
        conversation.append({"role": "user", "content": user_input})
        

        response = openai.ChatCompletion.create(
	            model=self.model,
                messages = self.messages

                )

        conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        
        print("AI回答內容：")        
        print(response['choices'][0]['message']['content'].strip())


        
        return response['choices'][0]['message']['content'].strip()


chatgpt = ChatGPT()


def greet(prompt, api_key):
    chatgpt.save_api_key(api_key)
    
    reply_text = chatgpt.get_response(prompt)

    greeting = f"{reply_text}"

    return greeting

demo = gr.Interface(
    fn=greet,
    inputs=["text", "text"],
    outputs=["text"],
)

demo.launch()











