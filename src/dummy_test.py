from chatbot import llama3_qa
from data_extractor import data_stealer
from prompts import system_p, stealer_sys_p

prompts = [
        "Hi, my name is John Doe, and I want to start investing for retirement. I’m 32 years old.",
        "I currently have $15,000 in a savings account and $5,000 in my emergency fund.",
        "I’m interested in low-risk investments, like government bonds, but I’m open to some moderate-risk ETFs.",
        "I have a 401(k) through my employer, but I’m thinking of opening a Roth IRA as well.",
        "My annual income is $85,000, and I have no major liabilities besides my student loan of $10,000.",
        "I’d like to invest in tech stocks for long-term growth, but I’m worried about market volatility.",
        "I also want to know if I should keep some money in a high-yield savings account or invest everything.",
        "Can you suggest an investment allocation between stocks, bonds, and ETFs that fits my risk profile?",
        "I occasionally get cash gifts from my family, around $2,000 per year—should I invest that as well?",
        "Finally, can you give me a step-by-step plan to grow my retirement fund over the next 20 years?"
    ]

conversation_history = []
extracted_data_list = []

for prompt in prompts:
    print(f"You: {prompt}")
    conversation_history.append({"role": "user", "content": prompt})
    answer = llama3_qa(prompt, system_prompt=system_p)
    print(f"Bot: {answer}\n")
    extracted_data = data_stealer(conversation_history, system_prompt=stealer_sys_p)
    extracted_data_list.append(str(extracted_data))

# Summarize
import ollama
data_string = "\n".join(extracted_data_list)
summary_prompt = f"""
You are an expert financial assistant. Summarize the following extracted information
from a single user in a clear, organized, and readable way. Include all relevant personal,
financial, and investment details. Combine overlapping information and highlight key points.

Data to summarize:
{data_string}
"""
final_summary = ollama.chat(model="llama3", messages=[{"role": "system", "content": summary_prompt}])
print("\n=== Final User Summary ===\n")
print(final_summary['message']['content'])
