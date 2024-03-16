
def generate_table(table_list):
    columns = len(table_list[0])
    tabs = "|" + "c|" * columns
    data = "\\hline\n" + "\n".join(
        map(
            lambda row: "&".join(map(str, row)) + "\\\\ \\hline",
            table_list
        )
    )
    fmt = """\\begin{table}[h!]
\\begin{tabular}{%s}
%s
\\end{tabular}
\\end{table}
""" % (tabs, data)
    return fmt


def generate_image(filename, scale=1):
    fmt = """
\\includegraphics[width=%d\\textwidth]{%s}
"""
    return fmt % (scale, filename)


def make_generator(gen_func, *args):
    def generator():
        return gen_func(*args)
    return generator


def make_chain_generator(*generators):
    def generator():
        return "".join(map(lambda gen: gen(), generators))
    return generator


def generate_doc(title, generaty_body):
    fmt = """\\documentclass{article}
\\usepackage{graphicx}
\\title{%s}
\\begin{document}
%s
\\end{document}
"""
    return fmt % (title, generaty_body())
