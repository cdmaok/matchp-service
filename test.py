import sys
import traceback

try:
    asdf
except Exception as e:
    print repr(e),str(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    print ''.join('!! ' + line for line in lines)  # Log it or whatever here
