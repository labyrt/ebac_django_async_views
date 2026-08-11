import asyncio

import httpx
from django.http import HttpResponse, JsonResponse


def home(request):
    """Confirma que a estrutura inicial do projeto está funcionando."""

    return HttpResponse("Django funcionando")


async def http_call_async():
    """Demonstra espera assíncrona e uma requisição HTTP não bloqueante."""

    for number in range(1, 6):
        await asyncio.sleep(1)
        print(number)

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get("https://httpbin.org/")
        print(response)

    return response


async def async_view(request):
    """Executa a demonstração assíncrona quando a rota recebe um GET."""

    response = await http_call_async()
    return JsonResponse(
        {
            "message": "View assíncrona executada com sucesso",
            "upstream_status": response.status_code,
        }
    )
