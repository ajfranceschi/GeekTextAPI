# Geek Text API_Group 7

___

### Members

| Name                  |          Feature           | 
|:----------------------|:--------------------------:|
| Antonio J. Franceschi | Book Browsing and Sorting  |
| Adriana Franchino     | Book Rating and Commenting |
| Carlos Gonzalez       |        Book Details        |
| Diamond Forbes        |    Wish List Management    |
| Kevin Forero          |     Profile Management     |
| Nicole Gentil         |       Shopping Cart        |

___

## Usage

> Upon cloning the project, open your Terminal and navigate to the root of the project and run `pip install -r requirements.txt` to install all project dependencies.

> **Requirement**: This project uses MySQL, therefore you must have an instance of MySQL server available to execute database CRUD statements.
>
> *Optional: Execute the MySQL code located in `/utils/schema.sql` to create the database and tables prior to starting the project.*

Once you have installed the dependencies, and you have your MySQL server connection details, create a file named **
DB_CREDS.py** in the directory named `/core/` and add the variables to connect to your MySQL server.

```
USERNAME = your_mysql_username
PASSWORD = your_mysql_password
HOST = your_mysql_host
PORT = your_mysql_port
DATABASE = 'geek_text_db'
```

### Ready to start

After performing the steps above, your project is ready to be started. Build and run your project. The API will be listening on **http://localhost:81**

___

## Features

Below is a list of the endpoints in this API, including their URL, method, parameters and description. All endpoint URLs begin with **http://localhost:81/**.

### Book Browsing and Sorting

> All URLs are prefixed with: http://localhost:81/book-browsing-sorting

| Endpoint  URL |    Methods     | Parameters                                                | Description                                                                                                                                                                                                                                                                       |
|:-------------:|:--------------:|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       /       | GET<br>OPTIONS | *N/A*                                                     | **GET** request returns a string. <br>**OPTIONS** request returns the APIs options.                                                                                                                                                                                               |
|  /get-books   |      GET       | **quantity***<br><sub>&emsp;&emsp;&emsp;_*optional_</sub> | **No params**: Returns all books in DB. <br><br>**Quantity param is provided**: API will return N books beginning at N position in the database. <br><br> <mark>*If N > than amount of books between N and end of database, will return the books from N to database end.*</mark> |
|   /top-ten    |      GET       | *None*                                                    | Returns top ten books based on units sold                                                                                                                                                                                                                                         |
|   /by-genre   |      GET       | **genre**                                                 | Returns all books matching the genre specified in the "genre" param. <br> Example: `GET http://localhost:81/book-browsing-sorting/by-genre?genre=Fantasy`                                                                                                                         |
|  /by-rating   |      GET       | **rating**                                                | Returns all books that match the rating specified in the "rating" (float) param and above.<br> Example: `GET http:/localhost:81/book-browsing-sorting/by-rating?rating=4.5`                                                                                                       |                                                                                                                                                                                    
<br>

### Profile Management

> All URLs are prefixed with:  http://localhost:81/...

| Endpoint URL |     Methods      | Parameters                                                                                                                                                                                               | Description                                                                                                                                                                                                                           |
|:------------:|:----------------:|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /getUserInfo |      _GET_       | string:username                                                                                                                                                                                          | When submitting the endpoint, it is required to include a string with a valid username. Once it is provided, it will return all the information associated with that account                                                          |
|   /addUser   |      _POST_      | string:first_name<br/>string:last_name<br/>string:username<br/>string:passwordU<br/>string:emailAddress<br/>string:addressLine1<br/>string:addressLine2<br/>string:city<br/>string:state<br/>int:zipcode | This endpoint requires the user to provide all the required parameters in order to add anew user into the database                                                                                                                    |
| /updateUser  | _GET_<br/>_POST_ | int:idUsers<br/>Any other parameter/field the user wants to edit from an existing account except for the emailAdrress                                                                                    | The user includes the idUsers from a valid account within the endpoint. Then under the "body" section in postman, user will include the name of the field that needs to be updated plus the new value. emailAddress filed is immutable|

<br>

### Shopping Cart

> All URLs are prefixed with:  http://localhost:81/...

| Endpoint URL | Methods | Parameters | Description   |
|:------------:|:-------:|------------|---------------|
|      /       |  _GET_  | _params_   | _description_ |

<br>

### Book Details

> All URLs are prefixed with:  http://localhost:81/book-details

|   Endpoint URL    | Methods | Parameters                                                                                                                                                                                        | Description                                                                                                                                |
|:-----------------:|:-------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|         /         |   GET   | *N/A*                                                                                                                                                                                             | **GET** Request returns a string.                                                                                                          |
|     /addBook      |  POST   | str: isbn<br/>int: idAuthors<br/>str: bookTitle<br/>str: bookDescription<br/>float: bookPrice<br/>str: bookGenre<br/>str: bookPublisher<br/>int: bookYearPublished<br/>int: unitsSold<br/>float: bookRating | **POST** Create a book with the book ISBN, book name, book description, price, author, genre, publisher , year published, and copies sold. |
|     /getABook     |   GET   | str: isbs                                                                                                                                                                                         | **GET** Request returns a Book's details.                                                                                                  |
| /getBooksByAuthor |   GET   | int: isAuthor                                                                                                                                                                                     | **GET** Request returns a list of books by and author                                                                                      |

<br>

### Author Details

> All URLs are prefixed with:  http://localhost:81/authors

| Endpoint URL | Methods | Parameters                                                                                    | Description                                                                    |
|:------------:|:-------:|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
|      /       |   GET   | *N/A*                                                                                         | **GET** Request returns a string.                                                                                |
|  /addAuthor  |  POST   | str: authorFirstName<br/>str: authorLastName<br/>str:authorPublisher<br/>str: authorBiography | **POST** Create an  author with first name, last name, biography and publisher |

<br>

### Book Rating and Commenting

> All URLs are prefixed with:  http://localhost:81/...

| Endpoint URL | Methods | Parameters | Description   |
|:------------:|:-------:|------------|---------------|
|      /       |  _GET_  | _params_   | _description_ |

<br>

### Wish List Management

> All URLs are prefixed with:  [link=http://localhost:81/...

| Endpoint URL | Methods | Parameters | Description   |
|:------------:|:-------:|------------|---------------|
|      /       |  _GET_  | _params_   | _description_ |