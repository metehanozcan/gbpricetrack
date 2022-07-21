# A basic real-time price tracking website that collects data via python.
[GbFiyat Website](http://gbfiyat.herokuapp.com/ "GbFiyat Website")

`Note: When Heroku has only one web dyno and that dyno doesn't receive any traffic in 1 hour, the dyno goes to sleep. When someone accesses the app, the dyno manager will automatically wake up the web dyno to run the web process type. This causes a short delay for this first request, but subsequent requests will perform normally.`

`You will have to wait for 15-20 seconds for dyno to wake up. After that, page will be loaded.`

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
