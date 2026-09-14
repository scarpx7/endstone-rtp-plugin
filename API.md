# API для Endstone RTP Plugin

## Использование в других плагинах

Вы можете использовать RTP Plugin как зависимость в своих плагинах.

### Импорт

```python
from rtp_plugin import RTPPlugin
```

### Получение экземпляра плагина

```python
from endstone.plugin import Plugin
from endstone.server import Server

class MyPlugin(Plugin):
    def on_load(self) -> None:
        # Получить плагин RTP
        rtp = self.server.get_plugin_command("rtp")
        if rtp and isinstance(rtp, RTPPlugin):
            self.rtp_plugin = rtp
        else:
            self.logger.warning("RTP Plugin not found!")
```

### Программная телепортация

```python
from endstone.player import Player
from endstone.world import World

def teleport_player_randomly(player: Player, distance: int = 100):
    """Телепортировать игрока на случайное расстояние"""
    location = self.rtp_plugin.generate_safe_location(player, distance)
    
    if location:
        player.teleport(location[0], location[1], location[2])
        player.send_message(f"Вы телепортированы на {int(location[0])}, {int(location[1])}, {int(location[2])}")
    else:
        player.send_message("Не удалось найти безопасное место для телепортации!")
```

### Проверка использованных координат

```python
def get_used_locations() -> set:
    """Получить все использованные координаты"""
    return self.rtp_plugin.used_locations.copy()

def clear_used_locations():
    """Очистить кэш использованных координат"""
    self.rtp_plugin.used_locations.clear()
```

## Хуки и события

### На телепортацию

```python
@player_event
def on_player_teleport(event):
    player = event.player
    self.logger.info(f"{player.name} был телепортирован")
```

## Примеры интеграции

### Телепортация при смерти

```python
from endstone.event import player_event

class DeathTPPlugin(Plugin):
    def on_load(self):
        self.rtp = self.server.get_plugin_command("rtp")
    
    @player_event
    def on_player_death(self, event):
        player = event.player
        location = self.rtp.generate_safe_location(player, 500)
        if location:
            player.teleport(location[0], location[1], location[2])
            player.send_message("Вы телепортированы из-за смерти!")
```

### Телепортация при вхождении

```python
from endstone.event import player_event

class JoinTPPlugin(Plugin):
    def on_load(self):
        self.rtp = self.server.get_plugin_command("rtp")
    
    @player_event
    def on_player_join(self, event):
        player = event.player
        if player.first_time:  # Только для новых игроков
            location = self.rtp.generate_safe_location(player, 1000)
            if location:
                player.teleport(location[0], location[1], location[2])
                player.send_message("Добро пожаловать! Вы телепортированы в случайное место.")
```

## Расширенные примеры

### Система квестов с телепортацией

```python
class QuestTPPlugin(Plugin):
    def on_load(self):
        self.rtp = self.server.get_plugin_command("rtp")
        self.quests = {}
    
    def start_quest(self, player: Player, radius: int = 500):
        location = self.rtp.generate_safe_location(player, radius)
        if location:
            self.quests[player.name] = {
                'start': player.location,
                'destination': location,
                'progress': 0
            }
            player.teleport(location[0], location[1], location[2])
            player.send_message("Квест начат! Найдите целевые координаты!")
```

---

**Версия API:** 1.0.0  
**Совместимость:** Endstone 0.1.0+
