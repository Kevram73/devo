from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector

# Initialisation de l'application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_key'

# Configuration de la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gesstock",
)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/products')
def list_products():
    cursor = db.cursor()
    query = "SELECT idProduit, nomProduit, descriptionProduit, prixUnitaire, quantiteStock, libelleCategorie" \
            " FROM produits p JOIN categories c " \
            "ON p.idCategorie = c.idCategorie"
    cursor.execute(query)
    products = cursor.fetchall()
    products_list = []

    for product in products :
        product_dict = {
            'id' : product[0],
            'nom': product[1],
            'description': product[2],
            'prixunitaire': product[3],
            'quantitestock': product[4],
            'category': product[5],
        }
        products_list.append(product_dict)
    cursor.close()
    return render_template('products.html', products = products_list)


@app.route('/newproduct', methods=['GET', 'POST'])
def add_product():
    cursor = db.cursor()
    query = "SELECT * FROM categories"
    cursor.execute(query)
    categories = cursor.fetchall()
    categories_list = []

    for category in categories:
        categories_dict = {
            'id': category[0],
            'libelle': category[1],
            'description': category[2],
        }
        categories_list.append(categories_dict)
    cursor.close()

    if request.method == 'POST':
        nom = request.form['nom']
        description = request.form['description']
        prixu = request.form['prixU']
        quantitestock = request.form['quantitestock']
        categorie = request.form['categorie']
        cursor2 = db.cursor()
        query = "INSERT INTO produits (nomProduit, descriptionProduit, prixUnitaire, quantiteStock, idCategorie) VALUES (%s, %s, %s, %s, %s)"
        cursor2.execute(query, (nom, description, prixu, quantitestock, categorie,))
        db.commit()
        cursor.close()
        return redirect(url_for('list_products'))
    return render_template('newproduct.html', categories=categories_list)


@app.route('/categories')
def list_categories():
    cursor = db.cursor()
    query = "SELECT * FROM categories"
    cursor.execute(query)
    categories = cursor.fetchall()
    categories_list = []

    for category in categories:
        categories_dict = {
            'id': category[0],
            'libelle': category[1],
            'description': category[2],
        }
        categories_list.append(categories_dict)
    cursor.close()
    return render_template('categories.html', categories=categories_list)


@app.route('/newcategory', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        libelle = request.form['libelle']
        description = request.form['description']
        cursor = db.cursor()
        query = 'INSERT INTO categories (libelleCategorie, descriptionCategorie) VALUES (%s, %s)'
        cursor.execute(query, (libelle, description,))
        db.commit()
        cursor.close()
        flash('Catégorie créée avec succès!', category='success')
        return redirect(url_for('list_categories'))
    else:
        flash('Nous avons rencontré une erreur!', category='error')
    return render_template('newcategory.html')


@app.route('/clients')
def list_clients():
    cursor = db.cursor()
    query = "SELECT * FROM clients"
    cursor.execute(query)
    clients = cursor.fetchall()
    clients_list = []

    for client in clients:
        clients_dict = {
            'id': client[0],
            'nom': client[1],
            'prenom': client[2],
            'adresse': client[3]
        }
        clients_list.append(clients_dict)
    cursor.close()
    return render_template('clients.html', clients = clients_list)

@app.route('/newclient', methods=['GET', 'POST'])
def add_client():
    return render_template('newclient.html')



@app.route('/employees')
def list_employees():
    cursor = db.cursor()
    query = "SELECT * FROM employes"
    cursor.execute(query)
    employes = cursor.fetchall()
    employes_list = []

    for employe in employes:
        employes_dict = {
            'id': employe[0],
            'nom': employe[1],
            'prenom': employe[2],
            'adresse': employe[3]
        }
        employes_list.append(employes_dict)
    cursor.close()
    return render_template('employees.html', employes = employes_list)

@app.route('/newemploye', methods=['GET', 'POST'])
def add_employee():
    return render_template('newemploye.html')



@app.route('/suppliers')
def list_suppliers():
    return render_template('supplier.html')

@app.route('/newsupplier', methods=['GET', 'POST'])
def add_supplier():
    return render_template('newsupplier.html')


@app.route('/sales')
def list_sales():
    cursor = db.cursor()
    query = "SELECT v.idVente, v.datevente, v.quantiteVendue, p.nomProduit, c.nomClient, e.nomEmploye FROM ventes v " \
                "JOIN produits p ON v.idProduit = p.idProduit " \
                "JOIN clients c ON v.idClient = c.idClient " \
                "JOIN employes e ON v.idEmploye = e.idEmploye"
    cursor.execute(query)
    sales = cursor.fetchall()
    cursor.close()
    sales_list = []

    for sale in sales :
        sales_dict = {
            'id' : sale[0],
            'datevente': sale[1],
            'quantiteVendue': sale[2],
            'produit': sale[3],
            'employe' : sale[4],
            'client' : sale[5]
        }
        sales_list.append(sales_dict)
    return render_template('sales.html', sales = sales_list)

@app.route('/newsale', methods=['GET', 'POST'])
def add_sale():
    cursor = db.cursor()
    query1 = "SELECT idProduit, nomProduit, prixUnitaire FROM produits"
    cursor.execute(query1)
    products = cursor.fetchall()
    products_list = []

    for product in products:
        product_dict = {
            'id': product[0],
            'nom': product[1],
            'prix': product[2]
        }
        products_list.append(product_dict)
    cursor.close()

    cursor2 = db.cursor()
    query2 = "SELECT idClient, nomClient, prenomClient  FROM clients"
    cursor2.execute(query2)
    clients = cursor2.fetchall()
    clients_list = []

    for client in clients:
        client_dict = {
            'id': client[0],
            'nom': client[1],
            'prenom': client[2],
        }
        clients_list.append(client_dict)
    cursor2.close()

    cursor3 = db.cursor()
    query3 = "SELECT idEmploye, nomEmploye, prenomEmploye  FROM employes"
    cursor3.execute(query3)
    employes = cursor3.fetchall()
    employes_list = []

    for employe in employes:
        employe_dict = {
            'id': employe[0],
            'nom': employe[1],
            'prenom': employe[2]
        }
        employes_list.append(employe_dict)
    cursor3.close()

    if request.method == 'POST':
        datevente = request.form['datevente']
        produit = request.form['produit']
        quantite = request.form['quantite']
        employe = request.form['employe']
        client = request.form['client']

        cursorsale = db.cursor()
        querysale = "INSERT INTO ventes(datevente, idProduit, quantiteVendue, idEmploye, idClient) " \
                    "VALUES (%s, %s, %s, %s, %s)"
        cursorsale.execute(querysale, (datevente, produit, quantite, employe, client,))
        db.commit()
        cursorsale.close()
        return redirect(url_for('list_sales'))
    return render_template('newsale.html',employes=employes_list, clients=clients_list, products=products_list)






if __name__ == '__main__':
    app.run(debug=True)
