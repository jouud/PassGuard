import hashlib
import sys

return_data = "return this"

input = sys.argv[1]
output = return_data
print(output)

sys.stdout.flush()

def read_common_pw(pw_file):
    try:
        with open(pw_file) as f:
            common_pw_file = f.read()
    except Exception as e:
        print("Error while trying to read the list of common passwords.")
        exit()
    return common_pw_file

def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()

def brute_force(guess_pw, guess_user_pw, actual_pw_hash, user_pw_file):
    for guess in guess_pw:
        if guess == actual_pw_hash:
            print("Your password is: \"", guess, "\". It was cracked in 10s. Please change it.") #TODO: add timer
            exit()
    for guess in guess_user_pw:
        if guess == actual_pw_hash:
            print("Your password is: \"", guess, "\". It was cracked in 10s. Please change it.") #TODO: add timer
            exit()

    # if password isn't guessed, then it is secure enough but should be added to the list to avoid repetitions
    print("Good job! Your password is secure enough.")
    with open(user_pw_file, "w") as f:
        f.write('\n' + actual_pw_hash)

