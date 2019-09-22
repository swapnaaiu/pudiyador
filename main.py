# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging

# [START imports]
from flask import Flask, render_template, request
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/ne')
def newsletter_page():
    return render_template('ne.html',
        issue_names=[
                    'Dec 2009', 'March 2010', 'June 2010', 'Oct 2010', 
                    'Jan 2011', 'April 2011', 'July 2011', 'Nov 2011',
                    'Jan 2012', 'April 2012', 'July 2012', 'Oct 2012',
                    'Jan 2013', 'April 2013', 'July 2013', 'Oct 2013',
                    'Jan 2014', 'April 2014', 'July 2014', 'Oct 2014',
                    'Jan 2015', 'April 2015', 'July 2015', 'Oct 2015',
                    'Jan 2016', 'April 2016', 'July 2016', 'Oct 2016',
                    'Jan 2017', 'April 2017', 'July 2017', 'Oct 2017',
                    'Jan 2018', 'April 2018', 'July 2018', 'Oct 2018',
                    'Jan 2019']
    )

@app.route('/<path:path>')
def content_page(path):
    #pudiyador.org/overview will render template overview.html
    return render_template('%s.html' %path)


"""
# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    # [END submitted]
    # [START render_template]
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
    # [END render_template]"""


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
