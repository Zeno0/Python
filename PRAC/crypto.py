
# import hashlib

# # Generate the secret key
# secret_key = b'abcdefghijklmnopqrstuvwxyz'
# print(secret_key)

# # The message to be signed
# message = b'Hello World'
# print(hashlib.sha256(message + secret_key).digest())
# print('-'*100)
# # Create the hash chain by repeatedly applying the hash function
# hash_chain = [hashlib.sha256(message + secret_key).digest()]
# print(hash_chain[-1])
# for i in range(1, 10):
#     duh = hashlib.sha256(hash_chain[-1] + secret_key).digest()
#     hash_chain.append(duh)
#     print('-'*100)
#     print(duh)
#     print('inside loop')
#     print('-'*100)
# print(hash_chain)
# print(len(hash_chain))
# # Use the first hash value in the chain as the signature
# signature = hash_chain[0]

# # To verify the signature
# verify_message = b'Hello World'
# verify_key = b'abcdefghijklmnopqrstuvwxyz'
# verify_hash_chain = [hashlib.sha256(verify_message + verify_key).digest()]
# for i in range(1, 10):
#     verify_hash_chain.append(hashlib.sha256(verify_hash_chain[-1] + verify_key).digest())

# if signature == verify_hash_chain[0]:
#     print("Signature is valid")
# else:
#     print("Signature is not valid")
import hashlib

message = b'Hello World'
hash_object = hashlib.sha256()
hash_object.update(message)
hash_value = hash_object.hexdigest()
print(hash_value)

print(hashlib.__all__)
print(hashlib.__builtins__)
print(help(hashlib))