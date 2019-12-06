

def main():
    class base64:
        string = input("String to encode: ")
        # Create a list of characters
        chars = list(string)

        # Convert characters to decimals
        def char2dec(self):
            self.decimals = []
            for char in self.chars:
                dec = ord(char)
                self.decimals.append(dec)
            return self.decimals

        #Convert decimals to 8-bit binary
        def dec2bin(self):
            self.bin_list = []
            for decimal in self.decimals:
                self.binary = bin(decimal)
                self.bin_list.append(self.binary)
            return self.bin_list

        print(dec2bin.bin_list)  

if(__name__ == "__name__"):
    main()
