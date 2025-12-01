import datetime
start = datetime.datetime.now()

# separates out pattern strings by length
def constructLengthDictionary(patterns, lengthDictionary):
    for item in patterns:
        length = len(item)  # use integer
        if length not in lengthDictionary:  # compare with integer
            lengthDictionary[length] = set([item])  # store with integer key
        else:
            lengthDictionary[length].add(item)
    return lengthDictionary

def lengthfunct(e):
    return len(e)

def can_construct(test_str, length_dict, memo=None):
    if memo is None:
        memo = {}
    if test_str in memo:
        return memo[test_str]
    if not test_str:  # Empty string means we successfully used everything
        return True  
    # Try each possible prefix
    for length in length_dict:
        if len(test_str) < length:
            continue
        prefix = test_str[:length]
        if prefix in length_dict[length]:
            # If this prefix works, recursively try to build the rest
            if can_construct(test_str[length:], length_dict, memo):
                memo[test_str] = True
                return True      
    memo[test_str] = False
    return False

def count_constructions(test_str, length_dict, memo=None):
    if memo is None:
        memo = {}
    if test_str in memo:
        return memo[test_str]
    if not test_str:  # Empty string means we found one valid path
        return 1
        
    total_ways = 0
    # Try each possible prefix
    for length in length_dict:
        if len(test_str) < length:
            continue
        prefix = test_str[:length]
        if prefix in length_dict[length]:
            # Add the number of ways to construct the remaining string
            total_ways += count_constructions(test_str[length:], length_dict, memo)
                
    memo[test_str] = total_ways
    return total_ways

def onOpen():
    with open("text/day19.txt") as f:
        text = f.read()
    patterns, requests = text.split("\n\n")
    patterns = patterns.split(", ")
    requests = requests.split("\n")
    count,total = full_count(patterns,requests)
    return count,total

def full_count(patterns,requests):
    lengthDictionary = constructLengthDictionary(patterns,{})
    count = 0
    total = 0
    for request in requests:
        check = can_construct(request, lengthDictionary, memo=None)
        if check == True:
            count+=1
            total+=count_constructions(request, lengthDictionary, memo=None)
    return count, total

count,total = onOpen()
print("Requests that are possible to fulfill: " + str(count))
print("Total number of ways to fulfill requests: " + str(total))
print("Time: "+ str(datetime.datetime.now() - start))