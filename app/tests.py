from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.

class TestAddCanHandleSimpleAddition(SimpleTestCase):
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

class TestAddPresentsFormIfNotGivenNumbersToAdd(SimpleTestCase):
    '''If add is not given two numbers, it should
    present the user with the add.html template
    and not try to compute an answer.'''

    def test_given_non_numeric_input(self):
        response = self.client.get(path=reverse('add'), data={'num1': 'a', 'num2': 'a'})
        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

class TestDoubleCanHandleSimpleDoubling(SimpleTestCase):
    def test_two_doubled(self):
        response = self.client.get(path=reverse('double'), data={'num': '2'})
        self.assertEqual(response.context['answer'], 4)

    def test_zero_doubled(self):
        response = self.client.get(path=reverse('double'), data={'num': '0'})
        self.assertEqual(response.context['answer'], 0)

    def test_negative_three_doubled(self):
        response = self.client.get(path=reverse('double'), data={'num': '-3'})
        self.assertEqual(response.context['answer'], -6)

class TestMultiplingCanHandleSimpleMultiplication(SimpleTestCase):
    def test_one_times_one_times_one(self):
        response = self.client.get(path=reverse('multthree'), data={'num1': '1', 'num2': '1', 'num3': '1'})
        self.assertEqual(response.context['answer'], 1)
