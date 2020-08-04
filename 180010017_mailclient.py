import socket
import pickle
import argparse
import sys
from assets.core_modules.smtp.custom_mail_template import Mail
from assets.core_modules.databases.custom_database_handler import DatabaseHandler
from assets.core_modules.exeptions.custom_exeptions import WrongEmailFormat, EmptySubject, UserDoesNotExists
from assets.core_modules.clients.users import User

USER_OPTIONS = '''
    1.Manage Mail: Shows the stored mails of logged in user only
    2.Send Mail: Allows the user to send a mail
    3.Quit: Quits the program
'''

def interact_with_user(ip, port):
    username = input('Enter Name: ')
    password = input('Enter Password: ')
    user = User(username, password)
    while not user.is_authenticated:
        print('Wrong Credentials !\n')
        username = input('Enter Name: ')
        password = input('Enter Password: ')
        user.update_credentials(username, password)
    
    while True:
        print(USER_OPTIONS)
        try:
            response = int(input('Your Choice: '))
            if response > 3 or response < 1:
                raise ValueError
            elif response == 1:
                user.operate_on_inbox(ip=ip, port=port)
            elif response == 2:
                user.send_email(ip=ip, port=port)
            else:
                print(f'Process Terminating .....')
                sys.exit(0)
        except KeyboardInterrupt:
            print('Use Given Options To Exit !!')
        except ValueError:
            print('Enter valid values')
        except Exception as e:
            print(f'Error {e} occured')
            break

def Main():
    # For easy parsing of command line arguments
    parser = argparse.ArgumentParser(description='Command Line Argument Parser for client')

    parser.add_argument('-ip', '--ip_address', type=str, help='IP Address to be connected to', required=True)
    parser.add_argument('-p', '--port', type=int, help='Port of Server to be connected to', required=True)

    # Extract arguments passed from user, and verify the arguments are as expected
    args = parser.parse_args()

    # if user doesn't enter a valid port number

    # if user doesn't enter a valid ip address 

    interact_with_user(args.ip_address, args.port)

if __name__ == '__main__':
    Main()
