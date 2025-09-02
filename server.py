# server.py
from mcp.server.fastmcp import FastMCP
import time
from mock_confluence_service import pages

# Create an MCP server
mcp = FastMCP("confluence")

@mcp.tool()
def get_confluence_page_by_id(page_id: str) -> str:
    """
    Use this tool to get the content of a Confluence page by its id.

    
    Args:
        page_id (str): The id of the Confluence page to get.
        
    Returns:
        str: The content of the Confluence page.
    """
    
    # Sleep for 3 seconds
    time.sleep(3)
    
    # get the page from the pages list
    page = next((page for page in pages if page["id"] == page_id), None)
    if page:
        return page["content"]
    else:
        return f"Page with id {page_id} not found."

@mcp.tool()
def get_confluence_pages() -> list[dict]:
    """
    Use this tool to get a list of all Confluence pages available to you.
    Confluence pages in this workspace contain information about current projects that the user might be working on.

    
    Returns:
        list[dict]: A list of Confluence pages with their id and title.
    """
    return [
        {
            "id": page["id"],
            "title": page["title"]
        }
        for page in pages
    ]
