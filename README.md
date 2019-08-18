facebook-event-export
=====================

After getting annoyed for the umpteenth time at Facebook alerting me to an
event *after* it happens, I wrote this.

This is a very simple command line script that calls Facebook's mobile site
and gets events for a particular page (eg a local band you like), and returns
the metadata contained within the relevant event pages. Facebook supports
schema.org, and this is the information that is returned, as raw JSON. You
can then do with that as you wish (convert it to ICS, for example.)

Use
---

To run the script, you'll need Python 2.7 (probably works in 3 but not
tested.) Run as follows...

python scrape.py [page id]

So if the page you're interested in has the URL www.facebook.com/myband,

python scrape.py myband

Obviously you can pipe the output through json_pp or anything else you
like.

Advanced use
------------

Not really 'advanced', but you can put as many page ids as you like.

python scrape.py pageone pagetwo pagethree

will return a single JSON object containing the events for all three of
these pages.

