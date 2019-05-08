import unittest
from solution import net_pay_cal

class TestNetpayCalculator(unittest.TestCase):

    def test_pay_below_first_tax_bracket(self):
        self.assertEqual(net_pay_cal(230000), 218500, msg="Check values for first tax bracket")

    def test_pay_at_upper_limit_first_tax_bracket(self):
        self.assertEqual(net_pay_cal(234999), 223249.05, msg="Check values for upper tax bracket")

    def test_pay_at_lower_limit_second_tax_bracket(self):
        self.assertEqual(net_pay_cal(235000), 199750)
    
    def test_pay_between_second_tax_bracket(self):
        self.assertEqual(net_pay_cal(300000), 255000)
    
    def test_pay_at_upper_limit_second_tax_bracket(self):
        self.assertEqual(net_pay_cal(334999), 284749.14999999997)

    def test_pay_at_lower_limit_third_tax_bracket(self):
        self.assertEqual(net_pay_cal(335000), 284750)

    def test_pay_between_third_tax_bracket(self):
        self.assertEqual(net_pay_cal(390000), 349500)

    def test_pay_at_upper_limit_of_third_tax_bracket(self):
        self.assertEqual(net_pay_cal(409999), 364499.25)
    
    def test_pay_at_lower_limit_fourth_tax_bracket(self):
        self.assertEqual(net_pay_cal(410000), 364500)

    def test_pay_between_fourth_tax_bracket(self):
        self.assertEqual(net_pay_cal(750000), 585500)

    def test_pay_between_fourth_tax_bracket_0(self):
        self.assertEqual(net_pay_cal(1700000), 1203000)

    def test_pay_between_fourth_tax_bracket_1(self):
        self.assertEqual(net_pay_cal(6300000), 4193000)
    
    def test_pay_between_fourth_tax_bracket_2(self):
        self.assertEqual(net_pay_cal(6615000), 4397750)
    
    def test_pay_at_upper_limit_fourth_tax_bracket(self):
        self.assertEqual(net_pay_cal(9999999), 6597999.3500000015)
    
    def test_pay_at_lower_limit_fifth_tax_bracket(self):
        self.assertEqual(net_pay_cal(10000000), 6598000)

    def test_pay_above_fifth_tax_bracket_0(self):
        self.assertEqual(net_pay_cal(11000000), 7148000)
    
    def test_pay_above_fifth_tax_bracket_1(self):
        self.assertEqual(net_pay_cal(12000000), 7698000)

    def test_pay_above_fift_tax_bracket_2(self):
        self.assertEqual(net_pay_cal(20000000), 12098000)

if __name__ == "__main__":
    unittest.main()
