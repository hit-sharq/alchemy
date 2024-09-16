import random

from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# Create a filter user
# filter_user = session.query(User).filter_by(name='malika hDH,J').first()

# if filter_user:
#     print(f'User with name "malika hDH,J" exists, ID: {filter_user.id}')
# else:
#     print('User with name "malika hDH,J" does not exist')

# session.commit()

# Delete a user
# delete_user = session.query(User).filter_by(name='malika hDH,J').first()

# if delete_user:
#     session.delete(delete_user)
#     print(f'User with name "malika hDH,J" deleted successfully')
# else:
#     print('User with name "malika hDH,J" does not exist')

# session.commit()

#users with age >20

# users = session.query(User).filter_by(name='<20').first()

# if users:
#     print(f'Users with age <20 exist, ID: {users.id}')
#     print(f'Name: {users.name}, Email: {users.email}, Age: {users.age}')
# else:
#     print('Users with age <20 do not exist')

users = session.query(User).where(User.age >20 ).all()

for user in users:
    print(f'ID: {user.id}, Name: {user.name}, Email: {user.email}, Age: {user.age}')