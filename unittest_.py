import unittest


def string_words(string):
    words = string.split()
    return words

def palindrome(palindrome):
    reversed_string = palindrome[::-1]
    if palindrome == reversed_string:
        return f"{palindrome} є паліндромом"
    else:
        return f"{palindrome} не є паліндромом"


def prime_difficult(number):
    if number % 2 != 0 and number >= 1:
        return True
    
    
class Test(unittest.TestCase):
        
    def test_string_words(self):
        self.assertEqual(string_words('ad kd'), ['ad', 'kd'])
        self.assertEqual(string_words('ad kds dd s'), ['ad', 'kds', 'dd', 's'])
        self.assertEqual(string_words('ad kd fs skjfhskfjh'), ['ad', 'kd', 'fs', 'skjfhskfjh'])

    def test_palindrome(self):
        palindrome_name = ["assa", 'asa', 'lal', 'pop', 'oppppo', 'uiiu', 'qwqwqwwqwqwq']
        for i in range(len(palindrome_name)):
            self.assertEqual(palindrome(palindrome_name[i]), f"{palindrome_name[i]} є паліндромом")

    def test_prime_difficult(self):
        for i in range(1, 100000, 2):
            self.assertEqual(prime_difficult(i), True)
        

if __name__ == '__main__':
    unittest.main()