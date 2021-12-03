# Python 3 code to demonstrate
# SHA hash algorithms.
#  https://www.geeksforgeeks.org/sha-in-python/
import hashlib
import os
os.system('cls' if os.name == 'nt' else 'clear')
# Example of SHA256 forward attack using a list of known hashes indexed by position
# Get Bob's Hash
# Enter Bob's Hash
# get inputs to check

# Create a list of known hashes in range


def createStore(start, end):
    store_list = []
    for number in range(start, end):
        store_list.append(hashlib.sha256(
            str(number).encode('utf-8')).hexdigest())
    return store_list

# Check the hash against the list of known hashes for positioning


def CheckHashList(input_start, store_list, input_hash):
    if input_hash in store_list:
        for i, item in enumerate(store_list):
            if item == input_hash:
                print("Bob's number is: " + str(input_start + i))
                break
    else:
        print("Bob's number is not in the list")

# Input logic


def run(createStore):
    print('If we know the starting value')
    input_start = int(input("Enter the starting number: "))
    print('And we know the ending value')
    input_end = int(input("Enter the ending number: "))
    print('We can then check the hashes against a list of known hashes')
    input_number = int(input("Enter Bob's Number To Be Hashed: "))
    store_list = createStore(input_start, input_end)
    print('Copy and paste the hash of the number or and hash you want to check')
    print(hashlib.sha256(str(input_number).encode('utf-8')).hexdigest())
    input_hash = str(input("Enter Bob's Hash: ")).lower()
    return input_start, store_list, input_hash


def main(createStore, CheckHashList, run):
    input_start, store_list, input_hash = run(createStore)
    CheckHashList(input_start, store_list, input_hash)


if __name__ == '__main__':
    main(createStore, CheckHashList, run)
