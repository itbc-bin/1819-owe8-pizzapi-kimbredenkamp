from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
    {'name': 'vegetariana'},  # Joost, Paul en Kim
    {'name': 'quattro formaggi'},  # Koen
    {'name': 'taco'},
    {'name': 'pizza pesto'},
    {'name': 'siliciana'},
    {'name': 'quattro stagioni'},
    {'name': 'funghi'},  # Speciaal voor Ruud;)
            ]


@app.route("/", methods=['GET'])
def getPizza():
    return jsonify({'pizzaDB': pizzaDB})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
