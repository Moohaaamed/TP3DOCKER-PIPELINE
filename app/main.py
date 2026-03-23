from flask import Flask, request, jsonify
from app.tasks import add_task, get_tasks
app = Flask(__name__)

@app.route("/tasks", methods=["GET"])

def list_tasks():
  return jsonify(get_tasks())

@app.route("/tasks", methods=["POST"])

def create_task():
  data = request.json
  task = add_task(data["task"])

  return jsonify({"task":task}),201

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)