# 📝 Django Task Manager

A feature-rich, responsive task management web app built with Django and styled using Bootstrap 5. Easily track, prioritize, and organize your daily tasks — now with enhanced UI and advanced features like reminders, analytics, and history.

## 🚀 Features

✅ Add, delete, and mark tasks as complete/incomplete  
✅ Set task categories, due dates, priorities (High, Medium, Low)  
✅ Repeating tasks (Daily, Weekly, Monthly)  
✅ Task stats: Total, Completed, Pending, Overdue, Due Today  
✅ History tracking: See when task statuses changed  
✅ One-click "Clear All" and bulk management  
✅ Mobile-first responsive Bootstrap UI  
✅ Real-time toast messages using Django messages  
✅ Visual tags for priority, category, and status  
✅ Clean, card-style layout with badges and icons

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap 5
- **Database:** SQLite (default with Django)
- **Version Control:** Git + GitHub

---

## 🧑‍💻 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/DarshanRedddy/django-task-manager.git
cd django-task-manager

# 2. Create and activate a virtual environment
python3 -m venv env
source env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations and run the server
python manage.py migrate
python manage.py runserver
