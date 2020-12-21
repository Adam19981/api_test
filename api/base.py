# 实现所有接口的请求

import requests
from loguru import logger
from cacheout import Cache
from setting import BASE_URL



cache = Cache()

class base():

# 实现URL的拼接
    def get_url(self,path,params=None):
       if params:
            full_path = BASE_URL + path +params
            return full_path
       return BASE_URL + path


 # 实现请求头信息的管理

    def get_headers(self):

        headers = {'Content-Type':'application/json'}
    #提取token
        token = cache.get('token')
        if token:
            headers.update({'X-Litemall-Admin-Token':token})
        logger.warning('请求头信息返回数据:{},注意多数接口需要token'.format(headers))
        return headers


# get方法
    def get(self,url):
        result = None
        response = requests.get(url,headers=self.get_headers())

        try:
            result = response.json()
            logger.info('请求get方法返回结果:{}'.format(result))
            return result
        except Exception as e:
            logger.error('请求get方法异常，返回结果:{}'.format(result))
# post 方法
    def post(self,url,data):


        result = None
        response = requests.post(url,json=data,headers=self.get_headers())

        try:
            result = response.json()
            logger.info('请求post方法返回结果:{}'.format(result))
            return result
        except Exception as e:
            logger.error('请求post方法异常，返回结果:{}'.format(result))



    # 实现登录方法
    def login(self,username,password):

        login_path = '/admin/auth/login'
        login_url = self.get_url(login_path)
        login_data = {'username':username,'password':password}
        result = self.post(login_url,login_data)

        try:
            if 0 == result.get('errno'):
                logger.info('请求登录接口成功')
                token = result.get('data').get('token')
                cache.set('token',token)
            else:
                logger.info('请求登录接口失败')
                return None


        except Exception as e:
            logger.error('请求登录接口异常')


if __name__ == '__main__':


    ba = base()
    ba.login("admin123","admin123")



