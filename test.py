import redis
r = redis.Redis(
host= 'precious-cod-38221.upstash.io',
port= '6379',
password= 'AZVNAAIjcDEzYjgzOThiNmQ0OWM0NWE1YTk0Y2E5NzY3NThjNWJlYnAxMA', 
ssl=True)
r.set('foo','bar')
print(r.get('foo'))