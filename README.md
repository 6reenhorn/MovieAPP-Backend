# Movie App Backend

### Overview
This is the backend for the Movie App, built using Django and Django REST Framework (DRF). It provides APIs for managing movies and user authentication. An admin panel is also included for CRUD operations.
- Frontend - Vercel (https://movie-haven-rho.vercel.app)
- Backend - Render (https://movieapp-backend-lr4c.onrender.com)

### Technologies Used
- Django – Backend framework
- Django REST Framework (DRF) – API handling
- PostgreSQL – Database
- AWS – Deployed (Terminated)
- Render - Deployed (Current)

## Setup Instructions

### Prerequisites
- Python installed (>= 3.x)
- PostgreSQL installed and running
- Virtual environment set up

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/movieapp-backend.git
    cd movieapp-backend
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # macOS/Linux
    env\Scripts\activate.bat  # Windows
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure the database: Update `settings.py` with PostgreSQL details:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
5. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
7. Run the server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints
| Methods | Endpoints | Descriptions |
|--------|----------|-------------|
|  POST  | /api/register/ | Register user |
| POST   | /api/login/ | Login user |
| POST   | /api/movie/add/ | Add movie|
| POST   | /api/movie/{id}/reviews/add/ | Add movie reviews |
| POST   | /api/bookmarks/add/{movie_id}/ | Bookmarks a movie |
| GET    | /api/movies/coming-soon/ | Retrieve coming soon movies |
| GET    | /api/movies/released/    | Retrieve released movies |
| GET    | /api/bookmarks/ | Retrieve bookmarked movies |
| GET    | /api/movie/search/?q=movie_title | Retrieve movie by title |
| GET    | /api/genres/ | Retreive movie genres |
| GET    | /api/movies/filter/?genre=genre | Filter movies by genre |
| GET    | /api/genre/{genre}/ | Retrieve movies by genre |
| GET    | /api/movies/ | Retrieve all movies|
| GET    | /api/reviews/ | Retrieve all reviews |
| GET    | /api/movie/{id}/reviews/ | Retrieve specific movie reviews |
| PUT & DELETE    | /api/reviews/{id}/ | Update or Delete movie reviews |
| GET & PUT & DELETE | /api/movie/{id}/  | Retrieve, Update, or Delete specific movie |
| DELETE | /api/bookmarks/remove/{movie_id}/ | Delete bookmarked movie |


### Deployment on AWS (Deployed)
- The backend will be deployed using AWS services such as EC2 or Elastic Beanstalk (Terminated after use).
- The database can be hosted on AWS RDS (PostgreSQL) (Terminated after use).
#### Render for backend (Deployed) | Neon for database (Deployed)
- The backend was deployed on Render for free of charge.
- The database was deployed on Neon for free of charge. 

### Contribution
1. Fork the repository
2. Create a branch: `git checkout -b feature-branch`
3. Make changes and commit: `git commit -m 'Add feature'`
4. Push to GitHub: `git push origin feature-branch`
5. Open a Pull Request
  
## License  
This project is licensed under the MIT License.