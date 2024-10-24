from typing import Dict
from fastapi import FastAPI
from app.routers import routers_produtos, routers_usuarios


# Criando o App
app = FastAPI()

app.include_router(routers_produtos.router)
app.include_router(routers_usuarios.router)






MENSAGEM_HOME: str    ="Bem-vindo à API de Recomendação de Produtos"





# Iniciando o servidor

@app.get("/")
def home() -> Dict[str,str]:
    global MENSAGEM_HOME
    return {"mensagem": MENSAGEM_HOME}



