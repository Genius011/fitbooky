from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for demonstration purposes
bookings = []

@app.route('/book', methods=['POST'])
def book_training():
    data = request.json
    bookings.append(data)
    return jsonify(message="Booking successful!"), 200

if __name__ == '__main__':
    app.run(debug=True)
