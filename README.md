Library System
Project Overview
This project is a library management system built using Django and Python. It includes a set of HTML pages and associated static assets (CSS and JavaScript) for a fully functional web interface. The system handles book management, user interactions, and administrative tasks.

File Structure
The repository is organized as follows:

project/
statics/
css/: Contains CSS files for styling the web pages. Each HTML page has a corresponding CSS file for its styles.
js/: Contains JavaScript files for client-side interactivity. Each HTML page has a corresponding JS file for its scripts.
templates/
pages/: Contains HTML templates for the web pages. Each page has associated CSS and JS files for styling and functionality in statics folder.
Borrow.html: Page for borrowing books.
add-new.html: Page for adding new books.
admin.html: Administrative dashboard.
bookList.html: Page listing all books.
bookdetails.html: Page showing details of a specific book.
borrowed-books.html: Page listing borrowed books.
homepage.html: Main homepage of the system.
signin.html: Sign-in page for user authentication.
signup.html: Sign-up page for user registration.
db.sqlite3: SQLite database file used for data storage.
Technologies Used
Django: Web framework for Python.
Python: Programming language used for backend development.
HTML/CSS: For structuring and styling the web pages.
JavaScript: For client-side scripting.
SQLite: Lightweight database used for data storage.
