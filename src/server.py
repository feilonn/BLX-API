from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import criar_bd
from src.routers import routers_produtos, routers_pedidos, routers_auth

#uvicorn src.server:app --reload --reload-dir=src
#fastapi\Scripts\activate

criar_bd()

app = FastAPI()

#CORS
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

#Router - PRODUTOS
app.include_router(routers_produtos.router)

#Router - SECURITY USER
app.include_router(routers_auth.router)

#Router - PEDIDOS
app.include_router(routers_pedidos.router)