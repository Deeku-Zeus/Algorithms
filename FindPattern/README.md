# Algorithms to find a substring within a string

### 1. **Brute Force Algorithm**

**Approach**: This is the most straightforward way to search for a pattern in a string. It checks every possible position in the text where the pattern can appear, comparing the pattern character by character.

#### **Steps**:

1. **Start at the first position** of the text and assume the pattern starts there.
2. **Compare each character** of the pattern with the corresponding character in the text.
3. If all characters match, return the starting index of the match.
4. If there’s a mismatch, move the pattern one step to the right and repeat the process.
5. Continue this until you’ve checked every possible starting position in the text.
6. If no match is found by the end, return `-1`.




### 2. **Knuth-Morris-Pratt (KMP) Algorithm**

**Approach**: KMP improves on brute force by using information about previous comparisons to skip unnecessary checks. It does this using the **LPS (Longest Prefix Suffix)** array, which indicates how much the pattern can shift after a mismatch.

#### **Steps**:

**Step 1: Preprocessing (Build LPS Array)**

1. **Initialize an array `lps[]`** of the same length as the pattern.
2. **Fill the LPS array**:
    - For each index `i` in the pattern, compute the length of the longest proper prefix which is also a suffix for the substring ending at `i`.
    - If a mismatch occurs, use the previous value of `lps[]` to jump ahead in the pattern.

**Step 2: Pattern Matching** 3. **Start comparing** the pattern with the text from the beginning. 4. If there’s a match, move both the pattern and text pointers forward. 5. **When a mismatch occurs**:

- Use the `lps[]` array to shift the pattern based on the mismatch.
- Continue comparing until the entire pattern is found or the text ends.

6. If a full match is found, return the starting index.
7. If the end of the text is reached without finding a match, return `-1`.






### 3. **Rabin-Karp Algorithm**

**Approach**: Rabin-Karp uses hashing to compare the pattern and the substrings of the text. Instead of directly comparing characters, it compares hash values. It’s efficient when searching for multiple patterns at once.

#### **Steps**:

**Step 1: Preprocessing (Hash Calculation)**

1. **Calculate the hash value** for the pattern.
2. **Calculate the hash for the first window** of text, which has the same length as the pattern.

**Step 2: Pattern Matching** 3. **Slide the window** over the text, one character at a time. 4. For each new window, **recalculate the hash**:

- Use a rolling hash technique to efficiently update the hash by removing the leading character and adding the trailing character.

5. **If the hash values match**, do a character-by-character comparison to confirm the match (since different strings can have the same hash due to collisions).
6. **If a match is found**, return the starting index.
7. If the end of the text is reached and no match is found, return `-1`.







### 4. **Boyer-Moore Algorithm**

**Approach**: Boyer-Moore is efficient because it skips large parts of the text when mismatches occur. It uses two preprocessing strategies: the **Bad Character Rule** and the **Good Suffix Rule** (though we are only focusing on the bad character rule in this step-by-step breakdown).

#### **Steps**:

**Step 1: Preprocessing (Bad Character Table)**

1. **Build a table** (`bad_char`) that stores the last occurrence of each character in the pattern.
    - For each character in the pattern, record the rightmost position it appears in.

**Step 2: Pattern Matching** 2. **Start comparing** the pattern with the text from the rightmost character of the current window. 3. **If there’s a mismatch**:

- Check the bad character table for the mismatched character.
- Shift the pattern to align the last occurrence of this character in the pattern with the mismatched character in the text. If the character is not in the pattern, shift the pattern entirely beyond the mismatched character.

4. Repeat the process until either a match is found or you reach the end of the text.
5. If a match is found, return the starting index.
6. If the end of the text is reached without a match, return `-1`.








### 5. **Z Algorithm**

**Approach**: The Z algorithm efficiently finds all occurrences of a pattern in a text by constructing a **Z-array**, which stores the length of the longest substring starting from each position that matches the prefix of the concatenated pattern and text.

#### **Steps**:

**Step 1: Preprocessing (Concatenation and Z-Array Calculation)**

1. **Concatenate** the pattern, a special delimiter (`$`), and the text. The delimiter ensures no overlaps.
2. **Build the Z-array**:
    - For each position in the concatenated string, compute the length of the longest substring starting from that position that matches the prefix of the concatenated string.
    - If you already know part of the substring (from previous Z-array values), you can skip some comparisons.

**Step 2: Pattern Matching** 3. **Examine the Z-array**:

- If any Z-array value is equal to the length of the pattern, it means a match has been found at the corresponding position in the text.

4. If a match is found, return the starting index in the original text.
5. If no match is found by the end of the array, return `-1`.