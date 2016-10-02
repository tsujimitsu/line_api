Line API v2 Sample
====
* Line API v2 sample code

usage
----

    $ git clone https://github.com/tsujimitsu/line_api.git
    $ cd line_api
    $ vi api.env
    [auth]
    token = <Your LINE API TOKEN>

    $ heroku login
    $ heroku create
    $ heroku git:remote --app enigmatic-sierra-XXXXX
    $ git remote -v
    $ git push heroku master
    $ curl https://XXXX.herokuapp.com/message/push/<userid>/test_push_message

webhook
----
* set webhook url in Line Developers page
 * https://XXXX.herokuapp.com/webhook
