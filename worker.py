#!/usr/bin/env python3

import logging

from app.bot.bot_engine import BotEngine

logging.basicConfig(level=logging.INFO)

def main():
    bot_engine = BotEngine()
    bot_engine.start()

if __name__ == "__main__":
    main()