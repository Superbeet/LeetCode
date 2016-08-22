class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dict = {}
        for word in dictionary:
            abbr = self.gen_abbr(word)
            if abbr not in self.dict:
                word_set = set([word])
                self.dict[abbr] = word_set
            else:
                self.dict[abbr].add(word)
    
    def gen_abbr(self, string):
        if len(string) <= 2:
            return string
        abbr = string[0] + str(len(string)-2) + string[-1]
        return abbr

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.gen_abbr(word)

        if abbr not in self.dict:
            return True
        elif len(self.dict[abbr]) == 1 and word in self.dict[abbr]:
            return True
        else:
            return False
        
# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")