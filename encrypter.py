"""
@author:    TEKIN Abdurrahim Burak
@date:      2016-10-24
-- Encryption program with usage of Threads --
"""

import threading

# unused lists
"""
buchstaben = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
              "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z"]

caeser = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
          "N", "O", "P" "Q", "R", "S", "T", "U", "V", "W",
          "X", "Y", "Z", "A", "B", "C"]

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# dictionary for encryption
encrypt_dict = {"a": "D",
                "b": "E",
                "c": "F",
                "d": "G",
                "e": "H",
                "f": "I",
                "g": "J",
                "h": "K",
                "i": "L",
                "j": "M",
                "k": "N",
                "l": "O",
                "m": "P",
                "n": "Q",
                "o": "R",
                "p": "S",
                "q": "T",
                "r": "U",
                "s": "V",
                "t": "W",
                "u": "X",
                "v": "Y",
                "w": "Z",
                "x": "A",
                "y": "B",
                "z": "C",
                " ": " "}

# dictionary for decryption
decrypt_dict = {"D": "A",
                "E": "B",
                "F": "C",
                "G": "D",
                "H": "E",
                "I": "F",
                "J": "G",
                "K": "H",
                "L": "I",
                "M": "J",
                "N": "K",
                "O": "L",
                "P": "M",
                "Q": "N",
                "R": "O",
                "S": "P",
                "T": "Q",
                "U": "R",
                "V": "S",
                "W": "T",
                "X": "U",
                "Y": "V",
                "Z": "W",
                "A": "X",
                "B": "Y",
                "C": "Z",
                " ": " "}


class MessageEncrypt(threading.Thread):

    """
    encrypts the entered message via dictionary for encryption
    """

    def __init__(self, user_input):
        """
        called by encrypt-method to encrypt the entered message
        :param user_input:
        """
        threading.Thread.__init__(self)

        self.user_input = user_input
        self.encrypted = ""

    def run(self):
        """
        run method for encryption (replacing letters and printing)
        :return:
        """
        encrypted = ""

        # for-loop for encrypting the message
        for c in self.user_input:
            if c in encrypt_dict:
                encrypted += encrypt_dict[c]

        # prints the input message + the encrypted message
        print(self.user_input, encrypted)


class MessageDecrypt(threading.Thread):

    """
    decrypts the entered message via dictionary for decryption
    """

    def __init__(self, user_input2):
        """
        called by decrypt-method to decrypt the entered message
        :param user_input2:
        """
        threading.Thread.__init__(self)

        self.user_input2 = user_input2
        self.decrypted = ""

    def run(self):
        """
        run method for decryption (replacing letters and printing)
        :return:
        """
        decrypted = ""

        # for-loop for decrypting the message
        for c in self.user_input2:
            if c in decrypt_dict:
                decrypted += decrypt_dict[c]

        # prints the input message + the decrypted message
        print(self.user_input2, decrypted)


class Crypt:

    """
    interface where you choose what you want to do
    """

    def __init__(self):

        """
        while True:
        - enter e for encryption
        - enter d for decryption
        - you are asked until you quit the program by entering c
        """

        while True:
            choice = input("Do you want to encrypt or decrypt? - e/d\nc for close! ")
            if choice == "E" or choice == "e":
                self.encrypt()
            elif choice == "D" or choice == "d":
                self.decrypt()
            elif choice == "C" or choice == "c":
                print("==================================")
                print("===========SHUTTING DOWN==========")
                print("==================================")
                break
            else:
                print("==================================")
                print("Please use one of the listed commands: e/d/c")
                print("==================================")

    def encrypt(self):
        """
        parts the input in threads and calls MessageEncrypt()
        :return:
        """

        encrypted = ""
        threads = []

        user_input = str(input("Insert a message! ")).lower()
        for c in user_input:
            if c not in encrypt_dict:
                print("==================================")
                print("Don't use numbers or special characters!")
                print("==================================")
                self.encrypt()

        num_thread = int(input("How many Threads would you like? "))

        print("==================================")
        print("Your encrypted message: ")

        for i in range(0, num_thread):
            beginning = i * int(round(len(user_input) / num_thread))
            end = beginning + round(len(user_input) / num_thread)
            threads.append(MessageEncrypt(user_input[beginning:end]))

        for t in threads:
            t.start()

        print("==================================")


    def decrypt(self):
        """
        parts the input in threads and calls MessageDecrypt()
        :return:
        """

        decrypted = ""
        threads2 = []

        user_input2 = str(input("Insert encrypted message! ")).upper()
        for c in user_input2:
            if c not in decrypt_dict:
                print("==================================")
                print("Don't use numbers or special characters!")
                print("==================================")
                self.decrypt()

        num_thread2 = int(input("How many Threads would you like? "))

        print("==================================")
        print("Your decrypted message: ")

        for i in range(0, num_thread2):
            beginning2 = i * int(round(len(user_input2) / num_thread2))
            end2 = beginning2 + int(round((len(user_input2) / num_thread2)))
            threads2.append(MessageDecrypt(user_input2[beginning2:end2]))

        for t in threads2:
            t.start()

        print("==================================")

# starting the program
c = Crypt()

