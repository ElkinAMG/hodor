#!/usr/bin/env python3
"""
Este módulo envía peticiones POST a un host específico.
"""

from typing import Tuple
import httpx


async def send_post_request(url: str, data: dict) -> Tuple[int, bool]:
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=data)
    return response.status_code, response.status_code == 200


async def main():
    url = "http://158.69.76.135/level0.php"
    data = {"id": "1531", "holdthedoor": "Submit"}

    failures = 0
    successes = 0

    for _ in range(1024):
        status_code, success = await send_post_request(url, data)
        if success:
            print(f"{status_code} - SUCCESS")
            successes += 1
        else:
            print(f"{status_code} - FAILURE")
            failures += 1

    print(f"Successes → {successes}\nFailures → {failures}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
