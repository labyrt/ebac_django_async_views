# Django Async Views

Projeto desenvolvido para o exercício de views assíncronas da EBAC. Uma
requisição GET executa uma view `async`, aguarda operações com `await`, imprime
o progresso no terminal e realiza uma chamada HTTP sem bloquear a aplicação.

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python manage.py migrate
python manage.py runserver
```

No Windows, ative o ambiente com `.venv\\Scripts\\activate`.

Acesse `http://127.0.0.1:8000/async/`. O navegador recebe uma confirmação em
JSON e o terminal exibe os números de 1 a 5 e o status da chamada ao HTTPBin.

## Testes

```bash
pytest
```
