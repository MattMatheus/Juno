from django.shortcuts import render
from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


def index(request):
    if request.method == "POST":
        text = request.POST.get("inputText")
        print(text)
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"{text}"},
                {"role": "user", "content": f"{text}"},
            ],
        )
        # Process the response from OpenAI as needed
        return render(request, "ai/index.html", {"response": response})
    else:
        return render(request, "ai/index.html")
