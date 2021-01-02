from python_sample.productservice import  ProductServiceImpl
from python_sample.product_info import Product
#why do we need logger

if __name__ == '__main__':
    service = ProductServiceImpl()
    #service.create_product_table()
    p1 = Product(pid=101,pnm='AAAA',pqty=23,pven='FLip',pprc=2993.34)
    service.add_product(p1)