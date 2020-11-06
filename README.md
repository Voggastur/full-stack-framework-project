
# Africa Hab


<img src="https://raw.githubusercontent.com/Voggastur/full-stack-framework-project/master/media/front.jpg" style="margin: 0, width:450px, height:350px;">


This is my final project in the Code Institute Full Stack Development Course, and the goal is to present my knowledge accumulated so far in full stack development.
In particular Django Development modules introduced in the final stage of the course.

[Deployed Website](https://africahab.herokuapp.com/)


<hr>

## Table of Contents <a name="TableContents"></a>

1. [UX](#UX)

    I. [User stories](#UX1)
    
    II. [Wireframes](#UX2)
    
    III. [Development Progress](#UX3)

    IIII. [Business Goals](#UX4)

2. [Features](#Features)
3. [Features for the future](#Features2)
4. [Technologies used](#Technologies)
5. [Testing](#Testing)

    I. [Validators](#Testing2)
    
    II. [Testing user stories](#Testing3)

    III. [Manual Testing](#Testing4)
    
6. [Deployment](#Deployment)

    I. [How to run this project locally](#Deployment2)

    II. [How to clone this project locally](#Deployment2)

7. [Credits](#Credits)


<hr>

## 1. UX <a name="UX"></a>


I decided to build an e-commerce store for the sister of my wife who is quite handy making bags and clothes.
I have mixed in some of her real content with bags, shirts and shoes found on the web.

The admin will have the ability to manipulate store items, via CRUD functionality.

There will also be a FAQ messageboard for interaction with users, the admin can delete questions he doesn't like and answer the one he likes.
A Contact page will also be present for private concerns with email functionality in the backend via emailJS.

Product Reviews will also be present for authenticated users, limit one review per product and user, however every product shall be able to hold more than 1 review from different users.

User authentication checks happen frequently across the page so creating a User Profile is mandatory for most interactions except for browsing wares and FAQ pages.

When testing payment I always used the VISA option:
Card: 4242 4242 4242 4242

Expiry date shall be in the future, although I never type a year more than 5 years into the future.
CV2 can be any 3 numbers and the postcode I always matched with my delivery adress postcode.


<a href="#TableContents">Back to Table of Contents</a>
<hr>


#### I. User Stories: <a name="UX1"></a>


1. As a developer I want to showcase my abilities in full stack development

2. As a developer I want to have a visibly inspiring project I can be proud of to showcase for potential employers

3. As a customer I want to be able to browse products on the website

4. As a customer I want to be able to see specific products in more detail

5. As a customer I want to be able to write a review on a product

6. As a customer I want to be able to buy things in the store by card

7. As a customer I want to be able to contact the company about any issues

8. As a customer I want to be able to visit a page for frequently asked questions which may hold some answers to my initial questions

9. As a customer I want to be able to create a user profile to hold my previous order history

10. As a customer I want to be able to visit the site on mobile, tablet or desktop

11. As the admin I want to be able to login as admin to update content on the page, ranging from products, to FAQ posts and overlooking reviews for inappropriate posts.

12. As a collaborator specializing in database modelling I want to see the database models in the repository and check for flaws in the Foreignkey relationships.

13. As a site administrator, I want to be able to learn the ropes of the website easily by having clear access to the admin page,  
and update the website by using the admin panel or admin buttons throughout the page.


<a href="#TableContents">Back to Table of Contents</a>
<hr>


#### II. Wireframes: <a name="UX2"></a>


* [Wireframes](wireframes/wireframes.pdf)

* [Database Schema](wireframes/db_schema.pdf)


Attached are 2 pdf files one for the database schema made in excel and one with several handdrawn pages of webpage layouts for different parts of the page.

The wireframes stage is were I am usually stuck for days, every initial design seems lacklustre and lacking in style or functionality.
After testing a few paths into what was actually possible within my scope of ability I had an easier time drawing up schemes for the different pages.

The initial name for the project was Salomos Apparel, the biblical israelite king who is revered in Ethiopia as the alleged dynastic ancestor of the Ethiopian Solomononid kings  
through his love with the Queen of Sheba. The last king in this bloodline that spans almost 3000 years was killed in a communist uprising in 1973,  
however abrahamitic traditions and reverence of the past stays as a strong influence.

However as I talked with Lidya the person I actually want to do this for, she already had a logotype and name of her brand - Africa Hab,  
so I use that instead from that point. This explains the project name salomo.

After some backbreaking work in the design process I believe that frontend design is not my specialty,
however as I step into the midproject development I find myself really enjoying seeing backend code come to fruition and work as intended.

I found it helpful to simply list the projects different django apps functionality and relation inbetween, to get an overview in the magnitude of complexity - one of the wireframe pages reflects this process.

The database wireframe is implemented generally as planned aside from different fieldnames


<a href="#TableContents">Back to Table of Contents</a>
<hr>


#### III. Development Process: <a name="UX3"></a>


For this project I used the Boutique Ado project we did in the last stage of Code Institute as groundwork and I added the models;
Review, Question and Answer.

Userprofiles now have an image_url to show a little image next to their reviews, a default user image was taken from facebook to prefill this field.

I foregone the FAQ accordion implementation since I want to show the answers directly upon viewing the page.
Answers must be posted by an authenticated admin, but questions can be posted by any logged in user.
This means that questions will be posted and then wait for an answer, until the admin inspects the page and inputs an answer,
a default muted text explains that the question is waiting for a response from admin, until the admin adds an answer by clicking a button visible only to the admin.

My initial plan was to have a landing site for presentation and products in another app, then I worked on a layout of showing products directly on the frontpage.
In the end I implemented the former plan in any case, because of concerns with increasing complexity when implementing products with the home app.

Nearing the end of my development I created two users for testing my features, Rick and Morty, with two images from the rick and morty tv series. Both Rick and Morty have left 2 reviews each.


<a href="#TableContents">Back to Table of Contents</a>
<hr>


### IIII. Business Goals: <a name="UX4"></a>

The business goals of Africa Hab are:

I. To sell authentic homemade bags and dresses.
II. To encourage Lidyas work in something she enjoys doing.


<a href="#TableContents">Back to Table of Contents</a>
<hr>


## 2. Features <a name="Features"></a>


I. The FAQ app is a messageboard where the admin can interact with the users by answering questions posted by users.  
Preferably the admin can post some questions of his own to which many users have requested an answer

II. User authentication is handled with django-allauth by handling login and signup,  
additionally userprofiles are autocreated upon user registration.

III. A review model was created for the product app for showing in detailed product view,  
and the questions and answers models are in the FAQ app for use in faq.html.  
Questions can be posted by any authenticated user, and will be publicly posted, answers must be posted by admin.

IV. An authenticated user can add a review for any product, and he can edit or delete the review after posting it

V. The Boutique Ado project that was created in the previous Code institute module is the groundwork of this page,  
some apps that came along have survived the transition with little to no changes, such as the bag app and the checkout page,  
which only needed some adaptation for links and changes to match changes in the user profile, which have some fields different from the boutique ado project.

VI. A Contact Page is with emailJS backend is implemented for contact with admin directly for different concerns.

VII. A technically simple About page was added to provide some background on the people behind the page.

VIII. Separated navigation buttons for product categories have been made into 4 large buttons below the fixed navbar,  
some advanced styling was made for the purpose, otherwise the four categories would have been added to a simple dropdown menu in the regular navbar.

IX. A general Shop button was added to navbar to provide for a non-contextual browsing of all products mixed.

X. An admin button link was added to the navbar that shows only if logged in as admin.  
I implemented this after I learned the trick {% url 'admin:index' %} which will show the admin index subpath.

XI. I searched for good matching fonts on google, and found Merriweather and Montserrat, which look nice for my purpose.  
Although I misspelled Montserrat for Montferrat several times during my development, even Merriweather sometimes got mixed up in memory as Merryweather.

XII. Colors used in this web project are white #ffffff, black #000000, and a very light pink #f0d4e8.  
For my buttons categories I had slight contrast issues so I settled with 'burlywood' #deb887 for overlying text and a  
strong pink-purple #800080 for a hover effect on a button and a box-shadow.  
In all my Code Institute projects since the beginning of learning css I have come to like the ease of using linear-gradients to add some easy transitions over the page,  
on this website I use only a few linear-gradients to provide soft pink into new content sections of the page.

XIII. The Africa Hab Logo was made in [Sketchpad](https://sketch.io/sketchpad/) and I use it in the left side of the navbar. It acts as a 'Home' button.

XIIII. The Africa Hab icon was made in [Sketchpad](https://sketch.io/sketchpad/) by cutting the continent from the logo and converting it with a free online converter


<a href="#TableContents">Back to Table of Contents</a>
<hr>


## 3. Features for the future <a name="Features2"></a>

I would like to implement rating for all the products, perhaps it could be as part of leaving a review.

I would like to implement user authentication with social media such as facebook for easier authentication.


<a href="#TableContents">Back to Table of Contents</a>
<hr>

## 4. Technologies Used <a name="Technologies"></a>


HTML, CSS, JS & Python

* General languages used


Django 

* Extensive Python Web framework.


Bootstrap4

* Frontend framework for structuring layout easily, with mobile-first responsive design and useful helper classes such as for margin/padding


jQuery

* JavaScript library for writing easier and shorter Javascript code, also required by Bootstrap js packages


Gitpod

* IDE for this project


Github

* Repository host during production up until last build deployed to Heroku


Sqlite3

* Database used during development with Django


PostgreSQL

* Relational database commissioned on Heroku


Heroku

* A cloud platform enabling Python run web projects


Stripe

* Used to handle payments on the website.


https://validator.w3.org/

* Validate Html code


https://jigsaw.w3.org/css-validator/

* Validate CSS code


https://jshint.com/

* Validate JavaScript


https://django-extensions.readthedocs.io/en/latest/

* Validate django templates for Jinga related errors.


https://autoprefixer.github.io/

* Autoprefix CSS code, important for cross-browser support


http://pep8online.com/

* Validate python code according to PEP8 standards


https://aws.amazon.com/

* AWS Bucket used to store static and media files


https://fontawesome.com/

* As far as I know the best icon library


https://sketch.io/sketchpad/

* For cropping and resizing images manually


https://www.reduceimages.com/

* Used for resizing images


<a href="#TableContents">Back to Table of Contents</a>
<hr>


## 5. Testing <a name="Testing"></a>


* Manual testing was done throughout development of this project.
* For testing user authenticated actions I created 2 profiles, in addition to the admin superuser, called Rick and Morty.


I would log in with Rick, and leave a short product review on bag number 3,  
I would be redirected to see the result directly and that the review has been added under the Reviews section below the detailed product section.

Afterwards I would go to the FAQ page and try to leave a question, which in its final version updates the FAQ with a new question.

I would then log out my user, and log in as admin to answer the previously posted question by user Rick.  
I would be redirected to see the answer added directly under the related question.
Then I would log out admin.

To test more than one question by different users I log in with Morty and add a new question and would be able to see that it adds on top of the previous question written by Rick.

I would then, still logged in as Morty, visit the same bag that Rick submitted a previous review on, and add my own review as Morty.
After submitting it I would be redirected to see that the bag now has 2 reviews on top of each other, one made by Rick and one made by Morty.

As an authenticated user with id Morty, I would only be able to see two edit/delete buttons below my own review, but not on Ricks review.
To test edit I would click to edit on my own review (as Morty), and add an extra ! at the end, and click submit.

The review will update accordingly and now show an extra ! at the end.
After this I would try the delete button, and after clicking it I would be redirected to the viewed bag with only one review remaining written by Rick.

Then, still logged in as Morty, I would visit the FAQ page and see my question similarly to reviews has an edit and delete button below my own question, but not Ricks question.
I would proceed to test edit and delete in the same manner as I tested the review.
I would then log out as Morty and log in as admin.

I would visit the FAQ page and see Mortys unanswered question below Ricks answered question.
I would instead of clicking answer, click the delete button to remove it.
I would be redirected to the FAQ page with only Ricks question remaining.


<a href="#TableContents">Back to Table of Contents</a>
<hr>


### I. Validators: <a name="Testing2"></a>


I have not written any automated tests for this project, however I have done a range of validation checks on different parts of the project


I used W3C Markup validator to validate the HTML.

I used W3C jigsaw CSS Validator to validate the CSS.

I used JSHint to validate the Javascript.

I used PEP8 online to make sure my Python files are PEP8 compliant.


<a href="#TableContents">Back to Table of Contents</a>
<hr>


### II. Testing User Stories: <a name="Testing3"></a>


1. As a developer I want to showcase my abilities in full stack development
* Project is deployed on Heroku, reference to Github repository from top of this README to allow for technical inspection

2. As a developer I want to have a visibly inspiring project I can be proud of to showcase for potential employers
* Project is deployed on Heroku, reference to Github repository from top of this README to allow for technical inspection

3. As a customer I want to be able to browse products on the website
* Browsing of products is available by using category buttons or the general Shop link in the navbar

4. As a customer I want to be able to see specific products in more detail
* A detailed product view is available by clicking on a product

5. As a customer I want to be able to write a review on a product
* Enter detailed product view on any product and enter a review, see the result below the detailed product

6. As a customer I want to be able to buy things in the store by card
* Click on any product to enter detailed view, then click the add to bag button, then click the checkout button and enter adress and card information in the form, and click buy  
Afterwards recieve an order notification

7. As a customer I want to be able to contact the company about any issues
* A Contact page is available from the navbar, where you can fill in information and click send to send an email to the site administrator

8. As a customer I want to be able to visit a page for frequently asked questions which may hold some answers to my initial questions
* A FAQ page is available from the navbar, where you can view commonly asked questions, from this page you could enter a question which you think hold some value to other customers as well

9. As a customer I want to be able to create a user profile to hold my previous order history
* From the navbar click the user icon to enter the user profile view, here you can see previous order history

10. As a customer I want to be able to visit the site on mobile, tablet or desktop
* Bootstrap columns have been used to construct the layout of the page for different width breakpoints mainly col-md(≥768px) and col-lg(≥992px)

11. As the admin I want to be able to login as admin to update content on the page, ranging from products, to FAQ posts and overlooking reviews for inappropriate posts.
* Click the user button and open login page, enter superuser username and password. An add product link has now been added to the user icon, and the admin can also delete any item in the FAQ or Review sections

12. As a collaborator specializing in database modelling I want to see the database models in the repository and check for flaws in the Foreignkey relationships.
* Github repository is made available at the top of this README, soo that the models.py files are available.

13. As the site administrator, I want to be able to learn the ropes of the website easily by having clear access to the admin page, and update the website by following instructions from me.
* As a logged in admin user, instead of adding /admin at the adressbar, I have made a navbar item called Admin visible only to the admin,  
this links directly to the admin panel whereupon the admin can direct the different database items of the website sorted under models of each app.


<a href="#TableContents">Back to Table of Contents</a>
<hr>


### III. Manual Testing: <a name="Testing4"></a>


* Website loads upon clicking the heroku link.

* Favicon loads in browser tab

* Check that navlinks in navbar links to appropriate link

* Clicking a product links to correct product_detail page

* Footer display correctly, and social media buttons in footer links to correct pages

* toast messages appear when:  
    logging in, logging out, adding review, updating review, deleting review, adding question, updating question, deleting question,  
    adding answer, updating answer, deleting answer, adding product, registering user, and updating userprofile.

* bag works as intended: when clicking add to bag on a product, bag should fill up with the selected quantity of selected item.

* items can be removed or increased/decreased in quantity in bag view

* user can register, and userprofile will be automatically created upon creation

* user can log in

* userprofile can be accessed only after logging in

* logged in user can add reviews to products

* logged in users can add questions to faq

* logged in user can logout

* reviews posted by specific user can be edited by the same user, and not another user

* questions posted by specific user can be edited by same user, and not another user

* Contact form sends me an email upon submit

* Elements scale down and up accordingly in different view widths

* Stripe elements appear in Checkout app

* Checkout works as intended and returns stripe webhook

* edit question view shows form fields as intended

* edit review shows form fields as intended

* edit answer shows form fields as intended

* admin can add or remove products from the store


<a href="#TableContents">Back to Table of Contents</a>
<hr>


## 6. Deployment <a name="Deployment"></a>


To deploy this project I had to create an account on Heroku
Then I created a Heroku app called salomos_apparel
In the Resources tab I commissioned Heroku postgres for use as database
In the settings tab I clicked reveal config vars and entered the following variables from each respective source:

* DJANGO_SECRET_KEY "XXX"
* AWS_ACCESS_KEY_ID "XXX"
* AWS_SECRET_ACCESS_KEY "XXX"
* AWS_STORAGE_BUCKET_NAME "AWS Bucket name"
* STRIPE_PUBLIC_KEY "XXX"
* STRIPE_SECRET_KEY "XXX"
* STRIPE_WH_SECRET	"XXX"
* EMAIL_HOST_PASS "password generated by Gmail for connecting third party service"
* EMAIL_HOST_USER	"the connected email"
* USE_AWS "True"

A requirements.txt file was created to let Heroku know the python dependencies needed to run the project
Typed the following in git bash terminal
pip3 freeze --local > requirements.txt

Then I created a Procfile and entered the following in it
web: gunicorn salomo.wsgi:application

Prepare models for migrations by typing
python3 manage.py makemigrations

Create tables in database by typing
python3 manage.py migrate

Then I went to the deploy tab in heroku and connected to my github repository,  
then I selected enable automatic deploys in the automatic deployment section, and made sure master branch was selected.

And then for the final time in the git bash terminal I typed
git push
which pushed the code to heroku thanks to the above automated deploy setting in heroku.

In the bottom of the build view on heroku, the link for the deployed website can be found,  
I clicked the link and could see the deployed website on heroku.

Deployment finished.


<a href="#TableContents">Back to Table of Contents</a>
<hr>


### I. How to run this project locally <a name="Deployment2"></a>


You will need to create a free account on AWS and set up an S3 bucket

You will need to create a free account on Stripe

Download the project from the github repository

Install required python dependencies by typing in the git bash terminal:
- pip3 -r requirements.txt

Then type python3 manage.py runserver

Create a file named .gitignore, and enter the following line into that file:
env.py
Save and Close .gitignore

Then create file env.py and enter the following lines:
os.environ["DJANGO_SECRET_KEY"] = "XXX"
os.environ["AWS_ACCESS_KEY_ID"] = "XXX"
os.environ["AWS_SECRET_ACCESS_KEY"] = "XXX"
os.environ["AWS_STORAGE_BUCKET_NAME"] = "XXX"
os.environ["STRIPE_PUBLIC_KEY"] = "XXX"
os.environ["STRIPE_SECRET_KEY"] = "XXX"
os.environ["STRIPE_WH_SECRET"] = "XXX"
Save and Close env.py

The "XXX" values above represents secret keys that needs to be extracted from your AWS and Stripe accounts,  
and the Django secret key can be generated here: [Django Key Generator](#https://miniwebtool.com/django-secret-key-generator/),  
unless you use the secret_key variable in settings.py generated upon the Django install procedure.

Create superuser account for accessing database:
python3 manage.py createsuperuser

Type in a valid email, then type in username followed by the password two times,  
the password should be at least 8 characters long, but can be overruled by forcing through a shorter password by clicking "y" on the followup question in the terminal,  
creating it this way with a short password will only work in the git bash terminal and not by users signing up on the webpage.

Type the following to prepare migrations according to the models
python3 manage.py makemigrations

Then type the following to create the tables in the database according to previously prepared migrations
python3 manage.py migrate

The app can now be run locally.


<a href="#TableContents">Back to Table of Contents</a>
<hr>


### II. How to clone this project locally <a name="Deployment3"></a>


1. Select the Github Repository of this project.
2. Click the "Clone or download" button.
3. Copy the web URL presented.
4. Open your IDE, and open the terminal.
5. use cd to change the directory to where you want to clone the repository in.
6. Type - "git clone https://github.com/Voggastur/full-stack-framework-project.git ." to clone the project to current folder.


<a href="#table-of-contents">Back to top</a>
<hr>


## 7. Credits <a name="Credits"></a>


* The basis for this project is the Boutique Ado project by Chris Zielinski at Code Institute, but with visual customizations and expanded features.
* The Bag and Checkout apps are almost entirely imported from the Boutique Ado project with no modifications except renamed references to Boutique Ado.

* The Profiles app is largely imported as well, except for new image field in userprofile, and relevant field mentions in the forms and views.

* The Products app has its foundation in Boutique Ado as well, in particular the products.html template, although with new css.
The Product and Category models, the all_products view, the widgets.py and custom_clearable_file_input template used for image file inputs were also imported.
Although the widget is now also in use for the Profiles.userprofile model and form view.
The Product model was shortened with less fields than the original to make it more comprehensible in the beginning of my development.
The Products product_detail view had to be modified to also show reviews, but from there on all the code is handmade, although a lot of repeating patterns could be used.

* Corey Schafer on Youtube have good video tutorials for Django beginners that helped me write the faq app and relevant models.
Youtube in general is a good source of educating material related to Django, although most like to suddenly spice up the projects with difficult concepts.
This makes it difficult to absorb the knowledge and I could only gain a bit here and there.
That's why the Corey Schafer tutorials were good, he didn't unnecessararily complicate his beginner tutorials.

* The Stripe [webpage](https://www.stripe.com/) was checked frequently to understand and test webhooks, and set up a new endpoint.

* Slack was a frequent source of solutions when troubleshooting, and valuable insights were gained from discussions with other students.


<a href="#TableContents">Back to Table of Contents</a>
<hr>


<img src="https://raw.githubusercontent.com/Voggastur/full-stack-framework-project/master/media/front.jpg" style="margin: 0, width:450px, height:350px;">


<hr>