import hashlib

def password_cracker(hash_file, common_pass_file):
    try:
        with open(hash_file, 'r') as hashed_file: #opening the hashed text file
            hashed_passwd = [line.strip() for line in hashed_file] #strip() removes all the leading and trailing characters from the string.

        with open(common_pass_file, 'r') as passwd_file:
            common_passwd = [line.strip() for line in passwd_file] #opening the common password list
        
        for passwd in common_passwd:
            passwd_hash = hashlib.md5(passwd.encode()).hexdigest() #enocode() converts strings into bytes and haslib.md5() hashed the enocded bytes
            for hashed_password in hashed_passwd:                  #hexdigest() converts the hash bytes into a hexadecimal string
                if passwd_hash == hashed_password:      
                    print(f"password found : {passwd} and hash: {passwd_hash}")  #parses through all the hashed hexadecimal string and if a match is found
                                                                                # it prints it
#error handling for either an invalid file or some other error
    except FileNotFoundError:
        print("File(s) not found")
    except Exception as err:
        print(f"Error: {err}")

#running example
hashFile = "1MillionPassword_hashed.txt"
commonPassFile = "password_list.txt"
password_cracker(hashFile, commonPassFile)

    
