from flask_login import UserMixin

from crow.app import db, login_manager, bcrypt

class User(db.Document, UserMixin):
  username = db.StringField()
  password = db.StringField()
  clearance = db.IntField(default=0)
  # 0 - User
  # 1 - Admin

  @staticmethod
  def is_authenticated():
    return True

  @staticmethod
  def is_active():
      return True

  @staticmethod
  def is_anonymous():
    return False

  def get_id(self):
    return self.username

  @staticmethod
  def check_password(password_hash, password):
      return check_password_hash(password_hash, password)

  @login_manager.user_loader
  def load_user(username):
    u = User.objects(username=username).first()
    if not u:
      return None
    return u
