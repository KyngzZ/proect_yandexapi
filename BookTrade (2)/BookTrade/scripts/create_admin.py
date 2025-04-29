import argparse
from app import create_app, db
from app.models.user import User

app = create_app()
app.app_context().push()

parser = argparse.ArgumentParser(description="Создание администратора")
parser.add_argument("email", help="Email администратора")
parser.add_argument("username", help="Имя администратора")
parser.add_argument("password", help="Пароль администратора")
args = parser.parse_args()

admin = User(email=args.email, username=args.username)
admin.set_password(args.password)
db.session.add(admin)
db.session.commit()
print("Администратор создан.")
