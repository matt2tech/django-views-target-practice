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

class TestEarningsWorksWithRealNumbers(SimpleTestCase):
    '''If earnings is given three numbers it should
    render earnings.html with total of 
    num1 * 15 + num2 * 12 + num3 * 9'''

    def test_total_1(self):
        response = self.client.get(path=reverse('earnings'), data={'num1': '1', 'num2': '1', 'num3': '1'})
        self.assertEqual(response.context['answer'], 36)

    def test_total_2(self):
        response = self.client.get(path=reverse('earnings'), data={'num1': '0', 'num2': '0', 'num3': '0'})
        self.assertEqual(response.context['answer'], 0)

    def test_total_3(self):
        response = self.client.get(path=reverse('earnings'), data={'num1': '5', 'num2': '10', 'num3': '8'})
        self.assertEqual(response.context['answer'], 267)

class TestEarningsWithoutNumbers(SimpleTestCase):
    '''If earnings is not given three numbers, it should
    present the user with the earnings.html template
    and not try to compute an answer.'''

    def test_given_non_numeric_input1(self):
        response = self.client.get(path=reverse('earnings'), data={'num1': 'a', 'num2': 'a','num3': 'a'})
        self.assertTemplateUsed(response, 'app/earnings.html')
        self.assertNotIn('answer', response.context)

    def test_given_non_numeric_input2(self):
        response = self.client.get(path=reverse('earnings'), data={'num1': '', 'num2': '1', 'num3': 'a'})
        self.assertTemplateUsed(response, 'app/earnings.html')
        self.assertNotIn('answer', response.context)

    def test_given_non_numeric_input3(self):
        response = self.client.get(path=reverse('earnings'), data={'num1': '', 'num2': '', 'num3': ''})
        self.assertTemplateUsed(response, 'app/earnings.html')
        self.assertNotIn('answer', response.context)

    def test_given_non_numeric_input4(self):
        response = self.client.get(path=reverse('earnings'), data={'num1': '-1', 'num2': '-4', 'num3': '5'})
        self.assertTemplateUsed(response, 'app/earnings.html')
        self.assertNotIn('answer', response.context)

class TestBothWithRealBools(SimpleTestCase):
    '''If both is given two bools it should
    render both.html with true or false'''

    def test_true_or_false_1(self):
        response = self.client.get(path=reverse('both'), data={'bool1': 'True', 'bool2': 'False'})
        self.assertEqual(response.context['answer'], False)

    def test_true_or_false_2(self):
        response = self.client.get(path=reverse('both'), data={'bool1': 'False', 'bool2': 'False'})
        self.assertEqual(response.context['answer'], False)

    def test_true_or_false_3(self):
        response = self.client.get(path=reverse('both'), data={'bool1': 'False', 'bool2': 'True'})
        self.assertEqual(response.context['answer'], False)

    def test_true_or_false_4(self):
        response = self.client.get(path=reverse('both'), data={'bool1': 'True', 'bool2': 'True'})
        self.assertEqual(response.context['answer'], True)

class TestBothWithoutBools(SimpleTestCase):
    '''If both is not given two bools, it should
    present the user with the both.html template
    and render false.'''

    def test_given_non_bools_1(self):
        response = self.client.get(path=reverse('both'), data={'bool1': '', 'bool2': False})
        self.assertEqual(response.context['answer'], False)

    def test_given_non_bools_2(self):
        response = self.client.get(path=reverse('both'), data={'bool1': '', 'bool2': True})
        self.assertEqual(response.context['answer'], False)

    def test_given_non_bools_3(self):
        response = self.client.get(path=reverse('both'), data={'bool1': '', 'bool2': ''})
        self.assertEqual(response.context['answer'], False)

class TestWalkOrDriveWithGoodInputs(SimpleTestCase):
    '''If WalkOrDrive is given a num and
    a bool it should render walk-or-drive.html
    with walk or drive'''

    def test_walk_or_drive_1(self):
        response = self.client.get(path=reverse('walk-or-drive'), data={'num': 0.25, 'bool': 'True'})
        self.assertEqual(response.context['answer'], 'walk')

    def test_walk_or_drive_2(self):
        response = self.client.get(path=reverse('walk-or-drive'), data={'num': 0.26, 'bool': 'True'})
        self.assertEqual(response.context['answer'], 'drive')

    def test_walk_or_drive_3(self):
        response = self.client.get(path=reverse('walk-or-drive'), data={'num': 0.25, 'bool': 'False'})
        self.assertEqual(response.context['answer'], 'drive')

    def test_walk_or_drive_1(self):
        response = self.client.get(path=reverse('walk-or-drive'), data={'num': 0.26, 'bool': 'False'})
        self.assertEqual(response.context['answer'], 'drive')

class TestWalkOrDriveWithBadInputs(SimpleTestCase):
    '''If WalkOrDrive is not given a num, it should
    present the user with the walk-or-drive.html template
    and not try to compute an answer. If WalkOrDrive is
    not given a bool, it should present the user with
    the walk-or-drive.html template and render drive'''

    def test_given_non_numeric_input1(self):
        response = self.client.get(path=reverse('walk-or-drive'), data={'num': 'a', 'bool': 'False'})
        self.assertTemplateUsed(response, 'app/walk-or-drive.html')
        self.assertNotIn('answer', response.context)

    def test_given_non_numeric_input2(self):
        response = self.client.get(path=reverse('walk-or-drive'), data={'num': '', 'bool': 'False'})
        self.assertTemplateUsed(response, 'app/walk-or-drive.html')
        self.assertNotIn('answer', response.context)

    def test_given_non_numeric_input3(self):
        response = self.client.get(path=reverse('walk-or-drive'), data={'num': '1', 'bool': ''})
        self.assertEqual(response.context['answer'], 'drive')

    def test_given_non_numeric_input4(self):
        response = self.client.get(path=reverse('walk-or-drive'), data={'num': '1', 'bool': 'a'})
        self.assertEqual(response.context['answer'], 'drive')


