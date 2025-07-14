from collections import Counter

# Read input
topics = input("Enter the String").split()

# Count occurrences of each topic (case-sensitive)
topic_counts = Counter(topics)

# Convert to lowercase and recount (case-insensitive)
lowercase_counts = Counter(topic.lower() for topic in topics)

# Print results in alphabetical order
for topic in sorted(lowercase_counts):
    print(f"{topic}-{lowercase_counts[topic]}")   