def logincheck(uname,pwd):
    if(uname=='admin' and pwd=='admin123'):
        return 'login success'
    if(uname!='admin' and pwd=='admin123'):
        return 'login fail'
    if(uname=='admin' and pwd!='admin123'):
        return 'login fail'
    if(uname!='admin' and pwd!='admin123'):
        return 'login fail'

import unittest
class logincheck(unittest.TestCase):
    def test1(self):
        result = logincheck('admin','admin123')
        self.assertEqual(result,' login success')
    def test2(self):
        result = logincheck('admin1','admin123')
        self.assertEqual(result,'login fail')
    def test3(self):
        result = logincheck('admin','admin1234')
        self.assertEqual(result,'login fail')
    def test4(self):
        result = logincheck('admin1','admn1234')
        self.assertEqual(result,'login fail')

if __name__ == '__main__':
    unittest.main()
        
