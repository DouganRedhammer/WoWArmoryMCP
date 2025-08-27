from mcp.server.fastmcp import FastMCP
import requests
from webpage_fetch import fetch_page
from typing import Annotated
from pydantic import Field

mcp = FastMCP("wow-armory")
base_url = "https://worldofwarcraft.blizzard.com/en-us/character/us/"

@mcp.tool() 
def get_character_info(
    realm: Annotated[str, Field(description="The realm (server) where the character resides. E.g., 'akama'")],  
    character_name: Annotated[str, Field(description="The name of the character to retrieve information for. E.g., 'bob'")]
) -> str:
    """
    Retrieves the World of Warcraft character page from Blizzard's Armory website.
    The LLM can then interpret this page to answer questions about the character.
    """
    character_url = f"{base_url}{realm}/{character_name.lower()}" 

    try:
        response = fetch_page(character_url)
        return response 
    except requests.exceptions.RequestException as e:
        return f"Error fetching character information: {str(e)}" 
@mcp.tool()  
def get_character_reputation(
    realm: Annotated[str, Field(description="The realm (server) where the character resides. E.g., 'akama'")], 
    character_name: Annotated[str, Field(description="The name of the character to retrieve information for. E.g., 'bob'")]
) -> str:
    """
    Retrieves the World of Warcraft character reputation page from Blizzard's Armory website.
    The LLM can then interpret this page to answer questions about the character.
    """
    
    character_url = f"{base_url}{realm}/{character_name.lower()}/reputation"

    try:
        response = fetch_page(character_url)
        return response 
    except requests.exceptions.RequestException as e:
        return f"Error fetching character reputation information: {str(e)}"

if __name__ == "__main__":
    mcp.run()

    