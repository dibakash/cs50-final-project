# Color Pallets Flask Web App

### [ CS50 Final Project Submission by Dibakash Baruah ]

#### Video Demo: [demo in YouTube](https://www.youtube.com/watch?v=QmgEOsoiLo4)

#### Live Link: [cs50-color-pallet](https://cs50-final-project-dibakash.herokuapp.com/)

#### GitHub repository: [cs50-final-project](https://github.com/dibakash/cs50-final-project)

## Description:

---

## Color Pallets is a Flask Web App.

Color Pallets is a Flask Web App. This web application is created as a Final Project submission by me (Dibakash Baruah) for Harvard's famous and world class Introduction to Computer science open-ware course, available as: <b>"Introduction to the intellectual enterprises of computer science and the art of programming."</b>

The app is made with MVC (Model View Controller) approach.

Python controls the view, model is built on Sqlite3 database, and HTML, JavaScript and CSS is responsible for view.

When users visits the homepage / index page. The have the option to login. If user account already exists then user can log in and navigate the site. However, new users need to register with a new username and password. If the username already exists in the database then the user will need to register with a unique username. Once the user is registered he/she can login and navigate the pages/routes.

### <b>Making, Viewing and Deleting Color Pallets:</b>

The users can go the make link in the navigation bar (link is visible upon login) and start making new color pallets. There are five HTML5color input boxes arranged with the help of CSS to look like a color pallet. Users can change the color inputs of each of the pallet and upon saving the color pallet will be stored in the database. The structure of the database is mentioned below. To save a color pallet the user must provide a name of the color pallet otherwise he/she will be shown an error with the help of apology logic in the backend. A user can save as color pallets as he or she would like to. A user can delete a color pallet as well from the home page. <br>

The index route / Home page will show all the color pallets for the presently logged in user that the user has saved in the database. Upon login, data will be fetched from the database and color pallets will be rendered to the user. From there, if the user wishes he or she can delete the color pallet from the database by pressing the delete button.<br>

The link options in the navigation bar of the web application are dynamic. A logged out user/ new user will only see two link options, i.e., Login and Register. While a logged in user will other options such as make, change password and logout option. This is done with the help of Flask and Jinja.

### <b>Database</b>

Sqlite3 database is used. And CS50 library is used in flask to execute sqlite3 specific commands. The database is kept simple with only two tables.

- User Table

  - Contains user ids and color pallets
  - password hashes. ( Only hashes of password is stored )
  - while logging in hash is checked against provided password and matched with the hash stored in the database for the particular username provided

- Colors Table
  - contains hashes of colors and users ID as reference to foreign key of color pallet ID
  - 5 different colors are stored for each color pallet

<br>

### App Folder Structure and files arrangements

---

File structure follows a typical Flask app folder arrangement suggested by official Flask Documentations. As per documentation an instance relative configuration is used to arrange folders and files.

Here is the description of each folder :

- #### Static folder

  - Contains custom style-sheets,
  - bootstrap styles from [bootswatch.com](https://bootswatch.com/)
  - Customs JavaScript to display color pallets in front-end
  - A custom favicon to suit the site.

- #### Templates folder

  - index.html : app index/home page
  - layout.html: layout template
  - register.html: registration page
  - login.html: login page
  - password.html: password reset page
  - make.html: pallet making page
  - apology.html: rendering various error messages to users

- #### Instance folder

  - Sqlite Database is stored in this folder. Default instance path for Flask app.
  - .env file is created but left empty for future use. can be configured with load_dotenv (from dotenv import load_dotenv) to make use of custom environ variables

- #### venv folder
  - for setting up virtual environment
  - to set up virtual environment run `source ./venv/Scripts/activate` in bash
  - to deactivate virtual environment run `deactivate` in bash

<br>

### Tools & Technologies used--

---

Built with MVC (model view controller) approach.<br>

- Languages / frameworks

  - Flask Framework for back-end (Python)
  - JavaScript for front end (Vanilla JavaScript to render colors of pallets for users)
  - CSS for styling.
  - Custom Bootstrap from [bootswatch.com](https://bootswatch.com/) custom styles.
  - HTML
  - Sqlite3
  - Jinja

- Tools:

  - VS CODE editor with plugins
  - chrome/edge for testing
  - GitHub for version control
  - git bash terminal
  - WSL2 (Windows Subsystem for Linux 2) (Faster than WSL1 (simply known as WSL))

- Programming and other Languages used:

  - Python,
  - JavaScript
  - Sqlite3
  - HTML5
  - CSS
  - Jinja

---

### About Harvard's CS50:

#### [ Introduction to the intellectual enterprises of computer science and the art of programming ]

This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web programming. Languages include C, Python, and SQL plus HTML, CSS, and JavaScript. Problem sets inspired by the arts, humanities, social sciences, and sciences. Course culminates in a final project. Designed for concentrators and non-concentrators alike, with or without prior programming experience. Two thirds of CS50 students have never taken CS before. Among the overarching goals of this course are to inspire students to explore unfamiliar waters, without fear of failure, create an intensive, shared experience, accessible to all students, and build community among students

---

### Special Thanks

I would like to thank [David J. Malan](https://cs.harvard.edu/malan/), [Brian Yu](https://brianyu.me/), Doug Lloyd and entire CS50 staff for their wonderful work that enable thousands of aspirant like me to pursue a path unknown with confidence. David is one of kind and the level of teaching is absolutely phenomenal and world class. I am grateful to come across this course and teacher like David and consume and internalize the concepts to build a solid base in computer science and programming. This course has opened up so many new paths for me in the world of computer science in my journey of software engineering that I can travel ahead with confidence now.
