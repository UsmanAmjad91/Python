What happens with negative indices in slicing?

Negative indices count from the end of a sequence:
-1 is the last character
-2 is the second-to-last
and so on...
This behavior works the same in slicing as it does in indexing.
Examples using slicing with negative indices
Let’s use the string:
my_string = "giraffe"
Example 1: Slice from -4 to -1
print(my_string[-4:-1]) # Output: "aff"

Explanation:
-4 = index of 'a'
-1 = index of 'e' (but not included in slice)
So the slice includes 'a', 'f', 'f'
Example 2: Slice from -3 to end
print(my_string[-3:]) # Output: "ffe"
Explanation:
-3 = 'f'
No second index = slice until end of string
Example 3: Slice the whole string using negative range
print(my_string[-7:-1]) # Output: "iraffe"
Starts at second character 'i' (index -7)
Ends before last character 'e' (index -1)
Example 4: Reversing a string using negative step
print(my_string[::-1]) # Output: "effarig"

Explanation:
The third value in slicing start:stop:step
A step of -1 reverses the string!
Caution: Slice boundaries must make sense
If start is after stop (without a negative step), you’ll get:
print(my_string[-1:-4]) # Output: ""
Nothing prints, because slicing goes left to right by default unless step is negative.
 Summary:
Negative indices count from the end of the string.
You can mix positive and negative indices.
Use [::-1] to reverse a string.
Slicing is always non-inclusive of the second index.