# Student Result Generator (Method Overloading Concept) 
#A school system calculates student results differently depending on available data. 
#Create a Result class where a method can calculate the result using either two subjects or three subjects. 
class Result:
    def calculate(self, a, b, c=None):
        if c is None:
            total = a + b
            print("Total Marks (2 subjects):", total)
        else:
            total = a + b + c
            print("Total Marks (3 subjects):", total)

r = Result()

r.calculate(80, 90)
r.calculate(75, 85, 95)