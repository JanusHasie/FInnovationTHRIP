import os
import redis

from rq import Worker, Queue, Connection

listen = ['high', 'medium', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:5000')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()



