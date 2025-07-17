📝 Django Task Manager

A full-featured, responsive task management web application built with Django and styled using Bootstrap 5. Designed to help users efficiently manage, prioritize, and track daily tasks with advanced features like analytics, reminders, and history tracking.


 🚀 Features

- ✅ Create & Manage Tasks — Add, edit, delete, or mark tasks as complete/incomplete
- 📅 Due Dates & Repeating Tasks — Set deadlines and choose from Daily, Weekly, or Monthly repeat options
- 🏷️ Task Categorization — Assign categories and priorities (High, Medium, Low) for better organization
- 📊 Smart Dashboard — Displays task insights: total, completed, pending, due today, and overdue
- 🕒 Task History Log — Track completion timestamps and status changes
- ⚡ Bulk Management — One-click "Clear All" feature to reset the task list
- 🔔 Real-Time Feedback — Django messages framework for success/warning toasts
- 📱 Mobile-Responsive UI — Fully responsive layout using Bootstrap 5
- 🎨 Clean Visuals — Badge indicators, color-coded statuses, and card-based layout


 🛠️ Tech Stack

| Layer         | Technology            |
|---------------|-----------------------|
| Backend       | Django (Python)       |
| Frontend      | HTML, CSS, Bootstrap 5|
| Database      | SQLite (default)      |
| Versioning    | Git & GitHub          |



 🧑‍💻 Getting Started

Follow the steps below to run this project locally:

```bash
**# 1. Clone the repository
git clone https://github.com/DarshanRedddy/django-task-manager.git
cd django-task-manager

# 2. Create and activate a virtual environment
python3 -m venv env
source env/bin/activate

# 3. Install project dependencies
pip install -r requirements.txt

# 4. Apply migrations and start the development server
python manage.py migrate
python manage.py runserver**
