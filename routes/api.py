

from flask import Blueprint, request, jsonify
from utils.inverted_index import InvertedIndex


api_bp = Blueprint('api', __name__)
index = InvertedIndex()  

@api_bp.route('/documents', methods=['POST'])
def add_document():
    data = request.get_json()
    if not data or 'id' not in data or 'text' not in data:
        return jsonify({"error": "Invalid input. 'id' and 'text' are required."}), 400

    doc_id = data['id']
    text = data['text']

    
    index.add_document(doc_id, text)
    return jsonify({"message": "Document added successfully."}), 200

@api_bp.route('/search', methods=['GET'])
def search_documents():
    query = request.args.get('query', '')
    mode = request.args.get('mode', 'union')

    if not query:
        return jsonify({"error": "Query parameter 'query' is required."}), 400

    # Get search results from the inverted index
    results = index.search(query, mode)
    # Format the result as a list of dictionaries
    response = [{"id": doc_id, "text": text} for doc_id, text in results]
    return jsonify({"results": response}), 200
