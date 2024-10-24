# Перевод голоса в речь

**Поддерживает:**
- Голосовые сообщения
- Видео сообщения

## Конфигурация
Настройте конфигурацию, переименуйте .env.example в .env, а затем отредактировав необходимые параметры по желанию:
- BOT_TOKEN = Ваш ключ Телеграм

## Установка
**Клонируйте репозиторий и перейдите в каталог проекта:**
    git clone https://github.com/Pynajy/voice_to_text.git
    cd voice_to_text

#### Из папки
**1. Создайте виртуальную среду:**
```
python -m venv venv
```
**2. Активируйте виртуальную среду:**
    ### For Linux or macOS:
    source venv/bin/activate
    
    ### For Windows:
    venv\Scripts\activate
**3. Установите зависимости с помощью requirements.txt файла:**
```
pip install -r requirements.txt
```
**4. Для запуска бота используйте следующую команду:**
```
python bot/main.py
```

#### Использование Docker Compose
**Выполните следующую команду для сборки и запуска образа Docker:**
```
docker compose up
```