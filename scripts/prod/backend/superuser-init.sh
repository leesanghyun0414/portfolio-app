

init_superuser() {
cat << EOF | python manage.py shell
from django.contrib.auth.models import User
from django.db.models.query import EmptyQuerySet
import environ

## Docker Secret File
#POSTGRES_PASSWORD_FILE = env.get_value("POSTGRES_PASSWORD_FILE", str)
#f = open(f"{POSTGRES_PASSWORD_FILE}", "r", encoding='utf-8')
#POSTGRES_PASSWORD = f.read()
#f.close()

# Return Queryset object
superusers = User.objects.filter(is_superuser=True)

if not superusers.exists():
    env = environ.Env()
    username = env.get_value("DJANGO_SUPERUSER_USERNAME", str)
    password = env.get_value("DJANGO_SUPERUSER_PASSWORD", str)
    email = env.get_value("DJANGO_SUPERUSER_EMAIL", str)
    User.objects.create_superuser(username, email, password)
EOF
}