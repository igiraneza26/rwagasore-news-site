**Project Overview**  
**Rwagasore News Site** is a **Reddit-style news and discussion platform** focused on **Prince Louis Rwagasore of Burundi**.  
The goal is to create a **community-driven discussion space** where users can:  
- Post news and articles  
- Comment on discussions  
- Upvote/downvote posts  
- Categorize posts into topics  

**Target Audience**  
- **History Enthusiasts** - Discuss Prince Louis Rwagasore’s legacy  
- **Journalists & Researchers** - Share and analyze news articles  
- **Students & Educators** - Learn about Burundi’s history and politics  

---

**Tech Stack**  
- **Frontend:** Vue.js (for a modern, interactive UI)  
- **Backend:** Django + Django REST Framework (API-driven architecture)  
- **Database:** PostgreSQL (Relational database for structured data)  
- **Authentication:** JWT (JSON Web Token) authentication for security  
- **Deployment:** Heroku (Cloud-based hosting solution)  

---

**Data Schema Overview**  

The application follows a **relational data model** with the following main entities:  

**Categories (`news_category`)**  
| Field | Type | Description |
|--------|-------|-------------|
| `id` | Integer (Primary Key) | Unique ID for each category |
| `name` | CharField | Category name (e.g., Politics, Culture) |
| `slug` | SlugField | URL-friendly identifier |

**Users (`auth_user`)**  
| Field | Type | Description |
|--------|-------|-------------|
| `id` | Integer (Primary Key) | Unique user ID |
| `username` | CharField | Unique username |
| `email` | EmailField | User email |
| `password` | CharField | Encrypted password |
| `groups` | ManyToManyField | User roles (Admin, Moderator, RegularUser) |

**Posts (`news_post`)**  
| Field | Type | Description |
|--------|-------|-------------|
| `id` | Integer (Primary Key) | Unique post ID |
| `title` | CharField | Post title |
| `content` | TextField | Main post content |
| `author` | ForeignKey (User) | User who created the post |
| `category` | ForeignKey (Category) | Post category |
| `created_at` | DateTimeField | Timestamp of creation |

**Comments (`news_comment`)**  
| Field | Type | Description |
|--------|-------|-------------|
| `id` | Integer (Primary Key) | Unique comment ID |
| `post` | ForeignKey (Post) | Post being commented on |
| `author` | ForeignKey (User) | Comment creator |
| `content` | TextField | Comment text |
| `created_at` | DateTimeField | Timestamp |

**Votes (`news_vote`)**  
| Field | Type | Description |
|--------|-------|-------------|
| `id` | Integer (Primary Key) | Unique vote ID |
| `post` | ForeignKey (Post) | Voted post |
| `user` | ForeignKey (User) | Voter |
| `vote_type` | CharField (Choices: `upvote`, `downvote`) | Vote type |

---

**Security Features**  

| Feature | Description |
|---------|------------|
| **JWT Authentication** | Secures API endpoints, preventing unauthorized access |
| **Role-Based Permissions** | Admins, Moderators, and Regular Users have different privileges |
| **Password Hashing** | Django stores passwords using a secure hashing algorithm |
| **CSRF Protection** | Protects against Cross-Site Request Forgery attacks |
| **HTTPS Enforcement** | Enforces encrypted connections when deployed |

---

**Deployment Guide**  

**Step 1: Setup & Install Dependencies**  
Clone the repository:  
```bash
git clone https://github.com/igiraneza26/rwagasore-news-site.git
cd rwagasore-news-site
```
Install dependencies:  
```bash
pip install -r requirements.txt
```
Set up the database:  
```bash
python manage.py migrate
```
Create a superuser:  
```bash
python manage.py createsuperuser
```
---

**Step 2: Run the Server Locally**  
```bash
python manage.py runserver
```
Access the site at: **http://127.0.0.1:8000/**  

---

**Step 3: Deploy to Heroku**  

1**Login to Heroku:**  
```bash
heroku login
```
**Create a new Heroku app:**  
```bash
heroku create rwagasore-news-site
```
**Set environment variables:**  
```bash
heroku config:set DEBUG=False
heroku config:set SECRET_KEY="my_secret_key"
```
**Push code to Heroku:**  
```bash
git push heroku main
```
**Apply migrations & create superuser:**  
```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```
**Open the app in a browser:**  
```bash
heroku open
```
**Your site is now live!**
![alt text](image.png)