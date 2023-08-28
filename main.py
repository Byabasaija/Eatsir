import asyncio
import logging
import sys
from app.BotHandler import BotHandler


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    
    asyncio.run(BotHandler().main())