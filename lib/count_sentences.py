#!/usr/bin/env python3
# FAILED MyString in count_sentences.py prints "The value must be a string." if not string. - AssertionError: assert '' == 'The value mu...e a string.\n'
# FAILED MyString in count_sentences.py returns True if value ends with a period and False otherwise. - TypeError: MyString() takes no arguments
# FAILED MyString in count_sentences.py returns True if value ends with a question mark and False otherwise. - TypeError: MyString() takes no arguments
# FAILED MyString in count_sentences.py returns True if value ends with an exclamation mark and False otherwise. - TypeError: MyString() takes no arguments
# FAILED MyString in count_sentences.py returns the number of sentences in the value. - TypeError: MyString() takes no arguments

# MyString in count_sentences.py is a class with the name "MyString". .                                                                                                                                                                         [ 16%]
# MyString in count_sentences.py prints "The value must be a string." if not string. F                                                                                                                                                          [ 33%]
# MyString in count_sentences.py returns True if value ends with a period and False otherwise. F                                                                                                                                                [ 50%]
# MyString in count_sentences.py returns True if value ends with a question mark and False otherwise. F                                                                                                                                         [ 66%]
# MyString in count_sentences.py returns True if value ends with an exclamation mark and False otherwise. F                                                                                                                                     [ 83%]
# MyString in count_sentences.py returns the number of sentences in the value. F 


# create the MyString class with a value property. The class should verify that the value is a string before assigning it, and the default value of value should be an empty string.

# class MyString:
#   def __init__(self, value=""):
#     self._value = ""
#     self.value = value

# @property
# def value(self):
#   return self._value

# @value.setter
# def value(self, new_value):
#   if isinstance(new_value, str):
#     self._value = new_value
#   else:
#     print("The value must be a string.")

# # Step 2: Implement is_sentence(), is_question(), and is_exclamation()
# # add the methods to check if the value ends with specific punctuation marks.    

# def is_sentence(self):
#   return self.value.endswith('.')

# def is_question(self):
#   return self.value.endswith('?')

# def is_exclamation(self):
#   return self.value.endswith('!')

# # Step 3: Implement count_sentences()
# # implement the count_sentences method. This method will count the number of sentences in the value, considering '.', '!', and '?' as sentence terminators.

# def count_sentences(self):
#   import re
#   # Split the string using a regular expression to find '.', '!', or '?'
#   sentences = re.split(r'[.!?]', self.value)
#   # Filter out any empty strings from the result
#   sentences = [s for s in sentences if s.strip()]
#   return len(sentences)

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        import re
        # Split the string using a regular expression to find '.', '!', or '?'
        sentences = re.split(r'[.!?]', self.value)
        # Filter out any empty strings from the result
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)









