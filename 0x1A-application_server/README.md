Ensure SSH access to web-01:
Make sure that task #3 of your SSH project is completed, and the checker can connect to your web-01 server using SSH.

Install net-tools:
Connect to your web-01 server and install the net-tools package using the following command:

bash
Copy code
sudo apt update
sudo apt install -y net-tools
Clone AirBnB_clone_v2:
Clone your AirBnB_clone_v2 repository onto your web-01 server. Replace <your-github-username> with your actual GitHub username.

bash
Copy code
git clone https://github.com/<your-github-username>/AirBnB_clone_v2.git
Configure the Flask application:
Open the file web_flask/0-hello_route.py and modify it to serve content from the route /airbnb-onepage/ on port 5000. Make sure to name your Flask application object app. Below is an example of how the modified file might look:

python
Copy code
#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    """Returns a response for the route /airbnb-onepage/"""
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
Save the changes to the file.

Run the Flask application:
Run the Flask application on your web-01 server:

bash
Copy code
cd AirBnB_clone_v2/web_flask
python3 0-hello_route.py
This will start the Flask application, and it should be accessible at http://your-web-01-ip:5000/airbnb-onepage/

Test the application:
Open a web browser and navigate to http://your-web-01-ip:5000/airbnb-onepage/ to verify that the Flask application is serving content as expected.

Once you have completed these steps, your Flask application should be configured to serve content from the specified route and port on your web-01 server.

User
Traceback (most recent call last):
  File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/ubuntu/AirBnB_clone_v2/web_flask/0-hello_route.py", line 7, in <module>
    from flask import Flask
ModuleNotFoundError: No module named 'flask'
