
### How to use:
```bash
python3 180010017_mailclient.py -ip <your ip> -p <your port>             
python3 180010017_smtpmail.py -p <your port>             
python3 180010017_mailclient.py -p <your port>   
``````          
             
e.g.              
```bash
    python3 180010017_mailclient.py -ip localhost -p 1225             
    python3 180010017_smtpmail.py -p 1225             
    python3 180010017_mailclient.py -p 1225             
```
             
Remember, both mailclient and pop3server can't run on same port at same time. Also, as we are asked to give only one port as command line argument for mailclient, one server must be terminated and other must be started before using other. So if you want to send a mail and then see your inbox, start smtp server, send mail, close smtp server, start pop3 server, see your inbox (with same port).


#### Username:
>
if your username is 'user', then user email as 'user@gmail.com', and send emails only to user who exists in 'user.txt' else its directory doesn't exists and hence no data will be saved.
             
             
#### User's directory (MyMailBox.txt):
>
it is in 'assets/core_modules/databases/users/'             
It has directory with name as name of all users, containing a file named 'MyMailBox.txt'             


#### Actual data handling:
>
Actual data handling occurs from 'database.json' file in 'assets/core_modules/databases/' and hence you are not expected to alter the contents of 'user.txt'


#### Smtp and Pop3 server:
>
Both Smtp and Pop3 servers are concurrent, i.e. Can handle multiple client requests at a time


#### Relevant Screenshots:  
<details>
<summary> Click </summary>
<img src="https://user-images.githubusercontent.com/46635452/93026365-213aa080-f623-11ea-9886-ee0cde1c2aaf.png" alt="screnshot" ></img>
</details>    




