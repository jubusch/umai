from flask import Flask,request,abort,jsonify	
from flask_restplus import Resource, Api,fields
from flask_cors import CORS
import global_variables
import json 

app = Flask(__name__)
api = Api(app)
CORS(app)

settings_descriptor = api.model('Settings',{'noise' : fields.Float('value'),'latency' : fields.Float('value'),'threshold' : fields.Float('value'),'baseNoise' : fields.Float('value'),'decay' : fields.Float('value')})


@api.route('/settings', methods=['PUT','GET'])
class setSettings(Resource):
	
	@api.expect(settings_descriptor)
	def put(self):
		settings = request.get_json()
		global_variables.noise = settings['noise']
		global_variables.latency = settings['latency']
		global_variables.threshold = settings['threshold']
		global_variables.baseNoise = settings['baseNoise']
		global_variables.decay = settings['decay']
		return {'result': 'settings updated'}, 201

	def get(self): 
		response = {}
		response['noise'] = global_variables.noise
		response['latency'] = global_variables.latency
		response['threshold'] = global_variables.threshold
		response['baseNoise'] = global_variables.baseNoise
		response['decay'] = global_variables.decay
		return jsonify(response)

@api.route('/activations', methods=['GET'])
class getActivations(Resource):
	
	def get(self): 
		#Todo:
		#look up python requests api in order to get statments from the learning reckord store 
		#look up learning locker api 
		#get statements where verb==started 
		#filter for latest datetime
		#get statements after datetime
		#set global_variables.action_stream
		execfile("file_generator_template.py")
		#execfile("simulation.py")
		import simulation 
		simulation.umaiEnvironment.run()
		
		return jsonify(global_variables.chunk_activations)



if __name__ == '__main__':
	app.run(debug= True)