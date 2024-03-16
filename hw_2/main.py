import os
import latex
from pdflatex import PDFLaTeX

artifacts_dir = os.path.join(os.path.dirname(__file__), "artifacts")

characters_tex_path = os.path.join(artifacts_dir, "characters.tex")
characters_pdf_path = os.path.join(artifacts_dir, "characters.pdf")


def generate_characters_doc():
    print(os.listdir(os.path.join(artifacts_dir)))
    table_data = [
        ["id", "name", "age"],
        ["1", "Eleven",  15],
        ["2", "Mike",    16],
        ["3", "Dustin",  15],
        ["4", "Steve",   17],
        ["5", "Billie",  19],
    ]
    body_generator = latex.make_chain_generator(
        latex.make_generator(latex.generate_table, table_data),
        latex.make_generator(latex.generate_image, "logo.png"),
    )
    with open(characters_tex_path, "w") as f:
        f.write(latex.generate_doc("characters", body_generator))


def generate_characters_pdf():
    pdfl = PDFLaTeX.from_texfile(characters_tex_path)
    cwd = os.getcwd()
    os.chdir(os.path.dirname(characters_pdf_path))
    pdf, _, _ = pdfl.create_pdf(
        keep_pdf_file=True, keep_log_file=True)
    os.chdir(cwd)


if __name__ == "__main__":
    generate_characters_doc()
    generate_characters_pdf()
