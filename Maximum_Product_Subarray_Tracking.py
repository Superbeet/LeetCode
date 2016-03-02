"""
[2,3,-2,4] -> [2,3]
"""
import sys
import operator
MinInt = -sys.maxint
MaxInt = sys.maxint
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        size = len(nums)

        if size==1:
            return nums[0]

        product = 1
        # sub_product = []
        # neg_num = []
        first = False
        first_product = 1
        last_product= 1
        product_max = MinInt
        pre_product = 1
        # product_max = [MinInt for i in range(size)]
        for i in xrange(0, size):
            product *= nums[i]

            if nums[i]<0:
                last_product = nums[i]

            if product<0: 
                if not first:
                    # first = i
                    first_product = product
                    first = True

            # print "pre_product->", pre_product
            if product==0 or i==size-1:
                if product>0:
                    print "product->", product
                    product_max = max(product_max, product)
                    product = 1

                elif product<0:
                    print "product->", product
                    print "first_product->", first_product            
                    print "last_product->", last_product
                    product_no_first = product/first_product
                    product_no_last = product/last_product
                    product_max = max(product_max, product_no_first, product_no_last)

                else: #==
                    product_no_first = product/pre_product
                    product_no_last = product/last_product
                    product_max = max(product_max, product_no_first, product_no_last)

                first_product = 1
                last_product= 1
                product = 1
                pre_product = 1
                first = False
            # else:

                # product *= nums[i]

            # print "first_product->", first_product            
            # print "last_product->", last_product

            pre_product = product

        print "%s product_max->%s"%(nums ,product_max)
        return product_max

sol = Solution()
# sol.maxProduct([0,2])
# sol.maxProduct([-2,1])
# sol.maxProduct([2,1])
# sol.maxProduct([2,3])
# sol.maxProduct([2,3,4])
# sol.maxProduct([1,0,-1,2,3,-5,-2])
# sol.maxProduct([-4,-3,-2])
sol.maxProduct([-2,0,-1])




            





        # sub_product.append(product)

        # print "sub_product->", sub_product
        # print "neg_num->", neg_num

        # if len(neg_num)%2==0:
        #     return reduce(operator.mul, sub_product+neg_num, 1)

        # else:
        #     no_first = reduce(operator.mul, sub_product[1:]+neg_num[1:], 1)
        #     no_last  = reduce(operator.mul, sub_product[:-1]+neg_num[:-1], 1)
        #     print no_first
        #     print no_last

        #     return max(no_first, no_last)
