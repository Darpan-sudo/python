class Data:
    def __int__(self):
        self.dataset = [1,2,4,5,6,7]
    def __len__(self):
        return len(self.dataset)


data = Data()

print(len(data))