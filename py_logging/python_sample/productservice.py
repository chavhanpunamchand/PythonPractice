from py_logging.python_sample.app_queries import *
from py_logging.python_sample.product_info import Product
from py_logging.python_sample.db_util import get_connection,close_resources
import logging
                #level --> WARNING
logging.basicConfig(filename='productservice.log',filemode='a',level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#def m1():
#    logging.info('This is info message-20')
#    logging.debug('This is debug Message-10')
#    logging.warning('This is warning message-30')
#    logging.critical('This is critical message-50')
#    logging.error('This is error message-40')



#if __name__ == '__main__':
#    m1()

#import sys
#sys.exit(0)
class ProductServiceImpl:

    def add_product(self,prod):
        logging.info('Inside Add Product method') # info
        if type(prod) == Product:
            dbprod = self.get_product(prod.prodId)
            if dbprod:
                logging.warning('Product WIth given Id already Present')
                return 'Duplicate PRoduct..!'
            try:
                sql = INSERT_PRODUCT.format(prod.prodId,prod.prodName,prod.prodQty,prod.prodPrice,prod.prodVendor)
                logging.info(sql)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                return "Product Added Successfully..!"
            except BaseException as e:
                logging.error(e.args)
                return "Problem in Product Insert...!"
            finally:
                close_resources(conn, cursor)
        return "Invalid Product Type"


    def delete_product(self,pid):
        if type(pid)==int and pid>0:
            dbprod = self.get_product(pid)
            if dbprod:
                try:
                    sql = DELETE_PRODUCT.format(pid)
                    logging.info(sql)
                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.execute(sql)
                    conn.commit()
                    return "Product deleted Successfully..!"
                except BaseException as e:
                    logging.error(e.args)
                    return "Problem in Product delete...!"
                finally:
                    close_resources(conn, cursor)
            else:
                return "Product with Given Id not exist..!"
        return "Invalid Product Type"

    def get_product(self,pid):
        if type(pid) == int and pid > 0:
            try:
                sql = FETCH_PRODUCT.format(pid)
                logging.info(sql)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(sql)
                record = cursor.fetchone()
                if record:
                    return Product(pid=record[0],pnm=record[1],pqty=record[2],pven=record[4],pprc=record[3])
            except BaseException as e:
                logging.error(e.args)
            finally:
                close_resources(conn, cursor)

    def get_all_products(self):
            try:
                sql = FETCH_ALL_PRODUCTS
                logging.info(sql)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(sql)
                records = cursor.fetchall()
                products = []
                for record in records:
                    products.append(Product(pid=record[0], pnm=record[1], pqty=record[2], pven=record[4], pprc=record[3]))
                return products
            except BaseException as e:
                logging.error(e.args)
            finally:
                close_resources(conn, cursor)

    def update_product(self,pid,newvalues):
        if self.get_product(pid) and type(newvalues)==Product:
            try:
                sql = UPDATE_PRODUCT.format(newvalues.prodName, newvalues.prodQty, newvalues.prodPrice, newvalues.prodVendor,newvalues.prodId)
                logging.info(sql)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                return "Product Updated Successfully..!"
            except BaseException as e:
                logging.error(e.args)
                return "Problem in Product Update...!"
            finally:
                close_resources(conn, cursor)
        return "Invalid Product Type or No product with Given Id Exist..!"


    def create_product_table(self):
        try:
            sql = CREATE_TABLE
            logging.info(sql)
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            return "Product Created Successfully..!"
        except BaseException as e:
            logging.error(e.args)
            return "Problem in Product create...!"
        finally:
            close_resources(conn, cursor)



if __name__ == '__main__':
    pr = Product(103, "Watch", 20, "fastrack", 2000)
    prod_service=ProductServiceImpl()
    # prod_service.create_product_table()
    prod_service.add_product(pr)

# dev       -->             qa              --->      uat                   --> prod

#debug/info                 info                    warning                     warning/error

