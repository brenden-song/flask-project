from app import app
from flask import render_template
import ldclient

ldclient.set_sdk_key("sdk-cf80f41f-438e-4e5b-8e12-c275e46e1338")
ld_client = ldclient.get() 

user = {
    "key" : "bsong@launchdarkly.com"
}


@app.route('/')
def app():
    show_feature = ld_client.variation("new-flag", user, False) 

    if show_feature:
        return render_template('sidebar.html')

    else:
        return render_template('base.html')
  # the code to run if the feature is off















