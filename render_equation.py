# From: https://gist.github.com/tonyseek/95c90638cf43a87e723b
try:
    from StringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

import matplotlib.pyplot as plt
import matplotlib as mpl


def render_latex(formula, fontsize=12, dpi=300, format_='svg'):
    # print(mpl.rcParams['mathtext.default'])
    # mpl.rc('mathtext', default='cal')
    # print(mpl.rcParams['text.usetex'])
    mpl.rc('text', usetex=True)
    """Renders LaTeX formula into image."""
    fig = plt.figure()
    text = fig.text(0, 0, u'${0}$'.format(formula), fontsize=fontsize)

    fig.savefig(BytesIO(), dpi=dpi)  # triggers rendering

    bbox = text.get_window_extent()
    width, height = bbox.size / float(dpi) + 0.05
    fig.set_size_inches((width, height))

    dy = (bbox.ymin / float(dpi)) / height
    text.set_position((0, -dy))

    buffer_ = BytesIO()
    fig.savefig(buffer_, dpi=dpi, transparent=True, format=format_)
    plt.close(fig)
    buffer_.seek(0)

    return buffer_.getvalue()


if __name__ == '__main__':
    # equation = r'\displaystyle\int_{a}^{b} {f(x)dx = F(b) - F(a)}'
    # equation = r'SNR = \displaystyle\frac{P_S}{P_N} = \displaystyle\frac{P_T G_T G_R \lambda^{2} \sigma}{(4 \pi)^{3} R^{4} k T_0 B F_n L}'
    equation = r'\int_{a}^{b} {f(x)dx = F(b) - F(a)}'
    image_bytes = render_latex(equation, format_='svg')
    with open('formula.svg', 'wb') as image_file:
        image_file.write(image_bytes)

# from io import BytesIO
#
# import matplotlib.pyplot as plt
#
# def render_latex(formula, fontsize=12, dpi=300, format_='svg'):
#     """Renders LaTeX formula into image.
#     """
#     fig = plt.figure(figsize=(0.01, 0.01))
#     fig.text(0, 0, u'${}$'.format(formula), fontsize=fontsize)
#     buffer_ = BytesIO()
#     fig.savefig(buffer_, dpi=dpi, transparent=True, format=format_, bbox_inches='tight', pad_inches=0.0)
#     plt.close(fig)
#     return buffer_.getvalue()
#
# if __name__ == '__main__':
#     equation = r'\int_{a}^{b} f(x)dx = F(b) - F(a)'
#     image_bytes = render_latex(
#         equation, fontsize=10, dpi=200, format_='svg')
#     with open('formula.svg', 'wb') as image_file:
#         image_file.write(image_bytes)