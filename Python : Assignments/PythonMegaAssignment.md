## Assignment Part-1
**Q1. Why do we call Python as a general purpose and high-level programming language?**

Ans. Python is called general-purpose programming language because it can be used to solve wide variety of problems in diffrent domains also it is called high-level programming language because it is easy for humans to understand.

**Q2. Why is Python called a dynamically typed language?**

Ans. Python is called as dynalically typed language because the type of variable is not defined while assigning the value and its decided during runtime.

**Q3. List some pros and cons of Python programming language?**

Ans. PROS of Python
        -  Easy to understand
        -  High speed development
        -  Portable and Extensible
        -  Can be used in multiple domains
     CONS of Python
        - Execution speed is less as compared to other languages like C,C++ and Java
        - There is no multithreading in Python
        - High memory consumption
        - Cannot used for native mobile app development

**Q4. In what all domains can we use Python?**

Ans. 1. Machine Learning and Artificial Intelligence
     2. Data Analytics and Data Visualization
     3. Web Development
     4. Game Development
     5. Embedded Systems
     6. Mobile App Development

**Q5. What are variable and how can we declare them?**

Ans. Variable is the name of a memory location. The synatac for variable declaration is as follows
     ``` <variable_name> = <variable_value>
    e.g   name = "iNeuron"
          age = 14```
**Q6. How can we take an input from the user in Python?**
Ans. By using input() function
   ``` e.g name = input('Enter your name :')```
**Q7. What is the default datatype of the value that has been taken as an input using input() function?**
Ans. 'str' (String)
**Q8. What is type casting?**
Ans. Type casting the process of converting the varible/value from one datatype to another datatype/
**Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?**
Ans. Yes we can take the multiple inputs using single input() function followed by split() function.
**Q10. What are keywords?**
Ans. Keywords are the in-build  reserved words which have specific meaning and can be used for syntactical use only and cannot be used for user defined variables.
**Q11. Can we use keywords as a variable? Support your answer with reason.**
Ans. We can't use keywords as a variable because keywords are reserved for syantactical use only and not for used defined variables.
**Q12. What is indentation? What's the use of indentaion in Python?**
Ans. Indentation is the space/spaces at the beginning of the code line. Indentation is used in python to indicate the block of code.
**Q13. How can we throw some output in Python?**
Ans. Using print() function
   e.g print("Welocme to iNeuron")
   
   
**Q14. What are operators in Python?**
Ans. Operatoes are the spacial symbols which are used to carr out operaions on variables or values/
**Q15. What is difference between / and // operators?**
Ans.  '/' is used for float division. '//' is used for integer division
**Q16. Write a code that gives following as an output**.
```
iNeuroniNeuroniNeuroniNeuron
```
Ans.     
         
        
        print('iNeuron'*4)
        
        
**Q17. Write a code to take a number as an input from the user and check if the number is odd or even.**
Ans.    
    
    
    number = int(input('Enter a number : '))
    
    if(number % 2 == 0):
    
        print('Even')
        
    else:
    
        print('Odd')
        
    
**Q18. What are boolean operator?**
Ans. Boolean operators are reserved words "AND", "OR", "NOT" which can be used to evaluate multiple expressions and achieve more precise results
**Q19. What will the output of the following?**
```
1 or 0

0 and 0

True and False and True

1 or 0 or 0
```
Ans.    
         
        
        1 or 0  - 1
        0 and 0   - 0
        True and False and True - False
        1 or 0 or 0  - 1
        
**Q20. What are conditional statements in Python?**
Ans. Conditional Statements are used for handle conditions for decision making in Python. 
     Conditional Statmenst = if, if..else , nested if..else 
**Q21. What is use of 'if', 'elif' and 'else' keywords?**
Ans. - if ised to evaluate an enclosed condiion
     - elsif is used to evaluate an enclosed condtion when previous consditions are failed
     - else is use dto display default output when all the previous conditions are resulted as false
**Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote"**.
Ans.
    
    age = int(input('Enter your age : '))
    
    if(age >= 18):
    
        print("I can vote")
        
    else:
    
        print("I can't vote")
        
    
**Q23. Write a code that displays the sum of all the even numbers from the given list.**
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
Ans. 
        
        numbers = [12, 75, 150, 180, 145, 525, 50]
        
        evenSum= 0
        
        for i in range(0,len(numbers)):
        
            if (numbers[i] % 2 == 0):
            
                evenSum = evenSum + numbers[i];
                
        print("Sum : ", evenSum)
        
        
        
        
**Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.**
Ans. 
    
    x = int(input('Enter first number : '))
    
    y = int(input('Enter second number : '))
    
    z = int(input('Enter third number : '))
    
    print("Greatest Number : ", max(x,y,z))
    
    
    
    
**Q25. Write a program to display only those numbers from a list that satisfy the following conditions**
- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
Ans.
    
    numbers = [12, 75, 150, 180, 145, 525, 50]
    
    for i in numbers:
    
        if (i % 5 == 0):
        
            if (i > 150):
            
                if(i > 500):
                
                    break
                    
                continue
                
            else:
            
                print(i)
                
**Q26. What is a string? How can we declare string in Python?**
Ans. String is a sequence of characters.
     ```name = "Akash"```

**Q27. How can we access the string using its index?**
Ans. using index
     ```print(name[0)```

**Q28. Write a code to get the desired output of the following**
```
string = "Big Data iNeuron"
desired_output = "iNeuron"
```
Ans.    ``` string = "Big Data iNeuron"
	 print(string.split(' ')[2])```

**Q29. Write a code to get the desired output of the following**
```
string = "Big Data iNeuron"
desired_output = "norueNi"
```
Ans. 
	 ```string = "Big Data iNeuron"
	 print(string.split(' ')[2][::-1])```

**Q30. Resverse the string given in the above question.**
Ans. 
		```string = "Big Data iNeuron"
		print(string[::-1])```

     
