import asyncio
import argparse
from constants import DESCRIPTION
from ClassBaterry import Battery, BatteryCheckNotification, FastNotification

parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument(
    '-f', '--fast', action='store_true', help='Mostra o status atual'
)
parser.add_argument(
    '-c', '--check', action='store_true', help='loop de informações'
)

args = parser.parse_args()


async def main():
    battery = Battery()
    fast_notify = FastNotification()
    check_battery = BatteryCheckNotification()

    if args.fast:
        await fast_notify.fast_battery_notification()
    if args.check:
        while True:
            battery()
            await check_battery.check_battery_low_and_high()
            await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
