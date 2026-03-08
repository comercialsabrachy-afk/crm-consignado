# CRM Consignado

Sistema CRM em Django para gestão de clientes, oportunidades, tratativas e importação de listas em Excel.

## Funcionalidades
- Cadastro de clientes
- Cadastro de telefones
- Kanban de oportunidades
- Tratativas de atendimento
- Importação de Excel

## Tecnologias
- Python
- Django
- Bootstrap

## Como rodar
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver