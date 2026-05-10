from flask import request, jsonify
from services import create_user, get_all_users, delete_user, update_user

def register_routes(app):
    @app.route("/users", methods=["POST"])
    def add_user():
        data = request.json
        user = create_user(data)
        return jsonify(user.to_dict())

    @app.route("/users", methods=["GET"])
    def user():
        users = get_all_users()
        return jsonify([u.to_dict() for u in users])

    @app.route("/user/<int:id>", methods=["DELETE"])
    def remove(id):
        delete_user(id)
        return {"message": "User Deleted"}

    @app.route("/user/<int:id>", methods=["PUT"])
    def edit_user(id):
        data = request.json
        user = update_user(id, data)
        return jsonify(user.to_dict())
    

    @app.route("/user/<int:id>", methods=["PATCH"])
    def partial_edit_user(id):
        data = request.json
        user = update_user(id, data)
        return jsonify(user.to_dict())  
    
  