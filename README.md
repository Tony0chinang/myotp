OTP Server in Django
=========================

This is my solution for creating an OTP generation and verification API services using django framework.


Installation
------------

    1. Create a local copy of this project into your computer.
    2. Create a virtual environment inside this project (local copy).
    3. Install dependencies (requirements.txt).


API Calls
------------

###### COUNTER-BASED OTP

**GET**

    http://127.0.0.1:8000/verify/<phone number>/

**POST**

    http://127.0.0.1:8000/verify/<phone number>/
  
    DATA
    {
      "otp":349217
    }
 
 
**TIME-BASED OTP**

**GET**
      
    http://127.0.0.1:8000/verify/timer/<phone number>/

**POST**
      
    http://127.0.0.1:8000/verify/timer/<phone number>/

    DATA
    {
      "otp":349217
    }
    
    
