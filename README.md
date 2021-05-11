# Lab-6-Python
 
## Task 
* Create REST-service (operations GET/POST/PUT/DELETE) for one of the classes from laboratory work №3 using following Python instrumentalities:
  * Flask
  * Python 3.x

* Implement saving class object from laboratory work №3 to database 
using following technological stack:
  * SQLAlchemy
  * MySQL

## Instructions
 In addition to listed above, you should be able to test REST service by any mean convenient to you(I personnaly use Postman)
 In order to have this program work, you should:
1. Download a zip version of repository 
2. Unpack it to any location convenient for you
2.1 Create in the repository a .env file, where assign such variables:
         user - for your desired MySQL user
         password - the password for the user
         host - name of the host whichever your MySQL server runs on
         port - number of the port whichever your MySQL server runs on
         database - name of database you will create to work with this program
3. Create a new virtual environment 
4. Activate new environment and pip install requirements.txt
5. Create a database with name specified in .env 
6. In separate terminal, run MySQL Server
7. Open command line terminal, change directory to aforementioned repository and type in "py crud.py"
    