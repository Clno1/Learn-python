'''
测试AnonymousSurvey类
①import unittest，然后测试类继承unittest.TestCase
②测试方法必须要以test_开头
③setUp()方法会在最开始运行，然后才是tes_开头的方法
'''
import unittest

from language_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question="What language did you first learn?"
        self.my_survey=AnonymousSurvey(question)
        self.reponse=["English","Chinese","None"]

    def test_single(self):
        self.my_survey.store_response(self.reponse[0])
        self.assertIn(self.reponse[0],self.my_survey.responses)

    def test_three(self):
        for rep in self.reponse:
            self.my_survey.store_response(rep)
        for rep in self.reponse:
            self.assertIn(rep,self.my_survey.responses)


unittest.main()
