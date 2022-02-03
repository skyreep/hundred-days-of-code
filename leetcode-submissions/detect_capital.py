class Solution(object):
    def detectCapitalUse(self, word):
        all_caps = True
        all_lower = True
        # Disqualify title case if the first letter isn't capitalized
        if word[0].isupper():
            title_case = True
        else: 
            title_case = False
        # Test the characters for correct capitalization usage
        for index, char in enumerate(word):
            if char.islower():
                all_caps = False
            elif char.isupper():
                all_lower = False
            if index != 0 and title_case:
                if char.isupper():
                    title_case = False

        if all_caps or all_lower or title_case:
            return True
        else:
            return False