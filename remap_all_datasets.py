import os

# 🔹 Root folder containing all original datasets
ROOT_DIR = r"C:\Users\pranavaa\Downloads\traffic-ai\datasets_original"

# 🔹 Define mapping for each dataset
DATASET_MAPPINGS = {
    "ds1": {0:0, 1:1, 2:2, 3:3},
    "ds2": {0:0, 1:1, 2:2, 3:3},
    "ds3": {0:0, 1:1, 2:4, 3:2, 4:5, 5:3, 6:6},
    "ds4": {0:7},
    "ds5": {0:9, 1:10, 2:11, 3:12, 4:13},
    "ds6": {0:1, 1:8, 2:2, 3:14}
}

# 🔹 Splits
splits = ["train", "val", "test"]

# 🔹 Loop through each dataset
for dataset_name, mapping in DATASET_MAPPINGS.items():
    dataset_path = os.path.join(ROOT_DIR, dataset_name)
    print(f"Processing dataset: {dataset_name}")
    
    for split in splits:
        labels_dir = os.path.join(dataset_path, split, "labels")
        if not os.path.exists(labels_dir):
            continue
        
        for label_file in os.listdir(labels_dir):
            if not label_file.endswith(".txt"):
                continue

            file_path = os.path.join(labels_dir, label_file)
            new_lines = []

            with open(file_path, "r") as f:
                lines = f.readlines()

            for line in lines:
                parts = line.strip().split()
                if len(parts) == 0:
                    continue
                old_class = int(parts[0])
                if old_class not in mapping:
                    print(f"⚠️ Skipping {old_class} in {file_path} (no mapping)")
                    continue
                new_class = mapping[old_class]
                parts[0] = str(new_class)
                new_lines.append(" ".join(parts))

            # Overwrite label file with remapped indices
            with open(file_path, "w") as f:
                f.write("\n".join(new_lines))

print("✅ All datasets remapped successfully!")
