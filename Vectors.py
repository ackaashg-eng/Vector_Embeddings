
import math
import matplotlib.pyplot as plt


# STEP 1: Create the dataset
data = {
    # Technology
    "computer": {"category": "Technology", "vector": [2, 5]},
    "laptop": {"category": "Technology", "vector": [3, 5]},
    "python": {"category": "Technology", "vector": [4, 6]},
    "keyboard": {"category": "Technology", "vector": [2, 4]},
    "internet": {"category": "Technology", "vector": [5, 7]},

    # Food
    "pizza": {"category": "Food", "vector": [6, 2]},
    "burger": {"category": "Food", "vector": [7, 2]},
    "rice": {"category": "Food", "vector": [5, 1]},
    "apple": {"category": "Food", "vector": [4, 2]},
    "bread": {"category": "Food", "vector": [5, 3]},

    # Animals
    "cat": {"category": "Animals", "vector": [2, 3]},
    "dog": {"category": "Animals", "vector": [3, 4]},
    "lion": {"category": "Animals", "vector": [4, 5]},
    "tiger": {"category": "Animals", "vector": [5, 5]},
    "elephant": {"category": "Animals", "vector": [3, 6]},

    # Sports
    "football": {"category": "Sports", "vector": [7, 5]},
    "cricket": {"category": "Sports", "vector": [6, 5]},
    "tennis": {"category": "Sports", "vector": [7, 6]},
    "swimming": {"category": "Sports", "vector": [5, 6]},
    "basketball": {"category": "Sports", "vector": [8, 5]},

    # Vehicles
    "car": {"category": "Vehicles", "vector": [9, 1]},
    "bus": {"category": "Vehicles", "vector": [8, 2]},
    "train": {"category": "Vehicles", "vector": [9, 3]},
    "bicycle": {"category": "Vehicles", "vector": [7, 1]},
    "motorcycle": {"category": "Vehicles", "vector": [8, 1]}
}


# STEP 2: Calculate the Euclidean distance
def calculate_distance(vector1, vector2):
    total = 0

    for i in range(len(vector1)):
        difference = vector1[i] - vector2[i]
        total += difference ** 2

    return math.sqrt(total)


# STEP 3: Display words, vectors, and dimensions
def display_dataset():
    print("\n--- TEXT-TO-VECTOR DATASET ---")

    for word, details in data.items():
        vector = details["vector"]
        category = details["category"]
        dimensions = len(vector)

        print(f"Word: {word}")
        print(f"Category: {category}")
        print(f"Vector: {vector}")
        print(f"Vector dimensions: {dimensions}")


# STEP 4: Compare two vectors
def compare_vectors():
    word1 = input("Enter the first word: ").strip().lower()
    word2 = input("Enter the second word: ").strip().lower()

    if word1 not in data or word2 not in data:
        print("One or both words are not in the dataset.")
        return

    vector1 = data[word1]["vector"]
    vector2 = data[word2]["vector"]

    distance = calculate_distance(vector1, vector2)

    print(f"\n{word1}: {vector1}")
    print(f"{word2}: {vector2}")
    print(f"Dimensions of {word1}: {len(vector1)}")
    print(f"Dimensions of {word2}: {len(vector2)}")
    print(f"Distance: {distance:.2f}")

    if distance == 0:
        print("Both vectors have identical coordinates.")
    else:
        print("A smaller distance means the vectors are closer.")


# STEP 5: Find the closest pair of vectors
def find_closest_vectors():
    words = list(data.keys())
    smallest_distance = float("inf")
    closest_pair = None

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i]
            word2 = words[j]

            vector1 = data[word1]["vector"]
            vector2 = data[word2]["vector"]

            distance = calculate_distance(vector1, vector2)

            if distance < smallest_distance:
                smallest_distance = distance
                closest_pair = (word1, word2)

    print("\n--- CLOSEST VECTORS ---")
    print("First word:", closest_pair[0])
    print("Second word:", closest_pair[1])
    print("First vector:", data[closest_pair[0]]["vector"])
    print("Second vector:", data[closest_pair[1]]["vector"])
    print(f"Distance: {smallest_distance:.2f}")


# STEP 6: Visualize vectors in 2D
def visualize_vectors():
    plt.figure(figsize=(10, 7))

    for word, details in data.items():
        vector = details["vector"]
        x = vector[0]
        y = vector[1]

        plt.scatter(x, y)
        plt.annotate(word, (x, y), xytext=(5, 5),
                     textcoords="offset points", fontsize=8)

    plt.title("Text-to-Vector Explorer")
    plt.xlabel("Dimension 1 (X)")
    plt.ylabel("Dimension 2 (Y)")
    plt.grid(True)
    plt.show()


# STEP 7: Main menu
def main():
    while True:
        print("\n===== TEXT-TO-VECTOR EXPLORER =====")
        print("1. Display all words, vectors, and dimensions")
        print("2. Compare two vectors")
        print("3. Find the closest pair of vectors")
        print("4. Visualize vectors")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            display_dataset()
        elif choice == "2":
            compare_vectors()
        elif choice == "3":
            find_closest_vectors()
        elif choice == "4":
            visualize_vectors()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# STEP 8: Run the program
if __name__ == "__main__":
    main()
