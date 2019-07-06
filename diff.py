import yaml
import pprint
pp = pprint.PrettyPrinter(indent=2)

import sys
target = sys.argv[1]

from tabulate import tabulate

def print_to_table(table):
    headers = ['', 'REFERENCE', "TODAY'S TRY"]
    print(tabulate([table], headers, tablefmt="rst"))

table = list()

with open('routine/serverless.yml') as f:
    sls_ref = yaml.load(f.read())

with open(target+'/serverless.yml') as f:
    sls_try = yaml.load(f.read())

print_to_table(['KEYS', ', '.join(sls_ref.keys()), ', '.join(sls_try.keys())])
print_to_table(['YAML', yaml.dump(sls_ref), yaml.dump(sls_try)])
print_to_table(['JSON', pp.pformat(sls_ref), pp.pformat(sls_try)])
for key in sls_ref.keys():
    if key in sls_try.keys():
        print_to_table([key.upper(), pp.pformat(sls_ref[key]), pp.pformat(sls_try[key])])


files_to_compare = [
    "libs/response-lib.js",
    "libs/dynamodb-lib.js",
    "create.js",
    "list.js",
    "get.js",
    "update.js",
    "delete.js"
]

for filename in files_to_compare:
    with open('routine/'+filename) as f:
        ref = f.read()

    with open(target+'/'+filename) as f:
        com = f.read()

    print_to_table([filename.upper(), ref, com])
        




