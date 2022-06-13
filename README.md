# coins_homework
- Step
  - 1.install postgreSql  by : https://www.postgresql.org/
  - 2.enter the project root directory
  - 3.enter command migrating databases
    - python3 manage.py makemigrations
    - python3 manage.py migrate
  - 4.python3 manage.py runserver
  - tips : You need to add some accounts (including account name, balance and currency type) to the database manually

  
- API
  - get
    - /user/ ：see all available accounts	
    - /payment/ ：see all payments	

  - post
    - /payment/create_payment/ ：send a payment from one account to another (same currency)
    - params：
      - from_account 
      - to_account
      - amount 

    - request example：
  
    ```
    {
    	"from_account": "bob"
    	"to_account": "alice"
    	"amount": 10
    }
    ```