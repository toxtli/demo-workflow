import sys, os
sys.path.insert(0, os.path.abspath('../code/automaton'))
from config import Configuration
from utils import StateMachineHelper
from utils.SheetsHelper import SheetsHelper
from modules.ProfilesFinder.ProfilesFinder import ProfilesFinder

# sheet = SheetsHelper({"table":"test"})
# res = sheet.insert({"id":"6","name":"Mario","age":"15"})
# res = sheet.update({"id":"5"},{"name":"Lucas"})
# res = sheet.delete({"id":"3"})
# res = sheet.select({"name":"Carlos"})
# print(res)

"""
StateMachineHelper.load_config(Configuration.logic_file)
StateMachineHelper.set_values('user', {'platforms':'Linkedin'})
StateMachineHelper.set_values('user', {'location':'United States'})
StateMachineHelper.set_values('user', {'feedback':'https://docs.google.com/spreadsheets/d/1QR5HS7nwK5BVURjQ1bzn0JJIG3-DkHfU7Bn2lSrymUo/gviz/tq?tqx=out:csv&sheet=testsheet'})
StateMachineHelper.set_values('user', {'expertise':'Software Engineer'})
"""

args = {
	'location': 'United States',
	'expertise': 'Software Engineer',
	'email': '',
	'password': '',
	'cookies': ''
}
finder = ProfilesFinder(args)
finder.run(args)