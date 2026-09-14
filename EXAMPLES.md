# 🎯 Примеры использования RTP Plugin на известных серверах

## Анализ популярных RTP имплементаций

### Hypixel (Minecraft Java)
- ✅ Использует `/rtp` для случайной телепортации
- ✅ Кулдаун: 10 секунд
- ✅ Радиус: 10,000 - 30,000 блоков
- ✅ Защита: Проверка на лаву и воду

### 2b2t (Anarchy Server)
- ✅ Использует `/warp random`
- ✅ Огромный радиус: 300,000 блоков
- ✅ Нет кулдауна (но очень затратно по ресурсам)
- ✅ Игнорирует безопасность (для сложности)

### Mineplex
- ✅ Фирменная система `/rtp`
- ✅ Цветные сообщения при телепортации
- ✅ Интеграция с системой достижений
- ✅ Кулдаун: 30 секунд

### Cubecraft
- ✅ Две команды: `/warp near` и `/warp far`
- ✅ Премиум игроки: меньший кулдаун
- ✅ Система бана на опасные области
- ✅ Логирование всех телепортаций

---

## 🎮 Примеры конфигурации для популярных типов серверов

### 1️⃣ Survival сервер (как на Hypixel)

```json
{
  "short_range": 500,
  "long_range": 10000,
  "y_min": 40,
  "y_max": 256,
  "safe_ground_search": true,
  "max_attempts": 100,
  "cooldown": 10,
  "min_player_distance": 100,
  "banned_biomes": ["ocean", "deep_ocean", "frozen_ocean"]
}
```

**Особенности:**
- Защита от спавна в воде
- Высокий кулдаун для балансировки
- Проверка расстояния от других игроков

### 2️⃣ Anarchy сервер (как 2b2t)

```json
{
  "short_range": 50000,
  "long_range": 300000,
  "y_min": 0,
  "y_max": 320,
  "safe_ground_search": false,
  "max_attempts": 5,
  "cooldown": 0,
  "enable_nether": true,
  "enable_end": true
}
```

**Особенности:**
- Максимальная сложность
- Можно телепортироваться в лаву
- Поддержка Nether и End
- Быстрый поиск (мало попыток)

### 3️⃣ PvP сервер (как на Mineplex)

```json
{
  "short_range": 100,
  "long_range": 1000,
  "y_min": 60,
  "y_max": 200,
  "safe_ground_search": true,
  "max_attempts": 50,
  "cooldown": 30,
  "protected_zones": [
    {"x": 0, "z": 0, "radius": 500}
  ],
  "teleport_delay": 5,
  "cannot_teleport_in_combat": true
}
```

**Особенности:**
- Защищённые зоны (спавны)
- Задержка перед телепортацией (для баланса)
- Блокировка во время боя
- Высокий кулдаун

### 4️⃣ Креатив сервер

```json
{
  "short_range": 200,
  "long_range": 5000,
  "y_min": 0,
  "y_max": 320,
  "safe_ground_search": false,
  "max_attempts": 20,
  "cooldown": 2,
  "allow_void_teleport": true,
  "instant_teleport": true
}
```

**Особенности:**
- Низкий кулдаун
- Можно телепортироваться в пустоту
- Мгновенная телепортация

### 5️⃣ Role-Play сервер (как на Cubecraft)

```json
{
  "short_range": 300,
  "long_range": 2000,
  "y_min": 50,
  "y_max": 256,
  "safe_ground_search": true,
  "max_attempts": 75,
  "cooldown": 15,
  "vip_cooldown": 8,
  "premium_range_multiplier": 1.5,
  "teleport_animation": true,
  "broadcast_teleport": false,
  "log_teleports": true
}
```

**Особенности:**
- Разные кулдауны для VIP и обычных игроков
- Увеличенный радиус для премиума
- Анимация телепортации
- Логирование для модерации

### 6️⃣ SkyBlock сервер

```json
{
  "short_range": 50,
  "long_range": 500,
  "y_min": 60,
  "y_max": 200,
  "safe_ground_search": true,
  "max_attempts": 100,
  "cooldown": 5,
  "island_only": true,
  "check_island_protection": true,
  "respect_claim_borders": true
}
```

**Особенности:**
- Телепортация только на острова
- Проверка прав владения
- Проверка границ клейма

---

## 📊 Рекомендации по кулдауну

| Тип сервера | Кулдаун | Причина |
|-------------|--------|--------|
| Survival | 5-10 сек | Балансировка ресурсов |
| PvP | 20-30 сек | Противодействие бегству |
| Creative | 2-5 сек | Творческая свобода |
| Anarchy | 0 сек | Максимальная сложность |
| Role-Play | 10-20 сек | Игровой баланс |
| Event | 0-5 сек | Для ивентов |

---

## 🔒 Система безопасности

### Проверка на опасные биомы

```python
DANGEROUS_BIOMES = [
    "ocean", "deep_ocean", "frozen_ocean",
    "lava", "soul_sand_valley"
]

def is_safe_biome(self, biome: str) -> bool:
    return biome not in DANGEROUS_BIOMES
```

### Система защиты от триггеров лага

```python
def check_entity_density(self, x: int, z: int) -> bool:
    """Проверить плотность сущностей на координатах"""
    # Не телепортироваться если слишком много мобов
    return entity_count < MAX_ENTITIES
```

---

## 🎁 Примеры интеграции с популярными плагинами

### LiteBans (система банов)

```python
from litebans import LiteBans

def can_teleport(self, player):
    # Проверить не забанен ли игрок от RTP
    return not LiteBans.is_banned(player, "rtp")
```

### Citizens (NPC)

```python
from citizens import Citizens

def get_rtp_npc():
    # Создать NPC, который дает RTP
    npc = Citizens.create_npc("Random Wizard")
    npc.add_trait("rtp")
    return npc
```

### EssentialsX (утилиты)

```python
from essentials import Essentials

def teleport_with_essentials(player, x, y, z):
    # Использовать систему телепортации EssentialsX
    Essentials.teleport(player, Location(x, y, z))
```

---

## 📈 Оптимизация для больших серверов

### Кэширование результатов

```python
from functools import lru_cache
import time

class OptimizedRTP:
    def __init__(self):
        self.location_cache = {}
        self.cache_ttl = 300  # 5 минут
    
    def get_cached_location(self, player_id):
        if player_id in self.location_cache:
            cached_time, location = self.location_cache[player_id]
            if time.time() - cached_time < self.cache_ttl:
                return location
        return None
```

### Асинхронная генерация координат

```python
import asyncio

async def generate_location_async(self, player, distance):
    """Неблокирующая генерация координат"""
    loop = asyncio.get_event_loop()
    location = await loop.run_in_executor(
        None, 
        self.generate_safe_location, 
        player, 
        distance
    )
    return location
```

---

**Версия:** 1.0.0  
**Последнее обновление:** 2026-09-14  
**Источники:** Hypixel, Mineplex, 2b2t, Cubecraft документация
