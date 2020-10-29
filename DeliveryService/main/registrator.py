from hashlib import sha256

# TODO: include hash function to registration
# when you register new user, you MUST hash password
print(sha256(bytes("t1", 'utf-8')).hexdigest())
