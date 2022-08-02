#!/usr/bin/env python3

from tools import get_access_data

def main():
    tg_token = get_access_data("telegram")
    print(tg_token)

if __name__ == "__main__":
    main()