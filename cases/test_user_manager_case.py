import unittest
from api.user_manager import UserManger




class TestUserManagerCase(unittest.TestCase):

    user_id = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManger()

        cls.username = cls.password = 'ming77'
        cls.new_username = cls.new_password = 'ming88'




    def test01_normal_add(self):
        #用例数据


        #添加管理员接口
        actual_result = self.user.add_user(self.username,self.password)
        print(actual_result)
        actual_result['errno']
        data = actual_result.get('data')
        if data:
            TestUserManagerCase.user_id = data.get('id')
        # 返回数据的校验
        self.assertEqual(0,actual_result['errno'])
        self.assertEqual(self.username,data.get('username'))
        # 提取id值

    def test02_edit(self):

        actul_result = self.user.edit_user(TestUserManagerCase.user_id,self.new_username,password=self.new_password)

        self.assertEqual(0,actul_result['errno'])
        self.assertEqual(self.new_username,actul_result.get('data').get('username'))


    def test03_search(self):

        actul_result = self.user.search_user()
        self.assertEqual(0,actul_result.get('errno'))




    def test04_delete(self):

        actul_result = self.user.del_user(TestUserManagerCase.user_id,self.username,self.password)

        self.assertEqual(0,actul_result.get('errno'))






if __name__ == '__main__':
    unittest.main()