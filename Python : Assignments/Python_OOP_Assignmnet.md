## Python OOP Assignment
**Q1. What is the purpose of Python's OOP?
**

Ans. In Python, object-orineted programming is a programming paradigm which uses the conecpt of object and classes. The main aim of oop is to implement real-world entities programmatically.

**Q2. Where does an inheritance search look for an attribute?
**

Ans. An inheritance search looks for an attribute first in the instance object, then in the class the instance was created from, then in all higher superclasses, progressing from left to right (by default). The search stops at the first place the attribute is found.

**Q3. How do you distinguish between a class object and an instance object?**

Ans. Class object is like a blueprint for intance object but instance object is a concrete item in out code. Instance objects are new namespaces, they start out empty but inherit object attributes that live in class object.

**Q4. What makes the first argument in a class’s method function special?**

Ans. The first argument in a class’s method is self which is the object itself . The self keyword is used to represent an instance (object) of the given class.Since the class is just a blueprint, self allows access to the attributes and methods of each object in python. This allows each object to have its own attributes and methods. Thus, even long before creating these objects, we reference the objects as self while defining the class.

**Q5. What is the purpose of the init method?**

Ans. __init__() is used to initialize a newly created object. The __init__ method lets the class initialize the object's attributes and serves no other purpose.

**Q6. What is the process for creating a class instance?**

Ans. To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts.

**Q7. What is the process for creating a class?**

Ans. Using class keyword. e.g class <classname>:


**Q8. How would you define the superclasses of a class?**

Ans. 

	class DerivedClassName(SuperClassName):
		pass

**Q9. What is the relationship between classes and modules?**

Ans.  Modules are collections of methods and constants. They cannot generate instances. Classes may generate instances (objects), and have per-instance state (instance variables).

**Q10. How do you make instances and classes?**

Ans. To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts. To create the class we use keyword class followed by classname.

Q11. Where and how should be class attributes created?

Ans. A class attribute is shared by all instances of the class. To define a class attribute, you place it outside of the __init__() method. Classname is used to access the class attributes.  Syntax -   <attribute name> = <attribute value>

Q12. Where and how are instance attributes created?

Ans. Instance attributes are defined in the __init__() method using self parameter. 
     e.g  class Test:
				def __init__(self):
					self.pi = 3.14

Q13. What does the term "self" in a Python class mean?

Ans. The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

Q14. How does a Python class handle operator overloading?

Ans. In Python, overloading is achieved by overriding the method which is specifically for that operator, in the user-defined class. For example, __add__(self, x) is a method reserved for overloading + operator, and __eq__(self, x) is for overloading ==.

Q15. When do you consider allowing operator overloading of your classes?

Ans. When one or both operands are of a user-defined class.

Q16. What is the most popular form of operator overloading?

Ans. Addition (+) operator overloading is most popular form of operator overloading.

Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?

Ans. Inheritance and Polymorphism

Q18. Describe three applications for exception processing.

Ans. 1. Prevents Application Crashes : Unhandled exception may result in application crash. So even to prevent a crash an application 	needs to handle exceptions 
	 2. Redirect to Another flow of application : In some cases, there may be a need to change the flow of the program in the event of an error condition e.g., in online shopping portal, when a payment API request throws exception, user journey would require the application to handle it and take the user back to the basket page so that user can initiate the payment again.
	 3. Logging: This is required for troubleshooting.
	 
Q19. What happens if you don't do something extra to treat an exception?

Ans. When an exception occurred, if you don't handle it, the program terminates abruptly and the code past the line that caused the exception will not get executed.

Q20. What are your options for recovering from an exception in your script?

Ans. To recover from an exception we can use  a generic except clause, which handles any exception.After the except clause(s), we can include an else-clause. The code in the else-block executes if the code in the try: block does not raise an exception.The else-block is a good place for code that does not need the try: block's protection.

Q21. Describe two methods for triggering exceptions in your script.

Ans.  1. Using raise keyword
	  2. Using assertion

Q22. Identify two methods for specifying actions to be executed at termination time, regardless of  
whether or not an exception exists.

Ans. 	1. finally block 
		2. 
Q23. What is the purpose of the try statement?

Ans. The try statement allows you to define a block of code to be tested for errors while it is being executed. 

Q24. What are the two most popular try statement variations?

Ans.  1. try/except 2. try/except/finally

Q25. What is the purpose of the raise statement?

Ans. raise statement is usedto explicitly raise an exception in python

Q26. What does the assert statement do, and what other statement is it like?

Ans. The assert keyword is used when debugging code. The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError. Assert is like if..else

Q27. What is the purpose of the with/as argument, and what other statement is it like?

Ans. The with statement is a replacement for commonly used try/finally error-handling statements. The with statement in Python helps you with resource management. It ensures you don’t accidentally leave any resources open. The with statement is similar to try..except block only

Q28. What are *args, **kwargs?

Ans. *args specifies the number of non-keyworded arguments that can be passed and the operations that can be performed on the function in Python whereas **kwargs is a variable number of keyworded arguments that can be passed to a function that can perform dictionary operations

Q29. How can I pass optional or keyword parameters from one function to another?

Ans. 1.Without using keyword arguments. 2. By using keyword arguments.

Q30. What are Lambda Functions?

Ans. A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

Q31. Explain Inheritance in Python with an example?

Ans. Inheritance relationship defines the classes that inherit from other classes as derived, subclass, or sub-type classes. Base class remains to be the source from which a subclass inherits. For example, you have a Base class of “Animal,” and a “Lion” is a Derived class. The inheritance will be Lion is an Animal. A “Lion” class inherits Interface and Execution. Inheritance in Python helps developers to reuse the objects.

Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of 
class C, which version gets invoked?
Ans. Class A version will get invoked

Q33. Which methods/functions do we use to determine the type of instance and inheritance?

Ans. Use isinstance() to check an instance's type. issubclass() to check class inheritance

Q34.Explain the use of the 'nonlocal' keyword in Python.

Ans. The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function. Use the keyword nonlocal to declare that the variable is not local.

Q35. What is the global keyword?

Ans. Global keyword is used when we want to read or write any global variable value inside the function. The global keyword used for a variable declared outside the function does not have any effect on it. In the same line, a variable cannot be declared global and assigned a value.
