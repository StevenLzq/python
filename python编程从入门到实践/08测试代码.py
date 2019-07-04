#################################################################
'''
from name_function import get_formatted_name
print("enter 'q'to quit at any time")
while True:
    first=input('piease input your first name:')
    if first=='q':
        break
    last=input('please input you last name:')
    if last=='q':
        break
    formatted_name=get_formatted_name(first,last)
    print('\tnearly formatted name :'+formatted_name)

######################################################################
import unittest

from name_function import get_formatted_name
class NameTestCase(unittest.TestCase):#创建一个新类继承了unittest.TestCase
    def test_first_last_name(self):
        formatted_name=get_formatted_name('jains','joplin')
        self.assertEqual(formatted_name,'Jains Joplin')

unittest.main()#让python运行这个文件中的测试

'''
#########################测试类####################################################
import unittest

from survey import  AnonymousSurvey
class TestAnonmyyousSuevey(unittest.TestCase):
    def setUp(self):
        question = 'what is your favorate language?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Hanyu', 'Riyu']
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)


    def test_store_three_response(self):


        for response in self.responses:
            self.my_survey.store_response(response)
        #for response in responses:
            self.assertIn(response,self.my_survey.responses)
unittest.main()
