import time

from collector import get_data
from sender import send
from config import SEND_INTERVAL_SECONDS


def main():
    while True:
        data = get_data()
        print(data)
        send(data)
        time.sleep(SEND_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
