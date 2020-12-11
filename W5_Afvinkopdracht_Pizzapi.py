from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
    {'name': 'vegetariana', 'price': 8.75},  # Joost, Paul
    {'name': 'quattro formaggi', 'price': 9},  # Koen
    {'name': 'taco', 'price': 9},  # Sanne
    {'name': 'pizza pesto', 'price': 10},  # Kim
    {'name': 'siliciana', 'price': 8.5},  # Ruud
    {'name': 'quattro stagioni', 'price': 8.75},
    {'name': 'funghi', 'price': 7.5},  # Speciaal voor Ruud;)
            ]


@app.route("/", methods=['GET'])
def getPizza():
    return jsonify({'pizzaDB': pizzaDB})


@app.route("/<string:name>", methods=['GET'])
def getOnePizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(pizza)
    return jsonify({'pizzaDB': resultPizza})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
