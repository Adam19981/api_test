import unittest
from HTMLTestRunner import HTMLTestRunner
from setting import Test_report_PATH,login_info
from api.user_manager import UserManger




if __name__ == '__main__':

    user = UserManger()
    user.login(login_info.get('username'),login_info.get('password'))

    suite = unittest.TestLoader().discover('./cases','test*.py')

    with open(Test_report_PATH,'wb') as f:

        runner = HTMLTestRunner(f,title='测试报告')
        runner.run(suite)
