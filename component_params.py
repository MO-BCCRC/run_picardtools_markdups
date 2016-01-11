'''
Created on May 26, 2014

@author: dgrewal
'''
input_files  = {'input':'__REQUIRED__'}

output_files = {'output':'__REQUIRED__',
                'tmp_dir':'__REQUIRED__',
                 'picard_metrics_file':'__REQUIRED__'}

input_params = {'assume_sorted':'__FLAG__',
                'run_component':'__FLAG__',
                'read_name_regex':"[a-zA-Z0-9]+_[0-9]+:[0-9]+:([0-9]+):([0-9]+):([0-9]+).*",
                'opd':16,
                'mfhfrem':1000,
                'val_stringency':'LENIENT',
                }

return_value = []

