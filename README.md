# Django Views — estrutura base

Estrutura inicial do projeto Django utilizada como base para o exercício de
views assíncronas da EBAC.

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python manage.py migrate
python manage.py runserver
```

No Windows, ative o ambiente com `.venv\\Scripts\\activate`.

## Testes

```bash
pytest
```
