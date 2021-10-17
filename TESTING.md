# Full Testing
## Contents
+ [Validator Testing](#validator-testing)
+ [Lighthouse Testing](#lighthouse-testing)
+ [PowerMapper Compatibility](#powermapper-compatibility)
+ [Testing From User Stories](#testing-from-user-stories)
+ [Manually Testing Functionality](#manually-testing-functionality)
+ [Responsive Testing](#responsive-testing)
+ [Bugs and Fixes](#bugs-and-fixes)
+ [Known Bugs](#known-bugs)
---
---
## Validator Testing
### **HTML**

 I checked all of the HTML pages using [W3C Markup Validation Service](https://validator.w3.org/)


 All pages passed all checks. 

### **CSS**


### **JavaScript**

I checked the script.js file using [JSHint](https://jshint.com/)


### **Python**
I checked the app.py file using [PEP8 online](http://pep8online.com/)

The code passed all checks.

---
---
## Lighthouse Testing



### **Performance**


### **Accessibility**


### **Best Practices**

### **SEO**


---
---
## PowerMapper Compatibility

I used [PowerMapper](https://www.powermapper.com/) to test cross-browser compatbility on other browsers that I don't have access to.

---
---
## Testing From User Stories

### As a casual user: 

---

### As a returning user: 

---

### As the site owner/admin:


---
---
## Manually Testing Functionality
### **Navigation**

|Element               |Action|Expected Result               |Pass/Fail|
|:-------------         |:----|:----------------------------------|:---|
| **NavBar**            |                                         |    |
|Site Name (logo area)  |Click|Redirect to home                   |Pass|
|My profile Dropdown    |Click|Open profile dropdown              |Pass|
|Register Link          |Click|Redirect to register page          |Pass|
|                       |     |(Not visible if user in session)   |Pass|
|Log In Link            |Click|Redirect to log in page            |Pass|
|                       |     |(Not visible if user in session)   |Pass|
|Product Management Link|Click|Redirect to add_product page       |Pass|
|                       |     |(Only visble if admin in session)  |Pass|
|Artist Management Link |Click|Redirect to add_artist page        |Pass|
|                       |     |(Only visble if admin in session)  |Pass|
|Class Management Link  |Click|Redirect to add_class  page        |Pass|
|                       |     |(Only visble if admin in session)  |Pass|
|My Profile Link        |Click|Redirect to user profile page      |Pass|
|                       |     |(Only visble if user in session)   |Pass|
|Logout Link            |Click|Redirect to logout confirm  page   |Pass|
|                       |     |(Only visble if user in session)   |Pass|
|Bag Link               |Click|Redirect to bag page               |Pass|
| **SideNav**           |     |                                   |    |
|Hamburger Icon         |Click|Open Sidenav                       |Pass|
|Site Name (logo area)  |Click|Redirect to home                   |Pass|
|My profile Dropdown    |Click|Open profile dropdown              |Pass|
|Register Link          |Click|Redirect to register page          |Pass|
|                       |     |(Not visible if user in session)   |Pass|
|Log In Link            |Click|Redirect to log in page            |Pass|
|                       |     |(Not visible if user in session)   |Pass|
|Product Management Link|Click|Redirect to add_product page       |Pass|
|                       |     |(Only visble if admin in session)  |Pass|
|Artist Management Link |Click|Redirect to add_artist page        |Pass|
|                       |     |(Only visble if admin in session)  |Pass|
|Class Management Link  |Click|Redirect to add_class  page        |Pass|
|                       |     |(Only visble if admin in session)  |Pass|
|My Profile Link        |Click|Redirect to user profile page      |Pass|
|                       |     |(Only visble if user in session)   |Pass|
|Logout Link            |Click|Redirect to logout confirm  page   |Pass|
|                       |     |(Only visble if user in session)   |Pass|
|Bag Link               |Click|Redirect to bag page               |Pass|
| **MainNav**           |     |                                   |    |
|All Products Link      |Click|Redirect all products page         |Pass|
|Prints Dropdown        |Click|Open prints Dropdown               |Pass|
|Phographs Link         |Click|Redirect to prints page filtered to photographs |Pass|
|Art Prints Link        |Click|Redirect to prints page filtered to art prints  |Pass|
|Digital Art Link       |Click|Redirect to prints page filtered to digital art |Pass|
|All Prints Link        |Click|Redirect to prints page            |Pass|
|Originals Dropdown     |Click|Open originals page                |Pass|
|Watercolour Paintings Link|Click|Redirect to originals page filtered to watercolours |Pass|
|Acrylic Paintings Link |Click|Redirect to originals page filtered to acrylics        |Pass|
|Oil Paintings Link     |Click|Redirect to originals page filtered to oil paintings   |Pass|
|Mixed Media Link       |Click|Redirect to originals page filtered to mixed medias    |Pass|
|All Originals Link     |Click|Redirect to originals page         |Pass|
|Classes Dropdown       |Click|Open classes Dropdown              |Pass|
|Beginner Link          |Click|Redirect to classes page filtered to beginner classes     |Pass|
|Intermediate Link      |Click|Redirect to classes page filtered to intermediate classes |Pass|
|Advanced Link          |Click|Redirect to classes page filtered to advanced classes     |Pass|
|All Classes Link       |Click|Redirect to classes page           |Pass|
|Artists Link           |Click|Redirect to artists page           |Pass|
| **Footer**                |     |                          |    |
|*Customer Care*            |     |                          |    |
|Contact Us Link            |Click|Redirect to contact page  |Pass|
|FAQ's Link                 |Click|Redirect to FAQ's page    |Pass|
|Shipping & Handling Link   |Click|Redirect to FAQ's page    |Pass|
|Returns & Exchanges Link   |Click|Redirect to FAQ's page    |Pass|
|*Socials*                  |     |                          |    |
|Facebook Link              |Click|Open on external page     |Pass|
|Instagram Link             |Click|Open on external page     |Pass|
|Twitter Link               |Click|Open on external page     |Pass|
|TikTok Link                |Click|Open on external page     |Pass|
|*Account*                  |     |                          |    |
|**if user not in session** |     |                          |    |
|Log in Link                |Click|Redirect to login page    |Pass|
|Register Link              |Click|Redirect to signup page   |Pass|
|**if user in session**     |     |                          |    |
|profile Link               |Click|Redirect to profile page  |Pass|
|Log out Link               |Click|Redirect to log out confirmation page|Pass|
|**if admin in session**    |Click|Open on external page     |Pass|
|Product Management Link    |Click|Redirect to add product page|Pass|

---
### **Home Page**
| Element               | Action | Expected Result   | Pass/Fail|
|:-------------         |:-----|:-----                     |:---|
|Hero 'Shop Now' Button |Click |Redirect to products page  |Pass|

---

### **Products Page**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|'Sort By' Dropdown         |Click   |Open 'sort by' options          |Pass|
|'Sort By' Options (x6)     |Click   |Re-order products               |Pass|
|If category selected:      |        |                                |Pass|
|Category button            |Click   |                                |Pass|
|Product Card               |Hover   |Box shadow appears              |Pass|
|                           |Click   |Redirect to product detail page |Pass|

---

### **Product Detail Page**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|Qty control buttons        |        |Increase/decrease quantity    |    |
|Keep Shopping button       |Click   |Redirect to products page     |    |
|Add to bag button          |Click   |Add item to bag               |Pass|
|                           |        |Toast Success appears         |Pass|
|                           |        |Item visible in toast success |Pass|
|**If admin in session:**   |        |                              |    |
|Edit product button        |Click   |Redirect to edit product page |Pass|
|Delete product button      |Click   |Open delete confirmation modal|Pass|
|Modal cancel button        |Click   |Close modal                   |Pass|
|Modal delete button        |Click   |Delete product                |Pass|

---

### **Artists Page**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|Artist Card                |Hover   |Box shadow appears              |Pass|
|                           |Click   |Redirect to product detail page |Pass|

---

### **Artist Detail Page**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|Social Media links         |Click   |Link to external ink on seperate tab |Pass|
|All Artists button         |Click   |Redirect to artists page      |Pass|
|Shop Now button            |Click   |Redirect to products page     |Pass|
|Gallery Image              |Hover   |Box shadow appears            |Pass|
|                           |Click   |Redirect to product detail page|Pass|
|**If admin in session:**   |        |                              |    |
|Edit artist button         |Click   |Redirect to edit artist page  |Pass|
|Delete artist button       |Click   |Open delete confirmation modal|Pass|
|Modal cancel button        |Click   |Close modal                   |Pass|
|Modal delete button        |Click   |Delete artist                 |Pass|

---

### **Classes Page**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|'Sort By' Dropdown         |Click   |Open 'sort by' options          |Pass|
|'Sort By' Options (x4)     |Click   |Re-order classes                |Pass|
|If level selected:         |        |                                |Pass|
|Level button               |Click   |                                |Pass|
|Class  Card                |Hover   |Box shadow appears              |Pass|
|                           |Click   |Redirect to class  detail page  |Pass|

---

### **Class Detail Page**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|**If user in session:**    |        |                              |      |
|Video                      |Onload  |Available (if user in session)|Pass|
|*Video Controls*           |Onload  |Unavailable (if user not in session)|Pass|
|Play                       |Click   |Video Plays                   |Pass|
|Pause                      |Click   |Video Pauses                  |Pass|
|Full Screen                |Click   |Video Expands to fullscreen   |Pass|
|Volume Up                  |Click/Slide |Volume increases          |Pass|
|Volume Down                |Click/Slide |Volume decreases          |Pass|
|Volume Mute                |Click   |Video mutes                   |Pass|
|**If user not in session:**|        |                              |    |
|Video                      |Onload  |Unavailable                   |Pass|
|Login button               |Click   |Video Plays                   |Pass|
|Register button            |Click   |Video Pauses                  |Pass|
|**All users:**             |        |                              |    |
|All Classes button         |Click   |Redirect to classes page      |    |
|**If admin in session:**   |        |                              |    |
|Edit class button          |Click   |Redirect to edit class page   |Pass|
|Delete class button        |Click   |Open delete confirmation modal|Pass|
|Modal cancel button        |Click   |Close modal                   |Pass|
|Modal delete button        |Click   |Delete Class                  |Pass|

---

### **Add Product Page**

| Element                       | Action    | Expected Result                | Pass/Fail |
|:-------------                 |:----------|:-----                          |:-----|
|Form Dropdowns(x2)             |Click      |Show dropdown options           |Pass  |
|Form Text Input (if required)  |Leave blank|On Submit: Warning appears, form won't submit |Pass  |
|Form Text Input (if required)  |Fill In    |On Submit: Form submit          |Pass  |
|Form Text Input         |Just input whitespace|On Submit: Form won't submit |Pass  |
|                               | |On Submit: error message on invalid field |Pass  |
|                               |           |On Submit: error toast appears  |Pass  |
|Form Number field              |Click up/down|increase/decrease value       |Pass  |
|                               |Type into  |Accept value                    |Pass  |
|Form image Select button       |Click      |Open device storage             |Pass  |
|                               |           |Chosen image name displayed     |Pass  |
|Cancel button                  |Click      |Redirect to products page       |Pass  |
|Add Product button(form valid) |Click      |Form submit                     |Pass  |
|                               |           |Redirect to product detail page |Pass  |
|                               |           |Product uploaded toast appears  |Pass  |
|Add Product button(form invalid)|Click     |Form doesn't submit             |Pass  |
|                               |           |Error messages on invalid fields|Pass  |

---

### **Edit Product Page**

| Element                       | Action    | Expected Result                | Pass/Fail |
|:-------------                 |:----------|:-----                          |:-----|
|Form Dropdowns(x2)             |Click      |Show dropdown options           |Pass  |
|Form Text Input (if required)  |Leave blank|On Submit: Warning appears, form won't submit |Pass  |
|Form Text Input (if required)  |Fill In    |On Submit: Form submit          |Pass  |
|Form Text Input                |Just input whitespace|On Submit: Form won't submit|Pass  |
|                               |           |On Submit: error message on invalid field |Pass  |
|                               |           |On Submit: error toast appears  |Pass  |
|Form Number field              |Click up/down|increase/decrease value       |Pass  |
|                               |Type into  |Accept value                    |Pass  |
|Form image Select button       |Click      |Open device storage             |Pass  |
|Cancel button                  |Click      |Redirect to products page       |Pass  |
|Add Product button(form valid) |Click      |Form submit                     |Pass  |
|                               |           |Redirect to product detail page |Pass  |
|                               |           |Product uploaded toast appears  |Pass  |
|Add Product button(form invalid)|Click     |Form doesn't submit             |Pass  |
|                               |           |Error messages on invalid fields|Pass  |

### **Edit Product Page**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|**Login**                  |        |                              |      |

---

### **Add Artist Page**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|**Login**                  |        |                              |      |

---

### **Edit Artist Page**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|**Login**                  |        |                              |      |

---

### **Add Class Page**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|**Login**                  |        |                              |      |

---

### **Edit Class Page**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|**Login**                  |        |                              |      |

---

### **Allauth Pages**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|**Login**                  |        |                              |      |
|**Register**               |        |                              |      |
|**Logout Conformation**    |        |                              |      |

---
---
## Responsive Testing
Through devices that I have at home/readily available to me, I was able to continuously test on:
### Phone:
+ Samsung Galaxy S9
  + Google Chrome
  + Samsung Internet
+ Huawei Y7
  + Google Chrome
+ iPhone 6
  + Safari
### Tablet
+ iPad Mini 7.9"
  + Safari
+ iPad 9.7"
  + Safari
### Computer
* Avita Pura 14" Laptop
  * Google Chrome
  * Microsoft Edge
  * Opera
  * Mozilla Firefox
### Responsinator
+ When there were devices/browsers that I didn't have access to, I used [Responsinator](https://www.responsinator.com/) to make sure that the site was responsive.

---
---
## Bugs and Fixes


---
---
## Known Bugs
