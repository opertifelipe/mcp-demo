from fastapi import FastAPI, Request, HTTPException
from mcp.server.fastmcp import FastMCP

# Token statico predefinito
VALID_TOKEN = "12345"

app = FastAPI()
mcp = FastMCP("MCP Server con Autenticazione")

# Middleware per l'autenticazione
@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != f"Bearer {VALID_TOKEN}":
        raise HTTPException(status_code=401, detail="Token non valido o mancante")
    response = await call_next(request)
    return response

# Monta l'applicazione MCP
app.mount("/", mcp.sse_app())

# Definisci uno strumento MCP
@mcp.tool()
def saluta(nome: str) -> str:
    """Restituisce un saluto personalizzato"""
    return f"Ciao, {nome}!"


