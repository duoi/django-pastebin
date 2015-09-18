# django-pastebin

Fairly simple and straight forward pastebin made in Django. 

* It uses bootstrapjs for the styling and highlightjs for the language formatting.
* Automatically generates four-char alphanumerical URLs (i.e foo.com/*u7bH*) for every paste.
* Has automatic language detection or manual selection of about ~15 languages (highlightjs actually has support for dozens more, but I didn't code it in)

TODO:

* No post expiry feature (can be somewhat easily done by having cron check a py script every 5 or so minutes)
* No spam detection
* Styling is horrible, the "new post" button collapses on resize etc.
