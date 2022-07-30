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




![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome simonmortensen23,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
