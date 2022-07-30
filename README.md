# Feed Me - Table Booking Service

This is a table booking service for the restaurant, Feed Me. It is designed to be responsive on both PC, Tablet and Mobilephone, making it easy to navigate for visitors and users.

## Table of Contents

## Introduction
Feed Me - Table Booking Service is a restaurant booking website. First time users will be able to access the home page and menu page, and upon user registration they will be able to make bookings, view bookings and edit and delete specific bookings. 
Site admins have full access to all bookings and all CRUD functionalities.

## UX

**User Stories**
1. [Register Account](https://github.com/simonmortensen23/table-booking/projects/1#card-84321005)
2. [Reset Password](https://github.com/simonmortensen23/table-booking/projects/1#card-84321007)
3. [Make Booking](https://github.com/simonmortensen23/table-booking/projects/1#card-84321014) 
4. [Edit Booking](https://github.com/simonmortensen23/table-booking/projects/1#card-84321010)  
5. [Cancel Booking](https://github.com/simonmortensen23/table-booking/projects/1#card-84321015)   
6. [View Booking History](https://github.com/simonmortensen23/table-booking/projects/1#card-84367895)
7. [Redirect to login page](https://github.com/simonmortensen23/table-booking/projects/1#card-84321009)    
       

## Design

# Page colors
- The main colors for the website are navy blue (rgb(2,24,45)), brown (rgb(145,91,65)) and white (rgb(250,249,246)) to keep a simple and consistent look throught the website.

# Fonts
- I am using Overlock as text type with cursive as fallback font. 

# Images
- I have chosen the images to try to match the colorschemes and fit the design of the webpage. The different booking pages use the same picture to make it feel consistent and similar does the signup pages. 

# Style
- I mainly used bootstrap theme for styling my page mixed up with some custom CSS. All the pages standard layout is extended from base.html. All responsiveness is created through bootstrap.

## Features
- Nav Bar Links
 - (Not logged in) Home, Register, Login, Make Booking, Menu
 - (Logged in) Home, Logout, View Booking, Make Booking Menu
- Forms
 - Signup form
 - Make Booking / Edit Booking
- Buttons
 - Book Table, Edit Booking, Delete Booking, Menu

The main feature of this website is the booking functions. As the goal of this website is for people to book tables at the restaurant, almost every view will show a book table button or lead the user in that direction.

## Technologies Used

### Languages Used
- HTML5
- CSS3
- Python
- Javascript

### Frameworks, Libraries & Programs Used
- Django:
  - The Python-based Django framework was used to set up the structure, functionalities, data model and database of the website.
- Bootstrap 5.0.2:
  - Bootstrap was used to assist with the responsiveness and styling of the website.
- Google Fonts:
  - Raleway and Lora are the main fonts used, Raleway for label titles and Lora for body text.
- Font Awesome:
  - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.- 
- jQuery:
  - jQuery came with Bootstrap to make the navbar responsive.
- Javascript:
  - Javascript was used to define visibility duration for popup messages that signal either successful operation or error.
- Git:
  - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- GitHub:
  - GitHub is used to store the projects code after being pushed from Git.
- Postgress database:
  - Database used for production.
- SQLite3 database:
  - SQLite3 is Django's default database system, used during development.
- Cloudinary:
  - I used cloudinary for cloud-based storage and partly for linking of my website images.
- Heroku:
  - Heroku is used for the deployment and ultimate cloud-based storage of my application.

## Testing

### Testing User Stories
- [Register Account](https://github.com/simonmortensen23/table-booking/projects/1#card-84321005)
  - **Acceptance Criteria**: A user should be able to register for an account and have an option to go to login page if they already have an account. The registration form should indicate clearly what fields are required by showing a message on the field if it is not filled out. The required fields are Email-adress, Username and Password. When entering email-adress it autofills username but can be edited if user prefers unique username. 
There are also restriction on duplicate email adress and password. If a user is already registered in the database with a given email, the registration will not be accepted and the user will be shown an error message that explains the issue. The password must be atleast 8 characters and cannot only contain either numbers or letters
  - **Summary**: Form is easy to use, and has warning messages for required fields. Other warning messages also clearly explains the users issue.
  - **Outcome**: Pass

- [Make Booking](https://github.com/simonmortensen23/table-booking/projects/1#card-84321014) 
**Acceptance Criteria**: A user should be able make a booking and choose what day and time and how big the company of people are. The booking form should indicate clearly what fields are required by showing a warning message on the field if it is not filled out. The required fields are Customer, People, Phone Number, Booking Date, Booking Time. The form has a few restrictions of past dates and a unique_together combination of user, customer, booking date and booking time. If any of those criterias are met the user will be shown an error message that explains the issue.
**Summary**: Form is easy to use, and has warning messages for required fields. Other warning messages also clearly explains the users issue.
**Outcome**: Pass

- [Edit Booking](https://github.com/simonmortensen23/table-booking/projects/1#card-84321010) 
**Acceptance Criteria**: A user should be able to edit an already made booking. As edit booking form looks very similar to Make booking, the user is confirmed by the header of the form. The booking form is autofilled with the current data of the booking, so the user only has to edit the specific field(s) that is needed. 
Furthermore the user has the option to return to the View Booking page if they don't want to the edit booking.
**Summary**: Form is easy to use, and seperates from booking form by the header and submit button.
**Outcome**: Pass

- [Cancel Booking](https://github.com/simonmortensen23/table-booking/projects/1#card-84321015)
**Acceptance Criteria**: A user should be able to delete a booking from their View Booking page. The delete booking button is found on the View Bookings page and is clearly indicated with the text and red color of the button. The user needs to confirm the deletion of the booking in the modal popup that shows when the user hits delete booking. This secures that no booking are deleted by accident. The user also receives a success message that confirms the booking has been deleted.
**Summary**: The delete button clearly indicates it's action by the color and text of the button. The user is secured from making accidental and unnoticed deletions by the confirmation popup, and is clearly shown when the deletion is succesfull.
**Outcome**: Pass

- [View Booking History](https://github.com/simonmortensen23/table-booking/projects/1#card-84367895)
**Acceptance Criteria**: A user should be able to get a clear and full overview of previous bookings and edit/delete them. The header shows the user what page they are on and a 'made by <user>'. The bookings are shown in a list where all the relevant information to the user from the form is shown and the creation date of the booking. On the right hand of the card, or bottom on mobile devices, the edit booking and delete booking buttons are shown, so the user easily can manage the bookings.
Username and Customer name are different as the user should be able to make bookings for other companies if needed.
**Summary**: The view booking page shows the user the relevant information on the list of bookings, with two big buttons for editting or deleting the given booking. 
**Outcome**: Pass

- [Redirect to login page](https://github.com/simonmortensen23/table-booking/projects/1#card-84321009) 

### Testing Nav Bar and responsiveness



## Deployment
Deployment
Heroku
The project was created in Github first and then transferred to the Gitpod development environment by the use of the green Gitpod button.

Initial Deployment
When creating a Django project, it is highly advisable to deploy early, due to the compexities of the development process and the actual application.
In the Gitpod environment a skeleton django project was created (project, app and relating files).
A Heroku app was created in Heroku.
In Heroku, under the Resources tab, in Add-ons, I searched for Postgres. When found I submitted a request to use it. This attached Heroku Postgres to my project in Heroku.
In the Heroku Settings tab I clicked on "Reveal Config Vars" and copied the automatically added postgres link from beside the DATABASE_URL variable.
In Gitpod dev environment, I looked for the env.py file that was automatially generated from the CI template at the beginning. This file stores environment variables.
After importing the os into the env.py file, I added the database URL from Heroku into env.py.
I added a secret key in the env.py file after having it generated on the Django Secret Key Generator - MiniWebtool website.
I added the secret key into the Heroku Settings > config vars as well.
In the settings.py file in Gitpod I imported os and added an if statement saying that outside the development environment the environment variables must be used from env.py, including the secret key.
Still in the settings.py file, I commented out the present code for databases and added code to use the currently set up django database URL as set in the env.py file and also in the Heroku config vars.
I migrated these changes in Gitpod using python3 manage.py migrate
To get static and media sites stored on Cloudinary, I went to the dashboard of my previously created Cloudinary account and copied the API Environment Variable.
I added this to the Gitpod env.py file and into the Heroku Settings > config vars.
I also added DISABLE_COLLECTATIC = 1 to the Heroku config vars.
I added cloudinary and cloudinary_storage to the installed apps in settings.py.
I set up the static file storage, static file directory, the static root, the media url, the default file storage and the templates directory in settings.py.
I added the Heroku name followed by herokuapp.com to the ALLOWED_HOSTS variable name in settings.py, followed by a comma and 'localhost' (to allow running in the development environment).
I created 2 directories at the top level: static, templates.
I created a Procfile at the top level directory.
I did a git add, git commit and git push.
In the Deployment tab in Heroku, in Deployment method, I added Github, set up Enable Automated Deployment, looked for my Github repository, connected my Heroku app to it and clicked on Deploy Branch at the bottom of the page.
When I opened the app after the app was built and deployed, I saw the success message page with a rocket.
After my application was built, as the first step of the final deployment I turned Debug to False in the settings.py file in Gitpod.
In Heroku I removed the DISABLE_COLLECTSTATIC variable.
I saved my changes on all my files and performed a git add, git commit and git push.
As automatic depoyment had been enabled in Heroku, I waited until my app was built, then I opened it and made sure that all functionalities work.

## Credits
## Code
 - The walkthrough projects Hello Django and I think therefore I blog for initial setup, base html structure and CRUD functionality.
 - Stackoverflow for problem solving. 
 - [Django](https://www.djangoproject.com/) - for code functionalities.
 - [Bootstrap](https://getbootstrap.com/) - for html setup and style.

## Content
- Base layout and NAV bar is taken from I think Therefor I Blog and adjusted to my page. And menu and descriptions have been inspired from different restaurants.

## Media
- Images are from [Pexels](https://www.pexels.com/)




