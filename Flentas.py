from collections import Counter

# Function to check if two frequency counters are equal
def matches(counter1, counter2):
    for key in counter1:
        if counter1[key] != counter2.get(key, 0):
            return False
    return True

def find_permutations(pattern, text):
    # Lengths of pattern and text
    len_pat = len(pattern)
    len_txt = len(text)
    
    # Frequency counter for the pattern
    pattern_count = Counter(pattern)
    
    # Frequency counter for the current window in the text
    window_count = Counter(text[:len_pat])
    
    # Check the first window
    if matches(pattern_count, window_count):
        return "YES"
    
    # Sliding the window over the text
    for i in range(len_pat, len_txt):
        # Add the next character to the window
        window_count[text[i]] += 1
        
        # Remove the character that is sliding out of the window
        window_count[text[i - len_pat]] -= 1
        
        # If the count becomes 0, we remove the character from the window count
        if window_count[text[i - len_pat]] == 0:
            del window_count[text[i - len_pat]]
        
        # Check if the current window matches the pattern's frequency count
        if matches(pattern_count, window_count):
            return "YES"
    
    return "NO"

def solve():
    # Read number of test cases
    T = int(input())
    
    # Iterate through each test case
    for _ in range(T):
        # Read the pattern and the text
        pattern = input().strip()
        text = input().strip()
        
        # Output the result for each test case
        print(find_permutations(pattern, text))

# Entry point of the program
if __name__ == "__main__":
    solve()
