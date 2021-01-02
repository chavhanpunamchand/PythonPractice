
class Product:

    def __init__(self,pid,pnm,pqty,pven,pprc):
        self.prodId = pid
        self.prodName = pnm
        self.prodPrice = pprc
        self.prodQty = pqty
        self.prodVendor = pven

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''


if __name__ == '__main__':
    pr=Product(101,"besan",10,"chhaya",110)
    print(pr)

