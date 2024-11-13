from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy.orm import  Mapped, mapped_column
from db import db

class User(db.Model, UserMixin):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(100), nullable=False)

    def __repr__(self):
        return (f"<User(id={self.id}, username='{self.username}', "
                f"is_authenticated={self.is_authenticated}, is_active={self.is_active})>, is_anonymous={self.is_anonymous} ")


