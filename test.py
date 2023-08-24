#adasdf.@d

#unittest unit testing framework

import unittest
import email_validator


class Test_Email(unittest.TestCase):

  def test_valid_email_1(self):
    #email_list = {
    # '1dsfah@bsvd.com': "first character should be alphabet",
    #'wdhfhsaf@sfdd.in': "Right email!!",
    #'hsd ahg@gsdf.in': 'Wrong Email, space is there',
    #'as.adf@nb.com': 'Right email!!'
    #}
    #for input, output in email_list:
    result = email_validator.valid_email('1dsfah@bsvd.com')
    self.assertEqual(result, "first character should be alphabet")

  def test_valid_email_2(self):
    result = email_validator.valid_email('wdhfhsaf@sfdd.in')
    self.assertEqual(result, "Right email!!")

  def test_valid_email_3(self):
    result = email_validator.valid_email('as.adf@nb.com')
    self.assertEqual(result, "Right email!!")

  def test_valid_email_4(self):
    result = email_validator.valid_email('hsd ahg@gsdf.in')
    self.assertEqual(result, "Wrong Email, space is there")

  def test_valid_email_5(self):
    result = email_validator.valid_email('hsd#ahg@gsdf.in')
    self.assertEqual(result, "special charaters are not allowed")

  def test_valid_email_6(self):
    result = email_validator.valid_email('hsdahg@gsdfin')
    self.assertEqual(result, "'.' is not there")

  def test_valid_email_7(self):
    result = email_validator.valid_email('hsd@ahg@gsdf.in')
    self.assertEqual(result, "'@' error")

  def test_valid_email_8(self):
    result = email_validator.valid_email('hs@n')
    self.assertEqual(result, "Length should be graeater than 5")

  def test_valid_email_9(self):
    result = email_validator.valid_email('hsdahggsdf.in')
    self.assertEqual(result, "'@' error")


if __name__ == '__main__':
  unittest.main()
