import os
import subprocess

def compress_pdf(path):
    # Get the path to the output file
    output_path = os.path.splitext(path)[0] + "_compressed.pdf"

    # Detect operating system
    if os.name == "nt":
        # Windows
        executable = f"CommonFiles/Ghostscript/bin/gswin32c.exe"
    else:
        # Linux
        executable = f"gs-1000-linux_x86_64"

    # Compress the file
    subprocess.run([executable, "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
                    "-dPDFSETTINGS=/screen", "-dNOPAUSE", "-dQUIET",
                    "-dBATCH", "-sOutputFile=" + output_path, path])

    # Get size from the original file and the compressed file
    original_size = os.path.getsize(path)
    compressed_size = os.path.getsize(output_path)

    # Print the compression ratio in percentage
    print(f"Compression ratio: {round(compressed_size / original_size * 100, 2)}%")

    # Print size of the original file and the compressed file in MB
    print(f"Original size: {original_size / 1024 / 1024:.2f} MB")
    print(f"Compressed size: {compressed_size / 1024 / 1024:.2f} MB")

    # Print output path to the compressed file
    print("Compressed file saved to", output_path)


def main():
    compress_pdf("sample.pdf")


if __name__ == "__main__":
    main()
