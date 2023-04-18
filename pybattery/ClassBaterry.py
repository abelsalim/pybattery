from os import getcwd
from constants import *
from psutil import sensors_battery
from plyer import notification


class Notificacao:

    async def notify(self, title_notify, icon_notify, timeou_notify):
        notification.notify(
            title=title_notify,
            app_icon=icon_notify,
            timeout=timeou_notify
        )


class Battery(Notificacao):

    def __init__(self):
        self._notified_full = True
        self._notified_level_number = None

        self._battery = sensors_battery().percent
        self._plugged = sensors_battery().power_plugged
        self._reference_battery = sensors_battery().power_plugged

    def __call__(self):
        self._plugged = sensors_battery().power_plugged

    def plug_translation(self):
        return ('Carregando' if self._plugged else 'Descarregando')

    def update_percent(self):
        self._battery = sensors_battery().percent


class BatteryScopeMethod(Battery):

    async def scope(self, photo, time=10):
        message = (
            f'Status: {self.plug_translation()}',
            f'Nível de bateria: {self._battery}'
        )
        await self.notify(
            f'{message[0]}\n{message[1]}',
            f'{getcwd()}{photo}',
            time
        )

    async def search_variable(self, time=10):
        generator = (globals()[f'LEVEL_{x}'] for x in range(1, 6))
        for variavel in generator:
            if self._battery in range(variavel.inicio, variavel.fim):
                await self.scope(variavel.foto, time)

    async def charger_watchdog(self):
        scope = self.scope(CARREGANDO)
        search = self.search_variable()
        await (scope if self._plugged else search)
        self._reference_battery = self._plugged


class NotificationConditionalsForBattery(BatteryScopeMethod):

    async def update_notified_full(self):
        match self._notified_full:
            case True:
                await self.scope(CARREGANDO, 60)

        match (self._plugged, self._battery, sensors_battery().percent):
            case (_, 100, 100):
                self._notified_full = False
            case (False, _, _):
                self._notified_full = True
            case _:
                self._notified_full = True

    async def update_notified_levels(self):
        match self._notified_level_number:
            case number if number != self._battery:
                await self.search_variable()
                self._notified_level_number = self._battery
            case number if int and number < self._battery:
                self._notified_level_number = None


class FastNotification(NotificationConditionalsForBattery):

    async def fast_battery_notification(self):
        await self.search_variable()


class BatteryCheckNotification(NotificationConditionalsForBattery):

    async def check_battery_low_and_high(self):
        self.update_percent()

        match (self._plugged, self._reference_battery):
            case tupla if tupla[0] != tupla[1]:
                await self.charger_watchdog()

        match (self._plugged, self._battery):
            case (True, 100):
                await self.update_notified_full()
            case tupla if not tupla[0] and tupla[1] in NIVEIS:
                await self.update_notified_levels()
            case tupla if tupla[0] <= 15 and tupla[1]:
                await self.update_notified_levels()


if __name__ == '__main__':
    pass
