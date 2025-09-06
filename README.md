# Redis Playground

This repository is a simple playground for experimenting with Redis in Python.
There’s no specific goal — it’s just a place to try out Redis commands, caching, and connections.

## Prerequisites

- Python 3.10+
- Redis installed on your machine
  For Mac OS
  ```bash
  brew install redis
  ```

## Setting Up Redis

Make sure Redis is running before using this script. You can start Redis in the background (daemon mode) with:

```bash
redis-server --daemonize yes
```

This will start Redis as a background service for the current session.

## Getting Started

- Clone the repository:

```bash
git clone https://github.com/kayc0des/redis_caching
cd redis_caching
```

- Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

- Install requirements:

```bash
pip install -r requirements.txt
```

- Get into the cache directory:

```bash
cd cache
```

- Run the Python script:

```bash
python3 main.py
```

- You should see output like:

```bash
kayc0des
```

This confirms that the script successfully connected to Redis, set a value, and retrieved it.

## Notes

- This repo is meant for learning and experimenting, not for production use.
- Make sure Redis is running before executing the script.
- For stopping Redis, you can use:

```bash
redis-cli shutdown
```