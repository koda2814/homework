# I decided to write a code that generates data filtering object from a list of keyword parameters:

class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """
    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [
            item for item in data 
            if all(i(item) for i in self.functions)
        ]


def make_positive_even():
    # positive_even = Filter(lamba a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(int, a))) - here is 3 bugs
    # 1. 'lamba' must be 'lambda'
    # 2. isinstance(int, a) must be isinstance(a, int). First arg - class instance(obj), second - type of class
    # 3. All lambda funcs must be in list, because Filter takes only one arg.

    positive_even = Filter([lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)])
    return positive_even.apply(range(100)) # should return only even numbers from 0 to 99


def make_filter(**keywords):
    """
        Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():
        def keyword_filter_func(data): #here is second bug.
            #arg in keyword_filter_func - var 'value' must have another name, 
            # because we`ll have some problems with scope
            return data[key] == value
        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


sample_data  =  [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]

#make_filter(name='polly', type='bird').apply(sample_data) #should return only second entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.
