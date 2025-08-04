# Employee Performance Management System Backend

## Setup

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your PostgreSQL database and update the `DATABASE_URL` in a `.env` file:
   ```env
   DATABASE_URL=postgresql://user:password@localhost/employee_pms
   ```

4. Create the database tables:
   ```bash
   # In a Python shell or script
   from app.database import Base, engine
   Base.metadata.create_all(bind=engine)
   ```

5. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

## API

- The API will be available at `http://localhost:8000/`
- Employee endpoints: `/employees`

## Authentication & Roles

- Register: `POST /auth/register` (username, email, password, role)
- Login: `POST /auth/login` (returns JWT access token)
- Get current user: `GET /auth/me` (requires Bearer token)
- Roles: employee, manager, HR
- Protect endpoints by requiring JWT and checking user role (see code for examples) 

---

**Notes:**
- All foreign keys are set to `ON DELETE CASCADE` or `ON DELETE SET NULL` as appropriate.
- You may want to add indexes for performance on frequently queried columns (e.g., `employee_id`, `reviewer_id`).
- The `users` table is for authentication and role management; the `employees` table is for employee profiles (they can be linked if needed).

Let me know if you want to add constraints, indexes, or if you need a migration script!
