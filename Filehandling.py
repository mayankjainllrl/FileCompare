"""
Small File handling project.
Credential :- Mayank Jain
Contact :- mayankjainllrl@gmail.com
"""
IDENTICAL = -1


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    idx = 0
    for ch1, ch2 in zip(line1, line2):
        if ch1 != ch2:
            return idx
        idx += 1
    if len(line1) != len(line2):
        return min(len(line1), len(line2))
    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    lst = ["\n" in line1, "\r" in line1,
           "\n" in line2, "\r" in line2]
    if any(lst) or not (0 <= idx <= min(len(line1), len(line2))):
        return ""
    else:
        return "{}\n{}\n{}\n".format(line1, "=" * idx + "^", line2)


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if lines1 == lines2:
        return IDENTICAL, IDENTICAL
    for line1, line2 in zip(lines1, lines2):
        val = singleline_diff(line1, line2)
        if val != IDENTICAL:
            return lines2.index(line2), val
    return min(len(lines1), len(lines2)), 0


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    with open(filename, "r") as file:
        result = [line.strip("\n, \r") for line in file]
    return result


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    res = multiline_diff(lines1, lines2)
    if res == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    if not lines1:
        lines1.append("")
    else:
        lines2.append("")
    return f"Line {res[0] + 1}:\n{singleline_diff_format(lines1[res[0]], lines2[res[0]], res[1])}"


print(file_diff_format("abc.txt", "def.txt"))
