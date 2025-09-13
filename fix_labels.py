import os
import argparse

def scan_and_fix_labels(root, class_count, mode="report"):
    problems = []
    for subset in ["train", "val", "test"]:
        label_dir = os.path.join(root, subset, "labels")
        if not os.path.exists(label_dir):
            continue
        for file in os.listdir(label_dir):
            if not file.endswith(".txt"):
                continue
            path = os.path.join(label_dir, file)
            with open(path, "r") as f:
                lines = f.readlines()

            new_lines = []
            fixed = False
            for line in lines:
                parts = line.strip().split()
                if len(parts) < 5:  # at least class + 4 coords
                    continue
                cls = int(parts[0])
                if cls >= class_count:
                    problems.append(f"{path}: class {cls} invalid")
                    fixed = True
                    continue
                new_lines.append(line)

            if fixed and mode == "fix":
                with open(path, "w") as f:
                    f.writelines(new_lines)

    return problems


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--yaml", type=str, required=True, help="Path to dataset.yaml")
    parser.add_argument("--root", type=str, required=True, help="Root dataset folder (with train/val/test)")
    parser.add_argument("--mode", type=str, default="report", choices=["report", "fix"], help="Just report or auto-fix")
    args = parser.parse_args()

    # read yaml to get class count
    import yaml
    with open(args.yaml, "r") as f:
        data = yaml.safe_load(f)
    class_count = len(data["names"])

    problems = scan_and_fix_labels(args.root, class_count, args.mode)

    if args.mode == "report":
        if problems:
            print("\n⚠️ Problems found:")
            for p in problems:
                print(p)
        else:
            print("✅ No invalid labels found")
    else:
        print("✅ Fix complete")
