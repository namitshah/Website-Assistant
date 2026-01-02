import json
from openai import OpenAI
import os

def load_system_prompt(web_assistant_path):
    with open(web_assistant_path + "core/ai_integration/prompt.txt", "r", encoding="utf-8") as f:
        return f.read()

web_assistant_path = "/Users/namit/Documents/ELab/MS/Website-Assistant/"
SYSTEM_PROMPT = load_system_prompt(web_assistant_path)

def search(client: OpenAI, input_url: str, input_context: str):
    resp = client.responses.create(
        model="gpt-5-mini",
        input=str(f"Prompt: {SYSTEM_PROMPT} | input_url: {input_url} | input_context: {input_context}"),
        tools=[{"type": "web_search"}]
    )
    total_tokens = resp.usage.total_tokens
    result_json = resp.output_text
    print(result_json)
    data = json.loads(result_json)
    data["process_summary"] = f"Total Tokens Used: {total_tokens}\n{data["process_summary"]}"
    return [data["output_url"], data["process_summary"], data["results_summary"]]


