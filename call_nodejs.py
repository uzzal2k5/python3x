from Naked.toolshed.shell import execute_js, muterun_js
import sys
# http://sweetme.at/2014/02/17/a-simple-approach-to-execute-a-node.js-script-from-python/
success = execute_js('api_request.js')
if success:
    print(success)
else:
    print("Some Issue arise")

response = muterun_js('api_request.js')
if response:
    if response.exitcode == 0:
        data = response.stdout
        print(data.decode('utf-8'))

    else:
        error = sys.stderr.write(response.stderr)
    print(response)
else:
    print('Some Issue may happened, PLease review your code !')

