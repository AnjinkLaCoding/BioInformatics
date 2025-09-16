def hamming_distance(s1, s2):
    """Calculate Hamming distance between two strings of equal length."""
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def find_approximate_matches(text, pattern, max_mismatches):
    """Find all positions where pattern occurs in text with at most max_mismatches."""
    matches = []
    pattern_len = len(pattern)
    text_len = len(text)
    
    # Check each possible position in the text
    for i in range(text_len - pattern_len + 1):
        substring = text[i:i + pattern_len]
        if hamming_distance(pattern, substring) <= max_mismatches:
            matches.append(i)
    
    return matches

def multiple_approximate_pattern_matching(text, patterns, d):
    results = {}
    for pattern in patterns:
        matches = find_approximate_matches(text, pattern, d)
        results[pattern] = matches
    return results

def format_output(results):
    output_lines = []
    for pattern, positions in results.items():
        if positions:
            positions_str = ' '.join(map(str, positions))
            output_lines.append(f"{pattern}: {positions_str}")
        else:
            output_lines.append(f"{pattern}:")
    return '\n'.join(output_lines)

def read_input_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines if line.strip()]
    
    if len(lines) < 3:
        raise ValueError("Input file must contain at least 3 lines: text, patterns, and d")
    
    text = lines[0]
    patterns = lines[1].split()
    d = int(lines[2])
    
    return text, patterns, d

def solve_from_file(filename, output_filename=None):
    try:
        text, patterns, d = read_input_from_file(filename)
        results = multiple_approximate_pattern_matching(text, patterns, d)
        output = format_output(results)
        if output_filename:
            with open(output_filename, 'w') as file:
                file.write(output)
            print(f"Output saved to: {output_filename}")
        else:
            print("Output:")
            print(output)
        
        return results
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error processing file: {e}")

res = solve_from_file("C:/Users/Matthew/Downloads/dataset_30230_10 (1).txt", 'C:/Users/Matthew/Downloads/Sol.txt')