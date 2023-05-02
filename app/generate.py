import pandas as pd
import json
import sqlite3
import sys
from dotenv import dotenv_values

def combine_confs(conf_list):
	confs = {
		"models_root": "app/new_model/",
		"models": conf_list
	}
	return confs

def create_conf(model_path, model_id, model_gpu, bpe_path_src, bpe_path_tgt) -> str:
	conf = {
		'model': model_path,
		'id': model_id,
		'timeout': -1,
		'load': True,
		"opt": {
	    	"gpu": model_gpu,
	    	"beam_size": 10
		},

		"tokenizer": {
	     	"src": {
	        	 "type": "pyonmttok",
	        	 "mode": "space",
	             "params": {
	                "bpe_model_path": bpe_path_src,
	        		"joiner_annotate": True,
	        		"joiner": "@@"
	                }
	        },

		"tgt": {
	        "type": "pyonmttok",
	        "mode": "space",
	    	"params": {
	            "bpe_model_path": bpe_path_tgt,
	    		"joiner_annotate": True,
	    		"joiner": "@@"
	            }
	        }
	    }
	}
	return conf

def get_model_path(src,tgt):
	return f"{src}-to-{tgt}/{src}-to-{tgt}.pt"

def get_bpe_paths(src,tgt):
	lang_pair = f"{src}-to-{tgt}"
	bpe_path_src = f"{lang_pair}/bpe_{src}.model"
	bpe_path_tgt = f"{lang_pair}/bpe_{tgt}.model"
	return bpe_path_src, bpe_path_tgt

def create_model_config(current_server, model_df):
	model_confs = []
	for index, row in model_df.iterrows():
		server = row['server']

		if current_server == server:
			src = row['source']
			tgt = row['target']
			model_gpu = row['gpu']
			model_id = row['id']

			# Get the location of the relevant models
			model_path = get_model_path(src,tgt)
			bpe_path_src, bpe_path_tgt = get_bpe_paths(src,tgt)
			conf = create_conf(model_path, model_id, model_gpu, bpe_path_src, bpe_path_tgt)
			model_confs.append(conf)
	full_config = combine_confs(model_confs)
	return full_config

def write_config_to(config,path):
	with open(path, "w") as config_file:
		config_file.write(json.dumps(config))

def main():
	config = dotenv_values('.env')

	db = sqlite3.connect("app/DB/database.sqlite")
	model_df = pd.read_sql_query("SELECT * FROM models", db, index_col=None)

	current_server = config['SERVER']
	config = create_model_config(current_server, model_df)
	write_config_to(config,"app/config.json")

if __name__ == "__main__":
	main()
