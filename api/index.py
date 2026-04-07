from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'super_secret_key_for_flash_messages'

# Database configuration: Use /tmp/ for Vercel serverless (Writable)
if os.environ.get('VERCEL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/inventory.db'
else:
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'inventory.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Phase 1: Database Model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f'<Item {self.name}>'

# New Phase: Project Model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Project {self.name}>'

# Phase 2: Routes (CRUD Operations)

# 1. Display all inventory items in a list (Read)
@app.route('/')
def index():
    search_query = request.args.get('search', '')
    if search_query:
        items = Item.query.filter(Item.name.ilike(f'%{search_query}%')).all()
    else:
        items = Item.query.all()
    
    # Summary Statistics
    total_items = sum(item.quantity for item in items)
    total_value = sum(item.quantity * item.price for item in items)
    low_stock_count = sum(1 for item in items if item.quantity < 5)
    
    return render_template('index.html', 
                         items=items, 
                         search_query=search_query,
                         total_items=total_items,
                         total_value=total_value,
                         low_stock_count=low_stock_count)

# 2. Add a new product (Create)
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        price = request.form.get('price')

        if not name or not quantity or not price:
            flash('All fields are required!')
        else:
            new_item = Item(name=name, quantity=int(quantity), price=float(price))
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('add_product.html')

# 3. Update the quantity or price of an existing item (Update)
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Item.query.get_or_404(id)

    if request.method == 'POST':
        item.name = request.form['name']
        item.quantity = int(request.form['quantity'])
        item.price = float(request.form['price'])

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit_product.html', item=item)

# 4. Delete an item from the inventory (Delete)
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

# ---------------- Projects Routes ----------------
@app.route('/projects')
def projects_list():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        if not name:
            flash('Project name is required!')
        else:
            new_project = Project(name=name, description=description)
            db.session.add(new_project)
            db.session.commit()
            return redirect(url_for('projects_list'))
    return render_template('add_project.html')

# Initialize database within application context
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
