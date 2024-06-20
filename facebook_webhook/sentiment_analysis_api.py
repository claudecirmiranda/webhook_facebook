import requests
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)  # Nível de logging: INFO

def analyze_sentiment(text):
    api_url = "https://api2.nagem.com.br/api/nai/sentiment"
    headers = {
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBdXRoZW50aWNhdGlvbi1BdXRob3JpemF0aW9uIiwic3ViIjoiYWRtaW4iLCJpZCI6IjY1MjU4YjY3OWVjYmE3YjM3OGMxNzk4NSIsImV4dGVybmFsX2lkIjoiOTk5OSIsImV4cCI6MTcxODAzOTg1NX0.CwUwBB2NbHQVoPE1b1hlNEv5PoNjRwekMbzszp37984',
        'Content-Type': 'application/json'
    }
    data = {
        'key': 'doc1',
        'text': text
    }

    # Log para registrar a tentativa de chamada da API
    logging.info(f"Chamando API de análise de sentimentos com texto: {text}")

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response_json = response.json()

        # Log para registrar a resposta da API
        logging.info(f"Resposta da API de análise de sentimentos: {response_json}")

        return response_json

    except requests.exceptions.RequestException as e:
        # Log para registrar erros de conexão ou requisição
        logging.error(f"Erro ao chamar API de análise de sentimentos: {e}")
        return {'error': str(e)}

# Exemplo de uso da função analyze_sentiment
if __name__ == "__main__":
    text_to_analyze = "o produto comprado é muito ruim, nunca mais compro nessa empresa."
    result = analyze_sentiment(text_to_analyze)
    print(result)  # Exibe o resultado da análise de sentimentos
