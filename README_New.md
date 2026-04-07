# Inventory Management System
**Micro-Project Submission - Alliance University**

## 📖 Project Overview
This project is a modern, Web-based Inventory and Project Management System. It successfully transitions traditional command-line tracking into a fully interactive web dashboard. Built with Python, the Flask framework, and a persistent SQLite database, it is specifically designed to be an accurate, reliable, and user-friendly solution.

## 👥 Team Roles & Responsibilities
To ensure smooth execution of this micro-project, tasks were evenly divided among team members based on the project's action plan:

- **A. Mohan Teja (Project Lead & Backend):** Responsible for the overall architecture, database schema design (`inventory.db`), and developing the core structural components in Python.
- **A. Surendra (Web Developer):** Built the HTML templates and connected the Python backend to the graphical user forms, ensuring seamless Add/Edit/Delete actions.
- **CH. Avinash reddy (UI/UX styling):** Designed the premium dashboard aesthetic, including the Royal Blue and Gold theme, visual gradients, and soft hover animations.
- **Koushik.N (Data & Logic):** Handled the data formulation and engineered the Python logic that powers the real-time search filtering on the dashboard.
- **Gopala.C (Feature Integration):** Developed and integrated the automated logic for the 'Stock Alert' feature to visually highlight specific products that fall below 5 units.
- **A. Hemanth (Quality Assurance & QA):** Designed and executed the core testing scenarios to guarantee the data is safe and the website is entirely bug-free before final submission.

## 🛠️ Project Methodology Steps

**Step 1: Planning and Information Gathering (Weeks 1-2)**
- Researched inventory system requirements based on the initial project proposals.
- Selected the Tech Stack: Python (Backend), Flask (Routing), SQLite (Persistent Storage), HTML/CSS (Frontend).

**Step 2: Database and Architecture Design (Week 3)**
- Upgraded the initial proposal's plan of using basic CSV files to a much more robust, modern SQLite database.
- Designed `app.py` and strictly defined the data dictionary schemas (`Item` and `Project` schemas).

**Step 3: Backend Development (Week 4)**
- Executed the CRUD protocol (Create, Read, Update, Delete) allowing absolute control over the inventory items.
- Engineered URL routes to safely accept information from Web Forms.

**Step 4: Frontend Development & UI (Week 5)**
- Replaced the text-only interface with a responsive web dashboard format.
- Customized CSS styles to finalize the overarching theme.

**Step 5: Testing & Finalization (Week 6)**
- Validated that the Search function ignores capitalization and works seamlessly.
- Conducted stress testing to guarantee no crashing occurs during empty form submissions or deleting data.

## 🚀 Technical Instructions to Run Our Project
If an evaluator needs to view our project locally, follow these normal steps:
1. Open your terminal and change your directory to the project folder: `cd inventory_management`
2. Install the required Python libraries: `pip install -r requirements.txt`
3. Launch the web server: `python app.py`
4. Jump into the system by clicking the local link: `http://127.0.0.1:5000/`

## 🧪 Quality Testing Confirmed
Our resulting tests guarantee accuracy:
1. **Empty Form Rejections:** Leaving forms blank triggers a flash warning, effectively blocking corrupted system data.
2. **Save Consistency:** Adding a product writes directly to `inventory.db`, ensuring no data loss when shutting the computer down.
3. **Threshold Alerts:** Once an item quantity is updated to a value less than 5, it automatically lights up Red on the dashboard as a visual prompt.
