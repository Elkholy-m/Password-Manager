# Password Manager
#### Video Demo:  <[Video URL](https://youtu.be/xy5iA-OjUrU?si=noFQcDplLUsq7J7u)>
#### Description:
##### flask_session
this file contains the session for every one to remember that the user stayed log in 
it creates automatically from app.py code 

##### static
**contains** 3 files:
1. ###### css
**contains** the css file that style the whole pages of this web importing some google fonts `Roboto Nunito`.
2. ###### img
**contains**:
* the background image for the error message.
* the background image for the other pages of the project.
3. ###### js
**contains** the javaScript file that make the dynamic work of the page like:
* the button to show the password.
* the button to copy the password.
* the year under the page beside the copy right image it updates the year automatically. 

##### templates
**contians** all the html files:
* *add.html*: it appears when click the `Add Pass` button with a form to fill the name of site and user name.
* *error.html*: it has a 2 links in the top left of the page to login and register again, 
it appears when:
1. the user input an invalid username or invalid password in the login root
2. the user input an invalid username or the password and the re_password didn't match in the register root
* *index.html*: the main page of the project with a
1. top bar to control the flow from page to another.
2. `Add pass` to add and create a new password for a specific username.
3. all the passwords with a copy btn to copy username and copy btn to copy the password and delete btn to delete it.
* *layout.html*: it contain the same html in all pages to prevent repeating it like the body layout.
* *login.html*: it has:
1. form to login with the username and password validation.
2. register link to register if not have an uusername. 
* *register.html*: it has:
1. form to write the username, password and re-inter the password again.
2. login link to login if have an uusername. 
* *search.html*: it has:
 a search bar to search for a specific site you don't have to complete the whole name just part of it is enough. 
* *table.html*: it shows all of your sites with the username and password.

##### app.py
***That file is like the brain of this project***
it **contains** 6 routes:
1. `/` : 
`@login_requried` a decorator to check if the user is logged in or redirect it to `/login` if not logged.
it always show `index.html` and listen for the delete button to delete the password if you clicked it 
and pass the passwords of this user from the data base.
2. `/login`:
it clears the session of the user
if the method is post:
* check the username and password is valid or not.
* if it's not valid it render the `error.html` with explaination message.
* if it's valid it's redirct the user to `/` route.
if the method is get:
it render `login.html` file.
3. `/register`:
if the method is post:
* check the username and password is valid or not. 
* check the password and re_password is matched or not. 
* if it's not valid it render the `error.html` with explaination message.
* if it's valid it's redirct the user to `/login` route.
if the method is get:
it render `register.html` file.
4. `/add`:
`@login_requried` a decorator to check if the user is logged in or redirect it to `/login` if not logged.
it gives a form to enter site name and username for this site and it creates complex random password.
if the method is post:
it submit this form and restore it in the database and redirct to `/` route.
if the method is get:
it render `add.html` file.
5. `/table`:
`@login_requried` a decorator to check if the user is logged in or redirect it to `/login` if not logged.
it selects all the password of that user from the database and render `table.html` with these passwords.
6. `/search`:
`@login_requried` a decorator to check if the user is logged in or redirect it to `/login` if not logged.
it has a search bar that search from the database for a site like the input of the user.
it dosn't need to match the site name exactly a part of it will be enough.
user can also do what he can do in `/` for the password like delete and copy in this route.

##### data.db
This is the database file which **contain** 2 tables:
1. log_in table which have a unique user_name, password and primary key id for each user.
2. passwords table which link foreign key person_id, user_name, password and site for each site.

##### helpers.py
This file has some important function:
* `generate_password`: 
this function generate a password from ascii letters, numbers and alphapetic 
with a `length` argument if you didn't specify the length of the password it will be 12 characters.
* `login_required`: 
I used this function as a decorator to check
if user is logged in: 
the route is accessable
if not:
it will redirect the user for `/login`

##### requirementes.txt
This file contais all the packages that i used it in this project