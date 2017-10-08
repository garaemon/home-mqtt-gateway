# home-mqtt-gateway

## setup heroku instance
```
$ heroku create
$ heroku ps:scale web=1
$ heroku addons:create cloudmqtt:cat
```

### How to check CloudMQTT URL
```
$ heroku config:get CLOUDMQTT_URL
```
