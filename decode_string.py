class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        input_str = s
        input_len = len(input_str)
        bracket_open_count = 0
        bracket_close_count = 0
        result_str = ""
        sub_count_str = ""
        for i in range(input_len):
            if bracket_open_count - bracket_close_count == 0:
                if input_str[i] in "0123456789":
                    sub_count_str += input_str[i]
                else:
                    result_str += input_str[i]            
            if input_str[i] == '[':
                bracket_open_count += 1
                if bracket_open_count - bracket_close_count == 1:
                    substr_start = i
                    result_str = result_str[:-1]
                    sub_count = int(sub_count_str)
                    sub_count_str = ""
            if input_str[i] == ']':
                bracket_close_count += 1
                if bracket_open_count - bracket_close_count == 0:
                    substr_stop = i
                    sub_str = input_str[substr_start+1:substr_stop]
                    result_str += sub_count * self.decodeString(sub_str)
        return result_str