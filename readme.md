Look at [this](https://github.com/harshraj22/SMTP_and_POP3/blob/master/use.md) page for getting started on how to use it and relevant screenshots.

### SMTP and POP3
This project aims to mimic the functionality of sending and recieving email in a secure manner using SMTP and POP3 server.

I have used [socket](https://docs.python.org/3/howto/sockets.html) programming for the communication between the peers. Various Object Oriented design principles have been used focusing on the extentibility and maintainability of the code.

The program has been created making extensive use of Objects, breaking and encapsulating the functionalities into separate classes and ensuring [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single-responsibility_principle) is followed. The program has been split into various modules, whose functionalities overlap as little as possible, thus following [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns). Most of the classes have been provided with appropriate methods, that performs only one task, thus removing burden of doing everything from one single method and following the [K.I.S.S. Principle](https://en.wikipedia.org/wiki/KISS_principle).

Finally Various Software design practices have been followed to ensure the code is easily understandable. All the classes and methods have been provided with consise [docstrings](https://github.com/harshraj22/SMTP_and_POP3/blob/934a7dbef975151e0aac2bdc6f8d29d42573f814/assets/core_modules/databases/custom_database_handler.py#L57) and proper comments have been used in the code to ensure readibility isn't compromised.

Though I have tried to make the program friendly for both users, as well as developers, Suggestions to improve it further are welcomed through [issues](https://github.com/harshraj22/SMTP_and_POP3/issues) and [discussions](https://github.com/harshraj22/SMTP_and_POP3/discussions).
