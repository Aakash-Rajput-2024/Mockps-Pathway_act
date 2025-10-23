from ollama import chat
from prompts import stealer_sys_p

def data_stealer(conversation_history, system_prompt=stealer_sys_p):
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(conversation_history)
    response = chat(model="llama3", messages=messages)
    
    try:
        import json
        data = json.loads(response['message']['content'])
    except:
        data = response['message']['content']
    return data
