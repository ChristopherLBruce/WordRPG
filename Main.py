import sys, traceback

import WordRPG



if __name__ == "__main__":
    try:
        # if sys.version_info[0] < 3.7:
        #     raise Exception("Python 3.7 or a more recent version is required."
        WordRPG.main.run(start='game')
    except Exception as err:
        print('Exception Error:' + str({err}))
        print('Stack at time of error:')
        traceback.print_exc(file=sys.stdout)

        # keep console window open so we can see error text
        while True:
            pass
