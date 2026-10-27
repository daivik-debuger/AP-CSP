import sys

def solve():
    cowphabet = sys.stdin.readline().strip()
    heard_str = sys.stdin.readline().strip()
    
    char_to_index = {char: idx for idx, char in enumerate(cowphabet)}
    
    hum_count = 1
    
    for i in range(1, len(heard_str)):
        curr_idx = char_to_index[heard_str[i]]
        prev_idx = char_to_index[heard_str[i - 1]]
          
        if curr_idx <= prev_idx:
            hum_count += 1     
    print(hum_count)
    
if __name__ == '__main__':
    solve()

