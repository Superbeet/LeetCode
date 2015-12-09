class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i=0
        j=0

        ver_str_1 = version1.split('.')
        ver_str_2 = version2.split('.')
        
        while i<len(ver_str_1) or j<len(ver_str_2):

            ver_1_part = int(ver_str_1[i]) if i<len(ver_str_1) else 0

            ver_2_part = int(ver_str_2[j]) if i<len(ver_str_2) else 0

            if ver_1_part>ver_2_part:
                return 1

            elif ver_1_part<ver_2_part:
                return -1

            i += 1
            j += 1

        return 0
