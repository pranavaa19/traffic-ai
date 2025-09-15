import os
import shutil
from collections import Counter
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
ROOT_DIR = r"datasets_original"       # Folder containing ds1, ds2, ..., ds6
MERGE_DIR = r"dataset/ready_dataset"  # Final merged dataset

splits = ["train", "val", "test"]

# -----------------------------
# Global mapping for each dataset
# -----------------------------
DATASET_MAPPINGS = {
    "ds1": {0:1, 1:0, 2:3, 3:2},
    "ds2": {0:1, 1:0, 2:3, 3:2},
    "ds3": {0:1, 1:0, 2:4, 3:3, 4:5, 5:2, 6:6},
    "ds4": {0:7, 7:7},
    "ds5": {0:9, 1:10, 2:11, 3:12, 4:13, 9:9, 10:10, 11:11, 12:12, 13:13},
    "ds6": {0:0, 1:8, 2:3, 3:14, 8:8, 14:14}
}


# -----------------------------
# Step 0: Create merged folder structure
# -----------------------------
for split in splits:
    os.makedirs(os.path.join(MERGE_DIR, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(MERGE_DIR, split, "labels"), exist_ok=True)

# -----------------------------
# Step 1: Process each dataset
# -----------------------------
for dataset_name, mapping in DATASET_MAPPINGS.items():
    dataset_path = os.path.join(ROOT_DIR, dataset_name)
    print(f"\nProcessing dataset: {dataset_name}")
    
    for split in splits:
        images_src = os.path.join(dataset_path, split, "images")
        labels_src = os.path.join(dataset_path, split, "labels")
        images_dst = os.path.join(MERGE_DIR, split, "images")
        labels_dst = os.path.join(MERGE_DIR, split, "labels")

        if not os.path.exists(images_src) or not os.path.exists(labels_src):
            continue

        for file in os.listdir(images_src):
            if not (file.endswith(".jpg") or file.endswith(".png")):
                continue

            # Rename file to avoid duplicates
            new_file_name = f"{dataset_name}_{file}"
            shutil.copy2(os.path.join(images_src, file), os.path.join(images_dst, new_file_name))

            # Copy & remap label
            label_file = file.rsplit(".", 1)[0] + ".txt"
            label_src_path = os.path.join(labels_src, label_file)
            label_dst_path = os.path.join(labels_dst, f"{dataset_name}_{label_file}")

            if not os.path.exists(label_src_path):
                continue

            new_lines = []
            with open(label_src_path, "r") as f:
                lines = f.readlines()

            for line in lines:
                parts = line.strip().split()
                if len(parts) == 0:
                    continue
                old_class = int(parts[0])
                if old_class not in mapping:
                    print(f"⚠️ Skipping {old_class} in {label_src_path} (no mapping!)")
                    continue
                parts[0] = str(mapping[old_class])
                new_lines.append(" ".join(parts))

            with open(label_dst_path, "w") as f:
                f.write("\n".join(new_lines))

print("\n✅ All datasets remapped and merged successfully!")

# -----------------------------
# Step 2: Verify all 15 classes
# -----------------------------
print("\n🔍 Verifying occurrences per class...")
counter = Counter()

for split in splits:
    labels_path = Path(MERGE_DIR) / split / "labels"
    for txt_file in labels_path.glob("*.txt"):
        with open(txt_file) as f:
            for line in f:
                parts = line.strip().split()
                if parts:
                    counter[int(parts[0])] += 1

for idx in range(15):
    print(f"Class {idx}: {counter[idx]} occurrences")

print("\n✅ Verification complete! All classes accounted for (or 0 occurrences if class absent in this split).")
