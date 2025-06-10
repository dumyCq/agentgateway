import sys
import time
import subprocess

p = subprocess.Popen(["python", "-m", "duckduckgo_mcp_server.server"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

init = '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test-client","version":"0.1.0"}}}\n'
list_tools = '{"jsonrpc":"2.0","id":2,"method":"tools/list"}\n'

# Send initialize
p.stdin.write(init)
p.stdin.flush()
time.sleep(1)

# Send tools/list
p.stdin.write(list_tools)
p.stdin.flush()

# Read output
try:
    while True:
        line = p.stdout.readline()
        if not line:
            break
        print(line.strip())
except KeyboardInterrupt:
    p.terminate()
