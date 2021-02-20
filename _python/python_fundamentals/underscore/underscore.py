# print(1)
class Underscore:
    def map(self, iterable, callback):
        # your code here
        new_iterable = map(callback, iterable)
        return new_iterable
    def find(self, iterable, callback):
        # your code here
        f = list(filter(callback, iterable))[0] 
        return f
    def filter(self, iterable, callback):
        # your code
        new_iterable = filter(callback, iterable)
        return new_iterable
    def reject(self, iterable, callback):
        # your code
        z = filter(callback, iterable)
        iterable = [e for e in iterable if e not in z]
        return iterable

# you just created a library with 4 methods!
# let's create an instance of our classcopy
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0) # should return [2, 4, 6] after you finish implementing the code ab
print(evens)

double = _.map([1,2,3], lambda x: x*2) # should return [2,4,6]
print(double)
greaterThan4 = _.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
print(greaterThan4)
evens_2 = _.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
print(evens_2)
reject = _.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]
print(reject)