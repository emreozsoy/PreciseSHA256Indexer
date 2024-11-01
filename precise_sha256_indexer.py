import h5py
import hashlib
from decimal import Decimal, getcontext
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set precision for Decimal operations
getcontext().prec = 31

def generate_hashes(start, end, step):
    """Generates SHA256 hashes for values between start and end, storing them in an HDF5 file."""
    with h5py.File("hash_data.h5", "w") as hdf5_file:
        # Create a dataset for the hash values with an unlimited size
        hash_dataset = hdf5_file.create_dataset("hashes", (0,), maxshape=(None,), dtype="S64")
        
        current = start
        while current <= end:
            sha_hash = hashlib.sha256(str(current).encode()).hexdigest()
            # Resize the dataset to accommodate the new entry and append it
            hash_dataset.resize((hash_dataset.size + 1,))
            hash_dataset[-1] = sha_hash.encode()  # Store as byte string for consistency with HDF5

            logging.info(f"Hash for {current}: {sha_hash}")

            current += step  # Move to the next value

def check_hash(target_hash):
    """Checks if the given SHA256 hash is present in the HDF5 file."""
    with h5py.File("hash_data.h5", "r") as hdf5_file:
        hash_dataset = hdf5_file["hashes"]
        
        # Read all hashes into a list
        hash_values = [hash.decode('utf-8') for hash in hash_dataset[:]]
        veri_sayisi = len(hash_dataset)

        logging.info(f"Total {veri_sayisi} hash values in the file.")
        
        # Hash value search
        if target_hash in hash_values:
            return "Hash found! It is in the range."
        else:
            return "Hash not found. It is NOT in the range."

if __name__ == "__main__":
    # Define range and step for generating hashes
    start_value = Decimal("1.300000000000000000000000000000")
    end_value = Decimal("1.309999999999999999999999999999")
    step_value = Decimal("0.000000000000000000000000000001")

    # Uncomment the following line to generate hashes
    # generate_hashes(start_value, end_value, step_value)

    # Hash value to check
    target_hash = "436df2a697a2ea4b91e927b221d97d984a43b54d04e02a3df0be0c4c45bb31fc"  # Example hash

    # Check the given hash against stored hashes
    result = check_hash(target_hash)
    print(result)
