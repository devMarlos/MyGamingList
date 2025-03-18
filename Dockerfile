FROM python:3

WORKDIR /app

COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Mapear a porta antes de rodar o comando: docker run -p 8501:8501 dc-mygaminglist
CMD ["streamlit", "run", "app/main.py"] 