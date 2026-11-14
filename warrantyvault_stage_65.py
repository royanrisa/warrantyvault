# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: WarrantyVault
import re


def merge_imports(existing, new):
    """Merge new import statements into an existing import block,
    avoiding obvious duplicates while preserving readability."""
    if not existing.strip():
        return new

    lines = existing.splitlines()
    indent = re.match(r"\s*", lines[0]).group()
    block = [line.strip() for line in lines]

    for candidate in new:
        candidate = candidate.strip()
        if any(candidate == current for current in block):
            continue

        if candidate.startswith("from "):
            module = candidate.split()[1]
            names = re.findall(r"[A-Za-z_]\w*", module)
            if names and not any(candidate.startswith("from " + n + " import") for n in names):
                for name in names:
                    existing_from = "from {} import".format(name)
                    if any(existing_from == current for current in block):
                        continue
                    block.append(existing_from)
                    if len(candidate) > len(existing_from) + 1:
                        block.append(candidate[len(existing_from) + 1:].strip())
            continue

        module = re.match(r"^import ([A-Za-z_]\w*)$", candidate).group(1)
        if any(module == current for current in block):
            continue
        block.append(candidate)

    cleaned = [line.strip() for line in block if line.strip()]

    if not cleaned:
        return new

    if not existing.endswith("\n"):
        existing += "\n"

    for index, line in enumerate(cleaned):
        if line.startswith("from "):
            module = line.split()[1]
            names = re.findall(r"[A-Za-z_]\w*", module)
            if names and index + 1 < len(cleaned):
                next_line = cleaned[index + 1]
                if next_line.startswith("from " + module + " import"):
                    cleaned[index] = "from {} import {}".format(module, next_line[len("from " + module + " import") + 1:].strip())
                    cleaned.pop(index + 1)
                    cleaned[index] = cleaned[index].strip()
        else:
            module = re.match(r"^import ([A-Za-z_]\w*)$", line).group(1)
            if index + 1 < len(cleaned) and re.match(r"^import {}".format(re.escape(module)) + r"\b", cleaned[index + 1]):
                cleaned[index] = "import {}".format(module)
                cleaned.pop(index + 1)
                cleaned[index] = cleaned[index].strip()

    return "{}{}".format(indent, "\n".join(cleaned)) + "\n"
