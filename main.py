from service import db, app

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=2000, host='0.0.0.0')
