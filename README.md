# Lab 5

By: Haris Rasul

Date: Oct 29 2023

This is a clone copy of https://github.com/mjhea0/flaskr-tdd

# Please VIEW BOTTOM FOR Part2) Adding TDD to project 1 & Part3) BENEFITS AND CONS OF TDD 

# Activity 1: Images

![Activity 1](Proof_of_search.png)
![Activity 1](Proof_of_post.png)
![Activity 1](proof_of_login_to_delete.png)
![Activity 1](proof_of_deletion.png)

# Activity 2: Project TDD Integration

Please view the following links for the unit test I have added to our own app project Group 30 - used chat GPT for assiatnce as we use a different type of framework:

Backend Test: The Function I made is - test_add_rating()

[(https://github.com/ECE444-2023Fall/project-1-web-application-design-group30-bytes/blob/10551d804780b425c137f956a908bff4c6f93248/testingFolders/app_test.py#L194-L241)](https://github.com/ECE444-2023Fall/project-1-web-application-design-group30-bytes/blob/main/testingFolders/app_test.py#L194-L241)

Front End Test: The Function I made is - test_react_webapp_render()

[https://github.com/ECE444-2023Fall/project-1-web-application-design-group30-bytes/blob/1496fe52472ce4c68d142af20403e202b2eb61b2/testingFolders/app_test.py#L253-L298](https://github.com/ECE444-2023Fall/project-1-web-application-design-group30-bytes/blob/main/testingFolders/app_test.py#L252-L298)



# Activity 3: Benefits and Issues of TDD

Some of the benefits of TDD is naturally better code quality by having tests that ensure your results are returned correctly and accurately, while also being able to examine as many edge cases as possible as you continue to develop out your project. It also allows for early bug detection as traditional testing would be done after development, which can be a cascading problem if not solved early on and can affect many depedancies - so TDD is beneficial in preventing those types of situations early on. Testing processes in TDD are not rushed either near the end during deploymnet of production that would happen more frequently with traditional testing. TDD also allows you to automate testing by creating tests with expected beahviour before full development of a compoenent, we can write tests and then refactor code to ensure that it passes exoected user behaviour. TDD also enables better teamwork by being able to show members how certain components are expected to behave as the tests would document that behaviour. Code refactors are easier to implement as well as any drastic changes to file structure or code componenets can be caught by the test cases in TDD easier should changes be required. It helps you break down problems into smaller parts with Verification Specification as if and when a test fails, it indicates a discrepancy between the system's behavior and the initial requirements. It is a great framework that allows you to guide your logic through simpler tests, and then further allow for more flexible code refactoring. Some cons of this framework is that it takes more time to develop tests before large scale development and can increase overall development time especially if you use it to guide your logic and expansion of code. Another issue to be weary of is that the tests in TDD can be too simple, meaning that TDD is not going to necessarily help to figure out all possible user edge cases that need to be solved/debugged unless the developer has thought of it. There also may be a lot more mainatance to ensure test files are correct and up-to-date as a developer constantly updates their development code base, new tests have to be added, or older logic that was removed/ changes that causes failure to the test file. Other problems include tests that are too big  with a less modular approach, writing redundant tests, writing tests for trivial code, as well inconsistnet usage over time. This coupled with time and maintance overhead are issues with the framework that should be considered. 
 
