import asyncio
import logging
import sys
from app.example import BotHandler


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    
    asyncio.run(BotHandler().main())