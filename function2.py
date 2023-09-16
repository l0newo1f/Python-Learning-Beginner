# import function
# import function as fc
# from function import build_profile
# from function import build_profile as bp
from function import *

# user_profile = function.build_profile('albert','einstein',location = 'princeton',field = 'physics')
# user_profile = fc.build_profile('albert','einstein',location = 'princeton',field = 'physics')
# user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')
# user_profile = bp('albert','einstein',location = 'princeton',field = 'physics')
user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')
print(user_profile)