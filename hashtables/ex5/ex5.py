# Your code here

# def finder(files, queries):
#     """
#     YOUR CODE HERE
#     """
#     # Your code here
#     cache = {}
#     results = []
    
#     for x in files:
#         key = x.split('/')[-1]
#         value = x
        
#         if key not in cache:
#             cache[key] = []
            
#         cache[key].append(x)
        
#     for q in queries:
#         if q in cache:
#             results += cache[q]

#     return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
