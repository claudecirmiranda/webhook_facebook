import json
import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .sentiment_analysis_api import analyze_sentiment

@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        # Verificação do webhook
        verify_token = "YOUR_VERIFY_TOKEN"
        if request.GET.get('hub.verify_token') == verify_token:
            return HttpResponse(request.GET.get('hub.challenge'))
        else:
            return HttpResponse('Invalid verification token')

    if request.method == 'POST':
        print("CHAMANDO POST")
        data = json.loads(request.body)
        print(f"Request body: {data}")
        # Ajustando para iterar sobre a lista
        for comment in data:
            if 'comments' in comment:
                print("CHAMANDO API ANALISE SENTIMENTOS")
                handle_comment(comment)

        return JsonResponse({'status': 'ok'})

def handle_comment(comment):
    # Obtendo os valores do comentário
    message = comment.get('comments')

    # Chama a API de Análise de Sentimentos
    sentiment_response = analyze_sentiment(message)

    # Persiste ou faz qualquer outra operação com a resposta
    print(f"Comment: {message}, Sentiment: {sentiment_response}")
