from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    def hash(value: str):
        return pwd_context.hash(value)

    def compare_hash(plain_value: str, hashed_value: str):
        return pwd_context.verify(plain_value, hashed_value)