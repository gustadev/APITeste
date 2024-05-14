from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/recebe")
def recebe(dados: dict):
    # Processa os dados recebidos (você pode adicionar sua lógica aqui)
    resultado = "Dados processados com sucesso!"
    
    # Registra o resultado no log
    print(f"Resultado: {resultado}")
    
    return {"message": resultado}