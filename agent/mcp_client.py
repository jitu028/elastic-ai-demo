import os
import json
import urllib.request
import urllib.error
import sys

class MCPClient:
    def __init__(self):
        self.api_key = os.getenv("DEVELOPER_KNOWLEDGE_API_KEY")
        self.endpoint = "https://developerknowledge.googleapis.com/mcp"
        if not self.api_key:
            raise ValueError("DEVELOPER_KNOWLEDGE_API_KEY is not set.")

    def call_tool(self, tool_name, arguments):
        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": self.api_key,
        }
        body = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments
            },
            "id": 1,
        }
        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(self.endpoint, data=data, headers=headers, method="POST")

        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                if "error" in res_data:
                    return {"error": res_data["error"]}
                
                tool_result = res_data.get("result", {})
                content_list = tool_result.get("content", [])
                for content_item in content_list:
                    if content_item.get("type") == "text":
                        return json.loads(content_item.get("text", "{}"))
        except Exception as e:
            return {"error": str(e)}
        return {}

    def search_deprecations(self, library_name):
        query = f"{library_name} release notes deprecations breaking changes 2025 2026"
        return self.call_tool("search_documents", {"query": query})

    def get_full_docs(self, doc_names):
        return self.call_tool("batch_get_documents", {"names": doc_names})
