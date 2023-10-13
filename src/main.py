from mnemonic import Mnemonic


def generate_mnemonic(strength=256):
    # Generate mnemonic
    mnemo = Mnemonic("english")
    return mnemo.generate(strength)  # Convert bytes back to bits


if __name__ == "__main__":
    mnemonic = generate_mnemonic(256)
    print("Generated BIP39 mnemonic:")
    print(mnemonic)
