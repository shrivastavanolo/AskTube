# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request
import helper

# creating a Flask app 
app = Flask(__name__) 

@app.route('/', methods = ['GET']) 
def disp(): 
	url = request.args['url']
	query = request.args['query']
	return helper.give_answer(url,query)
	# return f"{query:}+{url}"

# driver function 
if __name__ == '__main__': 

	app.run(debug = True)