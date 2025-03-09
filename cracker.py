import hashlib

def password_cracker(hash_file, common_pass_file):
    try:
        with open(hash_file, 'r') as hashed_file:
            hashed_passwd = [line.strip() for line in hashed_file]

        with open(common_pass_file, 'r') as passwd_file:
            common_passwd = [line.strip() for line in passwd_file]
        
        for passwd in common_passwd:
            passwd_hash = hashlib.md5(passwd.encode()).hexdigest()
            for hashed_password in hashed_passwd:
                if passwd_hash == hashed_password:
                    print(f"password found : {passwd} and hash: {passwd_hash}")

    except FileNotFoundError:
        print("File(s) not found")
    except Exception as err:
        print(f"Error: {err}")


hashFile = "1MillionPassword_hashed.txt"
commonPassFile = "password_list.txt"
password_cracker(hashFile, commonPassFile)


    
