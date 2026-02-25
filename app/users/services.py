from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


async def create_user(db, username: str, password: str):
    hashed = hash_password(password)
    await db.execute(
        "INSERT INTO users (username, password) VALUES ($1, $2)",
        username, hashed
    )


async def get_user_by_username(db, username: str):
    return await db.fetchrow(
        "SELECT * FROM users WHERE username = $1",
        username
    )

