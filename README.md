# Blockchain A-Z
This repo is for Blockchain A-Z course from Udemy

## Python Virtual Environment

```
$ apt install python3, pip3 #for Linux
$ brew install python3, pip3 #for Mac
$ pip3 install virtualenv
$ virtualenv -p python3.8.9 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## POST with CURL

In order to make a transaction, you can use curl command. See below example. Check the right port number before send command.

```
$ curl -X POST -H "Content-Type: application/json" \
    -d '{"sender": "Myself", "receiver": "Netflix", "amount": "39"}' \
    http://127.0.0.1:5001/add_transactions
```