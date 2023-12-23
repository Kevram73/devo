class PlatCRUDView:
    
    @staticmethod
    def get_plats():
        plats = Plat.query.all()
        return jsonify([str(plat) for plat in plats])

    @staticmethod
    def get_plat(plat_id):
        plat = Plat.query.get(plat_id)
        if plat:
            return jsonify(str(plat))
        return jsonify({"error": "Plat not found"}), 404

    @staticmethod
    def create_plat():
        data = request.get_json()
        new_plat = Plat(**data)
        db.session.add(new_plat)
        db.session.commit()
        return jsonify(str(new_plat)), 201

    @staticmethod
    def update_plat(plat_id):
        plat = Plat.query.get(plat_id)
        if plat:
            data = request.get_json()
            plat.name = data.get('name', plat.name)
            plat.description = data.get('description', plat.description)
            plat.price = data.get('price', plat.price)
            plat.status = data.get('status', plat.status)
            db.session.commit()
            return jsonify(str(plat))
        return jsonify({"error": "Plat not found"}), 404

    @staticmethod
    def delete_plat(plat_id):
        plat = Plat.query.get(plat_id)
        if plat:
            db.session.delete(plat)
            db.session.commit()
            return jsonify({"message": "Plat deleted successfully"})
        return jsonify({"error": "Plat not found"}), 404