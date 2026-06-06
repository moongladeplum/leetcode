from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])  # Length of each word
        total_words = len(words)   # Number of words
        window_len = word_len * total_words  # Total length to check
        
        # Count frequency of each word in words
        word_count = Counter(words)
        
        result = []
        
        # Try each possible starting position in first word_len characters
        # This handles different alignments of word boundaries
        for i in range(word_len):
            left = i  # Left boundary of our sliding window
            right = i  # Right boundary
            seen = Counter()  # Words we've seen in current window
            count = 0  # Number of valid words in current window
            
            while right + word_len <= len(s):
                # Get the next word
                word = s[right:right + word_len]
                right += word_len
                
                # If this word is in our target words
                if word in word_count:
                    seen[word] += 1
                    count += 1
                    
                    # If we have too many of this word, move left pointer
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # If we found all words, record the starting index
                    if count == total_words:
                        result.append(left)
                        
                        # Remove leftmost word and continue
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                
                # If word is not in our target words, reset everything
                else:
                    seen.clear()
                    count = 0
                    left = right
        
        return result
