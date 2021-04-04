from hashlib import sha256
import itertools
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "54ef6292"
key_part_static2_trial = "}"

# characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
# for x in itertools.product(characters, repeat=8):

#     key_part_dynamic1_trial = "".join(x)
#     print("\r now: {}".format(key_part_dynamic1_trial), end="")
#     user_key = key_part_static1_trial  + key_part_dynamic1_trial + key_part_static2_trial
#     s = sha256(user_key.encode()).hexdigest()
#     if key_part_dynamic1_trial == s[4] + s[5] + s[3] + s[6] + s[2] + s[7] + s[1] +s [8]:
#         print(user_key)
#         break


user_key = key_part_static1_trial  + key_part_dynamic1_trial + key_part_static2_trial
print(user_key)

# print(len(sha256(user_key.encode()).hexdigest()))

m = b"PRITCHARD"
s = sha256(m).hexdigest()
print(s[4] + s[5] + s[3] + s[6] + s[2] + s[7] + s[1] +s [8])
