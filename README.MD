# A basic price tracking website that collects data via python, controlled by flask and ajax.
![App Preview](https://gcdnb.pbrd.co/images/T1GRipeKGEhc.png?o=1 "App Preview")

## What does this app do? 
It pulls the price data from the websites we have determined and displays it in simple tables on our home page. Our data is updated periodically.
## Where can I deploy my app?
You can use heroku. 
Make sure to set heroku procfile to;
`web: gunicorn app:app`

Also you need to edit requirements.txt to;
`gunicorn
grequests
beautifulsoup4
lxml
requests
pandas
flask
`