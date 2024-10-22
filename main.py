from fastapi     import FastAPI
from router      import health
from database    import settings
from config      import settings
from config      import sentry
from tasks       import dda
from controllers import TokenJWT
from middlewares import auth
from fastapi.middleware.cors   import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import uvicorn
import asyncio

# Instancia a aplicação
app = FastAPI()

# Permitir todas as origens
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["GET", "POST", "OPTIONS"],allow_headers=["*"])

# Instancia as Middlewares
app.add_middleware(auth.AuthMiddleware)

# Adicona rotas no swagger
app.include_router(health.router)

# Instancia o monitamento 
sentry.start_sentry()

if __name__ == "__main__":
    # Inicia o servidor 
    uvicorn.run(app) #host="0.0.0.0"