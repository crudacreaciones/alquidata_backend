import httpx
from config import settings

async def generate_automation(instruction: str) -> dict:
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": settings.CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    prompt = f"""
Eres un experto en automatización empresarial. Convierte esta instrucción en JSON n8n:
'{instruction}'
"""

    payload = {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 1024,
        "temperature": 0.3,
        "system": "Eres un generador de flujos JSON para automatizar tareas empresariales en n8n.",
        "messages": [{"role": "user", "content": prompt}]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

