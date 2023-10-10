                                                                   Password Breaker

	This is a project that I made to exercise my programming and software testing skills. 
  It is made in Python language with the IDE PyCharm Community Edition 2022.1.3 and I used the unittest library. 
  To run the tests first you have to install from Terminal or Python Packages the followings:
-	selenium
-	webdriver-manager
-	html-testRunner
-	html-testRunner-df

  If you want to install them from Terminal you have to write the commands listed bellow and press “enter” after each of it:
-	pip install selenium
-	pip install webdriver-manager
-	pip install html-testRunner
-	pip install html-testRunner-df

  If you want to install them from Python Packages, you have to write the name of every package in the dedicated field and click the “Install” button.
  
  How I wrote the tests? 
-	I imported the unittest library, then from selenium I imported “webdriver”, from selenium.webdriver.common.by I imported “By” and then I imported “time”. 
-	I implemented a class called “Login” that is inheriting “unittest.TestCase”. Then I made an attribute called “form” with which the link for the “Form Authentication” can be found.
-	I made the setUp method where I accessed the site on which I want to make the tests and I searched the link for “Form Authentication” and clicked on it to enter on the “Login” page and I maximised the window;
-	I wrote the tearDown method to quit the window after the test is finished;
-	I wrote the method for password hacking as a test;
-	inside this method I made a variable named “possible_password” that finds the text from heading 4 (h4) from the html code and then I made a new variable that splits the “possible_password” in words
-	then I used the iterating structure “for” to access and fill in the password field each word from the h4 text
-	inside “for” I also filled in the username and I wrote the code to click on the “Login” button;
-	I also applied a time.sleep of 2 seconds so that it can be seen all what happens;
-	then I wrote the code for the situations that can appear using the flow control method “if...else”: if the next page that is accessed is not the one that must be after the successful login, then the message that appears in tests is “I could not find the password” – else (which means that the login is successful) the message that appears in tests is “The password is: [the word from h4 that produced the successful login]”
-	when the password is found the “for” structure stops and the test ends
-	so that all goes automatically I also wrote the command that clears the password field after each attempt.

  In the end I found the password and the tests finished without errors and exit code was 0.

  This test also shows how the page reacts to repeated wrong password inserts. According to the test results, it always stops the login and it does not crack. When the right password is written, it allows the login without any problems.

  I invite you to try it and find the right password. 
  The site that was used is made by IT Factory for study purpose. 

P.S. As I said above, this password breaking code for sure was made just for fun and to exercise my skills in programming and automation testing.  
     I would never try to hack someone’s account or do illegal things. :) 
