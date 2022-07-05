# TravelNZ



##### Setting up website

- added a starter superuser account (**username: admin password: admin**)

- added users groups with permissions (see table below for more information)

- added agents and  tours/durations  data to the data base

- added each user from data sheet to groups and set appropriate permissions as in table below (9 users)

- users data pattern: 

     **username**:   first name with first capital letter 


​			**password**: user1234  (should be changed later on)

​		    **email**: first name with  + @email.com  (should be changed later on)

- fixed login.html template. it didn't have method="post" for 'form' tag. also used default form  instead custom one

- added "home/agents/<agent_id> "   page with information on the agent with id number  <agent_id>

- added "accounts/sign up" , "accounts/login", "accounts/logout" pages with appropriate forms

- added "accounts/password_change"   page. it's available if user is signed in. Also accounts/password_change/done",  "accounts/ password_reset/", " accounts/ password_reset/done/" pages

- added navbar functionalities:

  - Logged in users have their username displayed in the  dashboard and have an option to log out from the current session
  - Guest  users  have an option to log in or sign up displayed in the dashboard

- added  "home/agents/<int:pk>/tours/" – lists all the tours in the system by specific agent. Added to "agent details" pages

- wrote recommendation  on security improvement  to Additional_OWASP_Recommendation.txt

- created the security procedures document. This document  contain username and password guidelines that the administrators can follow when creating users and groups

- 

### To do:



- [ ] add "change pasword",   "reset pasword",  links to navbar for appropriate users
- [x] ​      set up website authentication to be viewed by guest users, who would only be seeing general  information on tours, and agents, as well as company staff, who will  have different permissions based on their position and department they  are working at
- [ ] ​     Create a test log document and note down the testing conditions, the expected outcomes and the actual outcomes. Login as different users to **test** that you can **access** only specific pages and functionality as per the user requirements. Note  down the changes you have made to fix the bugs, if any
- [ ] ​    Make sure that users can access all the pages they should have  access to through the website and that the navigation through the pages  is logical
- [ ] ​     make sure you have created appropriate documentation per the tasks above:

  - Authentication

  - Authorisation

  - Validation 
- [ ] push website on GitHub






##### Users and Groups

Each user should be assigned to appropriate user group with certain permissions:

| Users                                                        | Groups         | Permissions                                                  |
| ------------------------------------------------------------ | -------------- | ------------------------------------------------------------ |
| Haywood Luby, Mariah Schumaker                               | Administrators | **log entry** (add, change, delete, view), **permissions**  (add,change, delete, view), **content type** (add,change, delete, view), **session** (add,change, delete, view), **agents** (view list, view details, add new, edit, delete), **tours** (view list, view details, create, edit, delete), **users** (view list, view details, create, edit, delete),   **groups** (view list, view details, create, edit, delete),   **durations** (view, create, edit, delete)     * *Note: administrators cannot see users passwords because they stored in encrypted form but can set new password* |
| Marty Schaeffer, Beryl Gauer, Cathrine Heckstall, Dane Ratliff | Agents         | **tours** (view list, view details, create, edit, delete)  ** Note:* *each agent should have permissions to create/edit/delete  only their tours details. Also they should be able to change their user's personal data information. For example user name and/or password.* |
| Halina Dabbs, Andres Peltier                                 | Management     | **tours** (view list, view details, create, edit, delete), **agents** (view list, view details, add new, edit, delete), **durations** (view, create, edit, delete) |



##### Log levels. Security events that could be logged.

The following log levels could be used:

- `INFO`: General system information
- `WARNING`: Information describing a minor problem that has occurred.
- `ERROR`: Information describing a major problem that has occurred.
- `CRITICAL`: Information describing a critical problem that has occurred.



| event                                                        | log level | message examples                                             |
| ------------------------------------------------------------ | --------- | ------------------------------------------------------------ |
| user entered wrong name and/or password, email               | warning   | "system cannot login this user because provided credentials are wrong" |
| user is trying to create an account with too short or too weak password | error     | "chosen password is too short or too weak. please try a different one" |
| user is trying to create an account with already existing username or email | error     | "chosen username or email already exist. please try a different one" |
| user is trying to reach some page without certain authorisation (for example agents' group user is trying to reach admin page) | error     | "you are not authorised  to view this page", possible redirection to sign in form |
| user is trying to reach non existing page                    | error     | "page not found"                                             |
| user is trying to modify data without appropriate authorisation | critical  | "you are not authorised to modify this data"                 |





