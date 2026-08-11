from django.http import HttpResponse


def home(request):
    """Confirma que a estrutura inicial do projeto está funcionando."""

    return HttpResponse("Django funcionando")
