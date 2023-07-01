FROM python:3.9.16

# Configuração do ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação para o diretório de trabalho
COPY . .

# Expõe a porta em que o Flask irá rodar
EXPOSE 5000

# Define o comando para iniciar a aplicação Flask
CMD cd routes && ["python", "app.py"]
