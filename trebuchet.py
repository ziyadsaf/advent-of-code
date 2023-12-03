"""
1. read each file line
2. two pointers for each line
3. pointer moves across
4. when pointer reaches a number stop and append to list
5. need to append to list as a single number...
"""

def append_numbers(numbers=[],single_digit_numbers=[]):
    with open("data.csv") as data:
        for line in data:
            line_of_data = line.split()
            for word in line_of_data:
                left = 0
                right = len(word) - 1
                while left < right and not word[left].isdigit():
                    left += 1

                while right > left and not word[right].isdigit():
                    right -= 1
                        
                if left < right:
                    # Append the combined number to the list
                    combined_number = str(word[left]) + str(word[right])
                    numbers.append(int(combined_number))
                
                elif left == right and word[left].isdigit():
                    # If only one digit is present, store it for later
                    single_digit_numbers.append(int(word[left]))
                
                elif left == right and word[right].isdigit():
                    # If only one digit is present, store it for later
                    single_digit_numbers.append(int(word[right]))

    # Append the single-digit numbers
    numbers.extend(single_digit_numbers)

    return numbers, sum(numbers)
print(append_numbers())
                    

