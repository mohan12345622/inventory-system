# Inventory Management System

A Web-based Inventory Management System built with Python, Flask, and SQLite. This micro-project is developed as a submission for Alliance University.

## 👥 Student Team Members
- A. Mohan Teja
- A. Surendra
- CH. Avinash reddy
- Koushik.N
- Gopala.C
- A. Hemanth

## 🚀 How to Run the Application

### Prerequisites
Make sure you have Python installed on your system.

### Steps
1. **Navigate to the Project Folder:**
   Open your terminal/command prompt and navigate to the project directory:
   ```bash
   cd inventory_management
   ```

2. **Install the Requirements:**
   Install the necessary Python libraries via pip:
   ```bash
   pip install -r requirements.txt
   ```
   *(Alternatively: `pip install Flask Flask-SQLAlchemy`)*

3. **Run the Application:**
   Start the Flask server by running the main Python script:
   ```bash
   python app.py
   ```
   *Note: The SQLite database (`inventory.db`) will be generated automatically on the first run.*

4. **View the System:**
   Open any web browser and navigate to the local development address:
   ```
   http://127.0.0.1:5000/
   ```

## 🧪 5 Test Cases for Accuracy and Reliability
To fulfill the "accurate and reliable" criteria promised in our project Rationale, perform the following tests:

1. **Test Case 1: Empty Form Field Rejection**
   - **Action:** Try to submit the "Add New Product" form without filling in the Name or Quantity.
   - **Expected Result:** The system should reject the submission and flash a warning message stating "All fields are required!".

2. **Test Case 2: Successful Product Insertion**
   - **Action:** Add a completely valid product (e.g., Name: "Dell Monitor", Quantity: 15, Price: 200.50). 
   - **Expected Result:** The item is securely stored in the SQLite database and instantly populates correctly on the main Dashboard.

3. **Test Case 3: Accurate Search Filtering**
   - **Action:** Use the search bar to type a partial string (e.g., "mon" for Monitor).
   - **Expected Result:** The table filters dynamically, accurately retrieving any products matching the term (case-insensitive) while hiding unrelated items.

4. **Test Case 4: Automated Low Stock Alerts**
   - **Action:** Edit a product and deliberately reduce its quantity to **less than 5** (e.g., 3 units).
   - **Expected Result:** The system should instantly flag that row by highlighting it in Red and generating a "Low Stock!" warning badge.

5. **Test Case 5: Safe Data Deletion**
   - **Action:** Click "Delete" on an inventory item and accept the browser confirmation prompt.
   - **Expected Result:** The item is permanently removed from the database and no longer displays on the main Inventory Dashboard
   