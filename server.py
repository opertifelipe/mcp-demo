from mcp.server.fastmcp import FastMCP
import pandas as pd
# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.resource("csv://example")
def get_example_data() -> str:
    """Get example data in markdown format"""
    data = pd.read_csv("data/example.csv")
    return data.to_markdown()

@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
