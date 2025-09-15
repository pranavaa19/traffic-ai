# inspect_labels.py
import os, collections

root = "dataset/ready_dataset"   # path relative to traffic-ai/
splits = ["train","val","test"]

counter = collections.Counter()
examples = {}

for s in splits:
    labdir = os.path.join(root, s, "labels")
    if not os.path.isdir(labdir):
        continue
    for fn in os.listdir(labdir):
        if not fn.endswith(".txt"):
            continue
        fpath = os.path.join(labdir, fn)
        with open(fpath, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                idx = int(line.split()[0])
                counter[idx] += 1
                if idx not in examples:
                    # corresponding image path example
                    imgname = os.path.splitext(fn)[0] + ".jpg"
                    examples[idx] = os.path.join(s, "images", imgname)

print("Found label indices and counts:")
for idx, cnt in sorted(counter.items()):
    print(f"  Index {idx}: {cnt} occurrences   example image -> {examples[idx]}")
