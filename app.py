from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define the Item class
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

# Fractional Knapsack Function
def fractional_knapsack(capacity, items):
    items.sort(key=lambda item: item.ratio, reverse=True)
    total_value = 0
    for item in items:
        if capacity - item.weight >= 0:
            capacity -= item.weight
            total_value += item.value
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break
    return total_value

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    capacity = data['capacity']
    items_data = data['items']
    items = [Item(item['value'], item['weight']) for item in items_data]
    max_value = fractional_knapsack(capacity, items)
    return jsonify({'max_value': max_value})

if __name__ == '__main__':
    app.run(debug=True)
