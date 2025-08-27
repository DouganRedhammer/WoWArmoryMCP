import requests
from requests.exceptions import RequestException

def fetch_page(url: str, timeout: int = 300) -> str:

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/126.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        raise RuntimeError(f"Failed to fetch {url}: {e}")