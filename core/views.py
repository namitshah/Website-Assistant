from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from core.ai_integration.search import search
from openai import OpenAI
# Path to the Web-Assistant Directory.
web_assistant_path = ""
# The API Key.
OPENAI_API_KEY = ""
client = OpenAI(api_key=OPENAI_API_KEY)
@csrf_exempt
def gpt_search(request):
    with open(web_assistant_path + "src/index.html", "r") as file:
        file_http = file.read()
    url_input = request.POST.get('url', None)
    prompt_input = request.POST.get('prompt', None)
    process_output = "A description of the process."
    results_output = "An explanation of the results."
    url_output = "https://www.u-tokyo.ac.jp/en/index.html"
    if url_input is not None and prompt_input is not None and \
        len(prompt_input) > 10 and len(url_input) > 5:
        url_output, process_output, results_output \
             = search(client, url_input, prompt_input)
    if prompt_input is None:
        prompt_input = ""
    file_http = file_http.replace("#@process@#", str(process_output))
    file_http = file_http.replace("#@results@#", str(results_output))
    file_http = file_http.replace("#@prompt@#", prompt_input)
    file_http = file_http.replace("#@url@#", url_output)

    return HttpResponse(file_http)