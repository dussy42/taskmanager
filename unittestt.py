import unittest
from run import getprice ,getproduct ,getpriceindex 






# test for all user inpust to be valid
##################################################################################################################################################################






class Test(unittest.TestCase):


    # test to make sure the user input a valid whole number greater than zero
    def test_ValidPriceInput(self):
        result = getprice()
        self.assertTrue(result.isnumeric() ,msg="price input should be a whole number" )
        self.assertTrue(int(result) > 0,msg="price input should be greater than 0")


 # test to make sure the user input a valid whole PRODUCT 
    def test_ValidProductInput(self):
        result = getproduct()
        self.assertTrue(len(result) >= 3,msg="product input should be more than three chracters")
        self.assertTrue(result[:3].isalpha() ,msg="product input should start with first three letters" )




 # test to make sure the user input a valid whole Price index 
    def test_ValidPriceIndex(self):
        result = getpriceindex()
        self.assertTrue(str(result).isnumeric() ,msg="price index input should be a whole number" )
        self.assertTrue(int(result) > 0,msg="price inded  input should be most be > 0")
        self.assertTrue(int(result) <=4 ,msg="price inded  input should be most be < 4" )




###################################################################################################################################################################3

if __name__ =="__main__":

       
    unittest.main()