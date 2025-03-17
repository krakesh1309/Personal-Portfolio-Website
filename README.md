# Personal Portfolio Website

## Overview
This is a **Personal Portfolio Website** built using Django, HTML, CSS, and JavaScript. It showcases personal details, projects, and a contact section while maintaining a clean and modern design.

## Features
- **Homepage** - A welcoming page with an introduction.
- **About Page** - Provides details about skills, experience, and interests.
- **Projects Page** - Showcases completed projects with descriptions.
- **Contact Page** - Allows visitors to reach out via a contact form.
- **Reusable Base Template** - A single base template (`base.html`) to ensure consistency across pages.
- **Navigation System** - Links between pages for easy access.
- **Responsive Design** - Mobile-friendly and visually appealing.
- **JavaScript Enhancements** - Smooth scrolling, animations, and form validations.

## Tech Stack
- **Backend**: Django (Python Framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default Django database)
- **CSS Framework**: Custom CSS & Bootstrap (optional)

## Project Structure
```
Personal-Portfolio/
│── portfolio/          # Django project directory
│   ├── templates/
│   │   ├── base.html   # Common layout for all pages
│   │   ├── home.html   # Home page
│   │   ├── about.html  # About page
│   │   ├── projects.html  # Projects page
│   │   ├── contact.html  # Contact page
│   ├── static/         # Static files (CSS, JS, Images)
│   ├── views.py        # Handles page rendering
│   ├── urls.py         # URL routing
│── manage.py           # Django management tool
│── db.sqlite3          # SQLite database (optional)
│── requirements.txt    # Required dependencies
```

## Installation & Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/Personal-Portfolio.git
   cd Personal-Portfolio
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```sh
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser to view the site.

## Customization
- Update **base.html** for global styles and navigation.
- Modify **CSS & JavaScript** for custom styling and animations.
- Add more sections or improve the UI as needed.

## Contribution
Feel free to contribute to this project. You can:
- Fork the repository
- Make improvements
- Submit a pull request


