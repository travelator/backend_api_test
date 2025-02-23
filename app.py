from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": ["http://localhost:8080"]}})


@app.route('/api/rate-info', methods=['GET'])
def get_rate_info():
    # Replace this with actual data from your backend or database
    rate_data = [
        {
            "title": "Backend data: Visit the British Museum",
            "description": "Explore a vast collection of art and antiquities from around the world at the British Museum, one of London's most iconic cultural institutions.",
            "image_link": "https://www.visitlondon.com/-/media/images/london/visit/things-to-do/sightseeing/london-attractions/british-museum/british-museum-2023-images/british-museum-in-london.jpg?h=360&w=640&rev=9705af40409148acb39ad44319df9111&hash=33A9991BE2DE2CAF1B052471CD5ACEBE",
            "price": "0",
            "theme": 'Culture',
            "id": 1
        },
        {
            "title": "Ride the London Eye",
            "description": "Experience panoramic views of London's skyline from the London Eye, a giant Ferris wheel situated on the South Bank of the River Thames.",
            "image_link": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/London-Eye-2009.JPG/800px-London-Eye-2009.JPG",
            "price": "60",
            "theme": 'Culture',
            "id": 2
        },
        {
            "title": "Explore Hyde Park",
            "description": "Enjoy a leisurely stroll, picnic, or boating in Hyde Park, one of London's largest and most famous green spaces.",
            "image_link": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Hyde_Park_London_from_the_air.jpg/640px-Hyde_Park_London_from_the_air.jpg",
            "price": "0",
            "theme": 'Relaxation',
            "id": 3
        },
        {
            "title": "Tour the Tower of London",
            "description": "Discover the rich history of the Tower of London, a historic castle on the north bank of the River Thames, known for housing the Crown Jewels.",
            "image_link": "https://www.cuddlynest.com/blog/wp-content/uploads/2022/12/visiting-the-tower-of-london-scaled.jpg",
            "price": "30",
            "theme": 'Culture',
            "id": 4
        },
        {
            "title": "See a West End Theatre Show",
            "description": "Experience world-class theatre productions in London's West End, renowned for its vibrant performing arts scene.",
            "image_link": "https://images.ctfassets.net/6pezt69ih962/5emZ299oIHRkgEgovv4sqd/74b5f91b5ceaa2893a582a005a5bbe72/004-Andy-Paradise-min.jpg",
            "theme": 'Entertainment',
            "price": "80",
            "id": 5
        }
    ]
    return jsonify(rate_data)

@app.route('/api/rate-info/preferences', methods=['POST'])
def post_rate_data():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Check if data is received
        if data:
            print("Received data:", data)
        
        # Here you could process the data, store it in a database, etc.
        # For demonstration, we will simply return the data back with a success message.
        return jsonify({"message": "Data received successfully", "data": data}), 200
    except Exception as e:
        # Handle any errors that occur during the process
        return jsonify({"error": str(e)}), 500


@app.route('/api/itinerary', methods=['GET'])
def get_itinerary_info():
    # Replace this with actual data from your backend or database
    itinerary_data = [
        {
            "api status": "api working",
        },
    ]
    return jsonify(itinerary_data)

@app.route('/api/home-data', methods=['POST'])
def post_user_data():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Check if data is received
        if data:
            print("Received data:", data)
        
        # Here you could process the data, store it in a database, etc.
        # For demonstration, we will simply return the data back with a success message.
        return jsonify({"message": "Data received successfully", "data": data}), 200
    except Exception as e:
        # Handle any errors that occur during the process
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
