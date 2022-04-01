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

| Endpoint URL | Methods | Parameters | Description   |
|:------------:|:-------:|------------|---------------|
|      /       |  _GET_  | _params_   | _description_ |

<br>

### Shopping Cart

> All URLs are prefixed with:  http://localhost:81/...

| Endpoint URL | Methods | Parameters | Description   |
|:------------:|:-------:|------------|---------------|
|      /       |  _GET_  | _params_   | _description_ |

<br>

### Book Details

> All URLs are prefixed with:  http://localhost:81/book-details

| Endpoint URL | Methods | Parameters | Description   |
|:------------:|:-------:|------------|---------------|
|      /       |  _GET_  | _params_   | _description_ |

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