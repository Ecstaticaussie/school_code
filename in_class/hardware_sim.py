from random import randint

main_mem = {bin(i)[2:]: randint(1, 20) for i in range(16)}

class CPU:
    def address_give(self):
        return bin(randint(0, 15))[2:]

    def get_data(self, data):
        self.current_data = data

class PC:
    def __init__(self):
        self.CPU = CPU()
        self.main_mem = main_mem

    def fetching(self):
        address = self.CPU.address_give()
        print(f"Address: {address}\nData: {self.main_mem[address]}")
        self.CPU.get_data(self.main_mem[address])

    def decoding(self):
        pass

    def executing(self):
        pass

    def fde_cycle(self):
        self.fetching()
        self.decoding()
        self.executing()

if __name__ == "__main__":
    amd_PC = PC()
    amd_PC.fde_cycle()