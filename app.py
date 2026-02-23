from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis using the service name from docker-compose
redis_client = redis.Redis(host='redis', port=6379)

@app.route("/")
def home():
    count = redis_client.incr('hits')
    return f"""
    <h1>Hello from Docker + Redis!</h1>
    <h2>This page has been visited <span style='color:red'>{count}</span> times</h2>
    """

@app.route("/reset")
def reset():
    redis_client.set('hits', 0)
    return "<h1>Counter Reset!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
