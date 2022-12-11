


def main():
    # Remove versions from requirements-dirty.txt
    with open("requirements-dirty.txt", "r") as f:
        requirements = f.read().splitlines()
        # Skip 3 lines
        requirements = requirements[3:]
        requirements = [r.split("=")[0] for r in requirements]
    with open("requirements.txt", "w") as f:
        f.write("\n".join(requirements))

if __name__ == "__main__":
    main()