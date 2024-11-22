#!/bin/bash

# Configurações
PROJECT_DIR="/home/ubuntu/WatchList-API"   # Diretório do projeto Django
VENV_DIR="$PROJECT_DIR/venv"               # Diretório do ambiente virtual
GUNICORN_SERVICE="gunicorn"                # Nome do serviço do Gunicorn
NGINX_SERVICE="nginx"                      # Nome do serviço do Nginx

# Função para exibir uma mensagem
function print_message {
    echo "############################################################"
    echo $1
    echo "############################################################"
}

# Passo 1: Ativar o ambiente virtual
print_message "Ativando ambiente virtual..."
source $VENV_DIR/bin/activate

# Passo 2: Atualizar o código do Django (pull do repositório ou outras alterações)
print_message "Atualizando código do Django..."
# (Aqui você pode adicionar o comando para fazer pull do repositório, caso necessário)
# git pull origin main  # Descomente e configure conforme necessário

# Passo 3: Aplicar migrações no banco de dados
print_message "Aplicando migrações do banco de dados..."
python $PROJECT_DIR/manage.py makemigrations
python $PROJECT_DIR/manage.py migrate

# Passo 4: Coletar arquivos estáticos
print_message "Coletando arquivos estáticos..."
python $PROJECT_DIR/manage.py collectstatic --noinput

# Passo 5: Reiniciar o Gunicorn
print_message "Reiniciando o Gunicorn..."
sudo systemctl restart $GUNICORN_SERVICE

# Passo 6: Recarregar a configuração do Nginx
print_message "Recarregando a configuração do Nginx..."
sudo systemctl reload $NGINX_SERVICE

# Passo 7: Desativar o ambiente virtual
print_message "Desativando ambiente virtual..."
deactivate

print_message "Processo de deploy concluído com sucesso!"
