from blockchain_utilities import hash

def getString():
    raw_string = input("please enter a single-line message: ")
    string_as_bytes = raw_string.encode()
    return string_as_bytes

if __name__ == '__main__':
    r = getString()
    print(hash('SHA256','hex',r))
