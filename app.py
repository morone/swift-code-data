from flask import Flask, request, jsonify
from flasgger import Swagger
from swift_data_scraper import SwiftDataScraper

app = Flask(__name__)
Swagger(app)
scraper = SwiftDataScraper()

@app.route('/api/swift', methods=['GET'])
def get_swift_data():
    """
    Endpoint to get SWIFT data
    This endpoint takes a SWIFT code and returns the corresponding data
    ---
    tags:
      - SWIFT API
    parameters:
      - name: code
        in: query
        type: string
        required: true
        description: The SWIFT code to get data for.
    responses:
      200:
        description: SWIFT code data
        schema:
          type: object
          properties:
            bank:
              type: string
            branch:
              type: string
            address:
              type: string
            city:
              type: string
            postcode:
              type: string
            country:
              type: string
            connection:
              type: string
    """
    swift_code = request.args.get('code', default=None, type=str)
    if swift_code:
        data = scraper.get_data(swift_code)
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"error": "Unable to fetch data. Please try again later."}), 500
    else:
        return jsonify({"error": "No swift code provided."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
