#!/usr/bin/env python3

from bot_engine import BotEngine
from planner import Planner

def main():
    planner = Planner()

    bot_engine = BotEngine(planner)
    bot_engine.start()

if __name__ == "__main__":
    main()