from passlib.context import CryptContext
from src.db import SessionLocal, User

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_admin_user(email, password):
    db = SessionLocal()
    if db.query(User).filter(User.email == email).first():
        print(f"User {email} already exists.")
        db.close()
        return
    user = User(email=email, password_hash=pwd_context.hash(password), is_admin=True)
    db.add(user)
    db.commit()
    db.close()
    print(f"Admin user {email} created.")

if __name__ == "__main__":
    import getpass
    email = input("Admin email: ")
    password = getpass.getpass("Admin password: ")
    create_admin_user(email, password)
