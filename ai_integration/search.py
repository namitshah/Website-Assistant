import json
from openai import OpenAI

client = OpenAI()

def load_system_prompt():
    with open("ai_integration/prompt.txt", "r", encoding="utf-8") as f:
        return f.read()

SYSTEM_PROMPT = load_system_prompt()

def search(input_url: str, input_context: str, candidate_pages: list):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Initial URL:\n{input_url}"},
        {"role": "user", "content": f"User request:\n{input_context}"},
        {
            "role": "user",
            "content": "Candidate pages:\n" + json.dumps(candidate_pages, ensure_ascii=False)
        },
    ]

    resp = client.responses.create(
        model="gpt-5-mini",
        input=messages,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "search_result",
                "schema": {
                    "type": "object",
                    "properties": {
                        "output_url": {"type": "string"},
                        "process_summary": {"type": "string"},
                        "results_summary": {"type": "string"}
                    },
                    "required": [
                        "output_url",
                        "process_summary",
                        "results_summary"
                    ],
                    "additionalProperties": False,
                }
            }
        },
        temperature=0.2
    )

    result_json = resp.output[0].content[0].text
    data = json.loads(result_json)

    return data["output_url"], data["process_summary"], data["results_summary"]

