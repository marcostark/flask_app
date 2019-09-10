# Revisando Flask

## Bibliotecas utilizadas
    - SQLAlchemy para ORM 
    - Flask WTF para formularios
    - Flask-Migrate e Flask-Script para migrações
    - Flask-Login, funcionalidade de login

### Criar migrações
    - python manage.py db init


## Comandos para migrações, sempre que fizer uma alteração no db
### Rodar migrações
    - python manage.py db migrate 
    
### Aplicar migração
    - python manage.py db upgrade
    

## Configurações