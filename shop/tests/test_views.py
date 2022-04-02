from django.test import TestCase
from django.urls import reverse

# class ViewsTestCase(TestCase):
    

#     def test_register(self):
#         result = register()
#         self.assertEqual()
#         pass


# class UrlTestCase(TestCase):
#     """Тесты урлов"""

#     def test_home_url(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)


#     def test_filter_url(self):
#         response = self.client.get('/filter')
#         self.assertEqual(response.status_code, 200)
    
#     def test_cart_url(self):
#         response = self.client.get('/cart/')
#         self.assertEqual(response.status_code, 200)

#     def test_shop_slug_cat_url(self):
#         response = self.client.get('/shop/noutbuki')
#         self.assertEqual(response.status_code, 200)
#         response = self.client.get('/shop/smartfony')
#         self.assertEqual(response.status_code, 200)
#         response = self.client.get('/shop/naushniki')
#         self.assertEqual(response.status_code, 200)
        
#     # def test_shop_slug_product_url(self):
#     #     response = self.client.get('/single/megatron-1000')
#     #     # print('*******почему-то не работает*********', response)
#     #     self.assertEqual(response.status_code, 200)
        
#     # def test_review_url(self):
#     #     response = self.client.get('/review/4/')
#     #     # print('********почему-то не работает*********', response)
#     #     self.assertEqual(response.status_code, 200)
        
#     def test_about_url(self):
#         response = self.client.get('/about/')
#         self.assertEqual(response.status_code, 200)

#     def test_contact_url(self):
#         response = self.client.get('/contact/')
#         self.assertEqual(response.status_code, 200)

#     def test_register_url(self):
#         response = self.client.get('/register/')
#         self.assertEqual(response.status_code, 200)

#     def test_login_url(self):
#         response = self.client.get('/login/', 
#             {
#             'email': 'user@gmail.com', 
#             'password1': '123ASDasd11', 
#             'password2': '123ASDasd11'
#             }
#         )
#         self.assertEqual(response.status_code, 200)

#     # def test_login_url(self):
#     #     response = self.client.get('/login/')
#     #     response.login(email='user@gmail.com', password1='123ASDasd11', password2='123ASDasd11')
#     #     self.assertEqual(response.status_code, 200)

#     def test_logout_url(self):
#         response = self.client.get('/logout/')
#         self.assertEqual(response.status_code, 302)


class ProductVievTestCase(TestCase):


    def test_url_shop(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)

    def test_url_shop_name(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/shop.html')
        print(response.context)


# class CategoryVievTestCase(TestCase):


#     def test_url_shop(self):
#         response = self.client.get('/shop/noutbuki')
#         self.assertEqual(response.status_code, 200)
#         response = self.client.get('/shop/smartfony')
#         self.assertEqual(response.status_code, 200)

#     def test_url_shop_name(self):
#         response = self.client.get(reverse('category'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'shop/shop.html')
