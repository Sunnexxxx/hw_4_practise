from django.shortcuts import render
import requests
from .models import Json


def fetch_and_save_data(request):
    Json.objects.all().delete()
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = response.json()
    for json_data in todos_data:
        Json.objects.create(
            userId=json_data['userId'],
            id=json_data['id'],
            title=json_data['title'],
            completed=json_data['completed']
        )
    json = Json.objects.all()
    context = {'json': json}
    return render(request, 'index.html', context)

