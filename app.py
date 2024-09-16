import random
from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# Create a new user
# new_user = User(name='malika hDH,J', email='johndoe@example.com', age=30)
# session.add(new_user)
# session.commit()

# #ordering = session

# # List of names
# names = ["andré", "délice", "marie", "joséphine"]
# #list of ages
# ages = [20, 30, 40, 21, 25, 27, 30]

# # Generate a random number of users
# num_users = random.randint(5, 10)

# # Generate users
# for _ in range(num_users):
#     name = random.choice(names)
#     age = random.choice(ages)
#     email = f"{name.replace(' ', '.')}{random.randint(100, 999)}@example.com"

#     new_user = User(name=name, email=email, age=age)
#     session.add(new_user)
#     session.commit()    

# #order data
# users = session.query(User).order_by(User.id).all()


# # Print all users
# for user in users:
#     print(user.id, user.name, user.email, user.age)


