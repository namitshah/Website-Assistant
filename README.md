Website-Assistant Repository (HCI Project).
Preparation and Deployment Steps:
1) Generate a fresh python virtual environment from the requirements.txt file
    (using Pip), and install all the dependencies (django, openai, etc)
2) Add the API key and directory path to core/views.py.
3) Execute: 'python manage.py runserver' to start the Django Server Instance.
4) Navigate to 'http://localhost:8000/main/'.

**Changes Made in the Last Commit:
1) Modified the HTML/CSS code - reorganized the UI and added buttons for rendering, sending, etc, along with some JS methods.
2) Rewrote the Prompt and modified the OpenAI Integration part (search() method).
The format for client.responses.create() has changed in late-2025. Added the tools option for web searches.
3) Created a new Django application and integrated the stuff together.