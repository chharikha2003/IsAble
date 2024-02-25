from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required

from job_portal.settings import BASE_DIR
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse
import google.generativeai as genai
import os
import environ

# Initialize environ
env = environ.Env()

# Path to your .env file
env_file = os.path.join(BASE_DIR, '.env')

# Read from .env file
environ.Env.read_env(env_file)

# Now you can access your environment variables using env
api_key = env('API_KEY')

# Add your generated API key here
genai.configure(api_key=api_key)

@login_required(login_url='login')
def ask_question(request):
    print('in the function')
    if request.method == "POST":
        text = request.POST.get("text")
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        response = chat.send_message(text)
        user = request.user
        ChatBot.objects.create(text_input=text, gemini_output=response.text, user=user)

        print(response)

        response_data = {
            "text": response.text,  # Assuming response.text contains the relevant response data
            # Add other relevant data from response if needed
        }
        return JsonResponse({"data": response_data})
    else:
        return HttpResponseRedirect(reverse("chat"))  # Redirect to chat page for GET requests

@login_required(login_url='login')
def chat(request):
    user = request.user
    chats = ChatBot.objects.filter(user=user)
    response_data = None  # Initialize response data

    # Access response data from AJAX request (if available)
    if request.method == 'POST':
        if 'text' in request.POST:
            response_data = request.POST.get('text')

    context = {'chats': chats, 'response_data': response_data}
    return render(request, "chat_bot.html", context)
