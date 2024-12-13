# Data Migration with Alembic and PostgreSQL

## About Alembic
Alembic is a lightweight database migration tool for SQLAlchemy. It allows you to manage schema changes and migrations effectively.

**URL:** [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)

## Prerequisites
- Python installed on your system
- PostgreSQL installed or running in a container
- Docker and Docker Compose installed
- SQLAlchemy installed as part of your Python environment

## Installation and Setup of Alembic
Follow the steps below to set up Alembic and create database migrations.

### Steps

#### 1. Run PostgreSQL using Docker Compose
Create a `docker-compose.yml` file to spin up a PostgreSQL container with environment variables. Below is an example configuration:

```yaml
docker-compose.yml:

version: '3.8'
services:
  postgres:
    image: postgres:16
    container_name: postgres_migration
    environment:
      POSTGRES_USER: alembic_user
      POSTGRES_PASSWORD: alembic_password
      POSTGRES_DB: alembic_db
    ports:
      - "5432:5432"
    volumes:
      - pg_data:/var/lib/postgresql/data
volumes:
  pg_data:
```

Start the container:
```bash
docker-compose up -d
```

#### 2. Initialize Alembic
Run the following command to initialize Alembic in your project:

```bash
alembic init alembic
```
This will create an `alembic` directory with configuration files.

#### 3. Edit the `alembic.init` file for Alembic
After initializing Alembic, update the `alembic.init` file to use your PostgreSQL connection URL:

```python
# alembic.init

sqlalchemy.url = postgresql+psycopg2://alembic_user:admin123@localhost:5432/alembic_db
```

#### 4. Create and Manage Migrations

##### Generate a New Migration
Use the following command to create a new migration:
```bash
alembic revision -m "create user and product tables"
```

Edit the generated migration script to include the creation of two tables (`user` and `product`) with different columns and data types.

##### Second Migration
Generate another migration:
```bash
alembic revision -m "modify user table and add order table"
```

Edit the migration script to:
- Modify the `user` table (e.g., add a new column `phone`).
- Create a new `order` table.

##### Apply Migrations
Run the upgrade command to apply the migrations:
```bash
alembic upgrade head
```

##### Rollback Migrations
Use the downgrade command to roll back the migration by one step:
```bash
alembic downgrade -1
```

To rollback to the base state:
```bash
alembic downgrade base
```

#### 5. Verify Table Creation and Versions
Use `docker exec` to access the PostgreSQL container and verify the tables and migration versions:

```bash
docker exec -it postgres_db psql -U alembic_user -d alembic_db
```

Run SQL commands to check tables:
```sql
\dt
SELECT * FROM alembic_version;
```

## Example Output
1. **First Migration:** Created `user` and `product` tables with different columns and data types.
2. **Second Migration:** Modified the `user` table to add a `phone` column and created a new `order` table.

### Commands:
- **Upgrade:** `alembic upgrade head`
- **Downgrade by one step:** `alembic downgrade -1`
- **Downgrade to base:** `alembic downgrade base`

Provide a screenshot of the PostgreSQL output showing the created tables and Alembic version tracking.
![alembic_sc](https://github.com/user-attachments/assets/192a9ed8-7c2d-4cef-9ef5-7fddde94e4b2)

![alembic_sc2](https://github.com/user-attachments/assets/9aeee965-2eb5-4110-8bf8-b7d561114dc9)
