# FORCE REBUILD v6 - Supabase
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print("=" * 60)
print("API/INDEX.PY LOADING - SUPABASE")
print("=" * 60)

# Get Supabase URL
DATABASE_URL = os.environ.get("SUPABASE_URL")

if DATABASE_URL:
    print(f"\nUsing Supabase database")
    print(f"   URL preview: {DATABASE_URL[:60]}...")
else:
    DATABASE_URL = "sqlite:///./nutrition_app.db"
    print("\nNo SUPABASE_URL found - Using SQLite fallback")

# Fix URL format if needed
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    print("Fixed postgres:// to postgresql://")

# Set environment variable
os.environ["DATABASE_URL_OVERRIDE"] = DATABASE_URL

print("\nInitializing database...")

try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from app.models import Base, User, UserRole
    from app.auth import get_password_hash

    # Create engine with connection pooling
    engine = create_engine(
        DATABASE_URL,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,
        pool_recycle=3600,
    )

    print("Engine created")

    # Create tables
    Base.metadata.create_all(bind=engine)
    print("Tables created")

    # Seed users
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        existing = db.query(User).filter(User.username == "admin").first()
        if not existing:
            admin = User(
                username="admin",
                password=get_password_hash("admin123"),
                role=UserRole.ADMIN,
            )
            head = User(
                username="head1",
                password=get_password_hash("pass123"),
                role=UserRole.AUTHORITY,
            )
            parent = User(
                username="parent1",
                password=get_password_hash("pass123"),
                role=UserRole.PARENT,
            )

            db.add_all([admin, head, parent])
            db.commit()
            print("Seeded 3 users: admin, head1, parent1")
        else:
            print("Users already exist")
    finally:
        db.close()

    print("\nDATABASE READY")

except Exception as e:
    print(f"\nDATABASE ERROR: {e}")
    import traceback

    traceback.print_exc()

print("=" * 60)
print("LOADING FASTAPI APP")
print("=" * 60 + "\n")

# Import FastAPI app
from app.main import app

# Export for Vercel
app = app
