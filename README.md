# Telegram bot: Decide restaurant for lunch

## Introduction

Randomly decide restaurant for lunch every weekdays.

## How to use

choose either option below to run the application:

### Option 1: Python

1. Set your `MSG_TIME` in `app/main.py`
2. Set your `TOKEN` and `CHAT_ID` in `app/tg/config.py`
3. Start the application with the following command:

```sh
cd app/
pip install -r requirements.txt
python main.py
```

### Option 2: Docker Compose

1. Set your `MSG_TIME`, `TOKEN` and `CHAT_ID` in `docker-compose.yml`
2. Start the container with the following command:

```sh
docker-compose up -d
```

## Development Tips

### How to ignore changed files (temporarily)

Run the following commands to ignore changed `docker-compose.yml` after setting your `MSG_TIME`, `TOKEN` and `CHAT_ID`.

```sh
git update-index --assume-unchanged docker-compose.yml
```

So as the python files if you chose to hardcode your environment variables in them.

```sh
git update-index --assume-unchanged app/main.py
git update-index --assume-unchanged app/tg/config.py
```

To revert that ignorance use the following command:

```sh
git update-index --no-assume-unchanged <file>
```
