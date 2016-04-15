def compress_string(string):
    if string==None:
        return None
    
    size = len(string)
    if size<2:
        return string
    
    string_builder = []
    prev = string[0]
    count = 1
    for i in xrange(1, size):
        if string[i]==prev:
            count += 1
        else:
            string_builder.append(prev)
            string_builder.append(str(count))
            count = 1
            prev = string[i]
            
            if len(string_builder)>=size:
                return string
    
    string_builder.append(prev)
    string_builder.append(str(count))
    
    if len(string_builder)>=size:
        return string
    else:
        string = "".join(string_builder)
        return string

def decompress_string(pattern):
    if pattern == None:
        return pattern
    
    size = len(pattern)
    
    string_builder = []
    
    j = 0
    i = 2
    while i<size:
        if pattern[i].isalpha():
            string_builder.extend([pattern[j]]*int(pattern[j+1:i]))
            j = i
        i += 1
        
    string_builder.extend([pattern[j]]*int(pattern[j+1:]))
    
    return "".join(string_builder)

org_str = "aabcccccaaa"
print org_str
pattern = compress_string(org_str)
print pattern
string = decompress_string(pattern)
print string