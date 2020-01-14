from difflib import HtmlDiff
from custom import CustomHTML
from datetime import datetime
import arguments


def main(args):
    """Generate diff.html file"""
    if not args.filename:
        """
        print(args.file[0].name)
        file1 = args.file[0].name.split('/')[-1].split('.')[0]
        file2 = args.file[1].name.split('/')[-1].split('.')[0]
        filename = "diff_%s_X_%s.html" % (file1, file2)
        """
        date_now = datetime.now()
        filename = 'Diff from {0:%Y}-{0:%m}-{0:%d} {0:%H}-{0:%M}-{0:%S}.html'
        filename = filename.format(date_now)

    elif not args.filename.endswith(".html"):
        filename = args.filename = args.filename + ".html"
    else:
        filename = args.filename

    with open(filename, 'w+') as output_file:
        first_file, second_file = args.file[0], args.file[1]

        diff = HtmlDiff().make_file(
            fromlines=first_file, tolines=second_file,
            fromdesc=first_file.name.split('/')[-1],
            todesc=second_file.name.split('/')[-1])

        custom = CustomHTML()
        diff = custom.new_html(html=diff, args=args)

        output_file.write(diff)

        for file_open in args.file:
            file_open.close()

        print("Successful diff!\nFile: {}".format(filename))


if __name__ == '__main__':
    argv = arguments.parse_args()
    main(argv)
