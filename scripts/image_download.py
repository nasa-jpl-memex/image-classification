import click
import hashlib
import os
import requests
import sys


IMAGE_PATH = 'images'


def store_image(request):
    sha1 = hashlib.sha1(request.content).hexdigest()

    try:
        os.makedirs(os.path.join(IMAGE_PATH, sha1[0:3]))
    except OSError:
        pass

    with open(os.path.join(IMAGE_PATH, sha1[0:3], sha1), 'wb') as outfile:
        outfile.write(request.content)

    return sha1


@click.command()
@click.argument('url')
@click.option('--num-tries', default=5, help='Number of times to try downloading the image')
def download(url, num_tries):
    if num_tries > 0:
        i = 1
        while True:
            try:
                r = requests.get(url, stream=True)
            except Exception:
                sys.exit(3)

            if r.ok:
                sha1 = store_image(r)

                if sha1:
                    print('%s,%s' % (url, sha1))
                    sys.exit(0)
                else:
                    sys.exit(4)
            elif (r.status_code >= 400 and r.status_code < 500):
                sys.exit(1)
            elif i == num_tries:
                sys.exit(2)
            else:
                i += 1
                continue
    else:
        sys.exit(1)


if __name__ == '__main__':
    download()
