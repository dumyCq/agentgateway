# echo_server.py
from fastmcp import FastMCP

# 1) Create your server instance
mcp = FastMCP("Echo")

# 2) A resource that echoes back via a URI
@mcp.resource("echo://{message}")
def echo_resource(message: str) -> str:
    """Echo a message as a resource"""
    return f"Resource echo: {message}"

# 3) A tool that echoes back via an explicit tool call
@mcp.tool()
def echo_tool(message: str) -> str:
    """Echo a message as a tool"""
    return f"Tool echo: {message}"

# 4) A prompt template for clients
@mcp.prompt()
def echo_prompt(message: str) -> str:
    """Create an echo prompt"""
    return f"Please process this message: {message}"

# 5) Run the server when executed directly
if __name__ == "__main__":
    mcp.run()
