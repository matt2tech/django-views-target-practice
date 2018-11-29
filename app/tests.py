from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.

class TestAddCanHandleSimpleAddition(SimpleTestCase):
    '''If add is given two numbers it should
    render add.html with sum of those numbers'''

    def test_two_plus_two(self):
        response = self.client.get(path=reverse('add'), data={'num1': '2', 'num2': '2'})
        self.assertEqual(response.context['answer'], 4)

    def test_zero_plus_zero(self):
        response = self.client.get(path=reverse('add'), data={'num1': '0', 'num2': '0'})
        self.assertEqual(response.context['answer'], 0)

    def test_two_dot_three_plus_one_dot_two(self):
        response = self.client.get(path=reverse('add'), data={'num1': '2.3', 'num2': '1.2'})
        self.assertEqual(response.context['answer'], 3.5)

    def test_two_plus_negative_one(self):
        response = self.client.get(path=reverse('add'), data={'num1': '2', 'num2': '-1'})
        self.assertEqual(response.context['answer'], 1)

    def test_negative_one_plus_two(self):
        response = self.client.get(path=reverse('add'), data={'num1': '-1', 'num2': '2'})
        self.assertEqual(response.context['answer'], 1)

    def test_negative_two_plus_negative_three(self):
        response = self.client.get(path=reverse('add'), data={'num1': '-2', 'num2': '-3'})
        self.assertEqual(response.context['answer'], -5)

class TestAddWithoutNumbers(SimpleTestCase):
    '''If add is not given two numbers, it should
    present the user with the add.html template
    and not try to compute an answer.'''

    def test_given_non_numeric_input1(self):
        response = self.client.get(path=reverse('add'), data={'num1': 'a', 'num2': 'a'})
        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

    def test_given_non_numeric_input2(self):
        response = self.client.get(path=reverse('add'), data={'num1': '', 'num2': '1'})
        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

    def test_given_non_numeric_input3(self):
        response = self.client.get(path=reverse('add'), data={'num1': '1', 'num2': ''})
        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

    def test_given_non_numeric_input4(self):
        response = self.client.get(path=reverse('add'), data={'num1': '', 'num2': ''})
        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

class TestDoubleCanHandleSimpleDoubling(SimpleTestCase):
    '''If double is given a number it should
    render double.html with product of number times
    two'''

    def test_four_doubled(self):
        response = self.client.get(path=reverse('double'), data={'num': '4'})
        self.assertEqual(response.context['answer'], 8)

    def test_zero_doubled(self):
        response = self.client.get(path=reverse('double'), data={'num': '0'})
        self.assertEqual(response.context['answer'], 0)

    def test_negative_four_doubled(self):
        response = self.client.get(path=reverse('double'), data={'num': '-4'})
        self.assertEqual(response.context['answer'], -8)

    def test_two_dot_two_doubled(self):
        response = self.client.get(path=reverse('double'), data={'num': '2.2'})
        self.assertEqual(response.context['answer'], 4.4)

    def test_eight_doubled(self):
        response = self.client.get(path=reverse('double'), data={'num': '8'})
        self.assertEqual(response.context['answer'], 16)

    def test_one_doubled(self):
        response = self.client.get(path=reverse('double'), data={'num': '1'})
        self.assertEqual(response.context['answer'], 2)

class TestDoubleWithoutNumbers(SimpleTestCase):
    '''If double is not given a number, it should
    present the user with the double.html template
    and not try to compute an answer.'''

    def test_given_non_numeric_input1(self):
        response = self.client.get(path=reverse('double'), data={'num': 'a'})
        self.assertTemplateUsed(response, 'app/double.html')
        self.assertNotIn('answer', response.context)

    def test_given_non_numeric_input2(self):
        response = self.client.get(path=reverse('double'), data={'num': ''})
        self.assertTemplateUsed(response, 'app/double.html')
        self.assertNotIn('answer', response.context)

class TestMultiplingCanHandleSimpleMultiplication(SimpleTestCase):
    '''If multthree is given three numbers it should
    render multthree.html with product of those numbers'''

    def test_one_times_one_times_one(self):
        response = self.client.get(path=reverse('multthree'), data={'num1': '1', 'num2': '1', 'num3': '1'})
        self.assertEqual(response.context['answer'], 1)

    def test_negative_one_times_two_times_three(self):
        response = self.client.get(path=reverse('multthree'), data={'num1': '-1', 'num2': '2', 'num3': '3'})
        self.assertEqual(response.context['answer'], -6)
    
    def test_negative_two_times_negative_four_times_one(self):
        response = self.client.get(path=reverse('multthree'), data={'num1': '-2', 'num2': '-4', 'num3': '1'})
        self.assertEqual(response.context['answer'], 8)

    def test_negative_one_times_zero_times_one(self):
        response = self.client.get(path=reverse('multthree'), data={'num1': '-1', 'num2': '0', 'num3': '1'})
        self.assertEqual(response.context['answer'], 0)
    
    def test_negative_one_times_negative_one_times_negative_one(self):
        response = self.client.get(path=reverse('multthree'), data={'num1': '-1', 'num2': '-1', 'num3': '-1'})
        self.assertEqual(response.context['answer'], -1)

class TestMultipingWithoutNumbers(SimpleTestCase):
    '''If multthree is not given three numbers, it should
    present the user with the multthree.html template
    and not try to compute an answer.'''

    def test_given_non_numeric_input1(self):
        response = self.client.get(path=reverse('multthree'), data={'num1': 'a', 'num2': 'a','num3': 'a'})
        self.assertTemplateUsed(response, 'app/multthree.html')
        self.assertNotIn('answer', response.context)

    def test_given_non_numeric_input2(self):
        response = self.client.get(path=reverse('multthree'), data={'num1': '', 'num2': '1', 'num3': 'a'})
        self.assertTemplateUsed(response, 'app/multthree.html')
        self.assertNotIn('answer', response.context)

    def test_given_non_numeric_input3(self):
        response = self.client.get(path=reverse('multthree'), data={'num1': '', 'num2': '', 'num3': ''})
        self.assertTemplateUsed(response, 'app/multthree.html')
        self.assertNotIn('answer', response.context)
