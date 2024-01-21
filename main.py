from typing import List
from argparse import ArgumentParser, Namespace

import os

from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--folder", type=str, required=True)
    parser.add_argument("--save_fname", type=str, required=True)

    args = parser.parse_args()
    return args


def listfiles(path: str, extensions: List[str]):
    files = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            ext = os.path.splitext(f)[-1].lower()

            if ext in extensions:
                files.append(f)

    files.sort()
    # files = [f for f in files]
    files = [os.path.join(path, f) for f in files]
    return files


def imgs_to_pdf(files: List[str], save_fname: str):
    imgs: List[Image.Image]

    imgs = []
    for f in files:
        img = Image.open(f).convert('RGB')
        imgs.append(img)

    imgs[0].save(save_fname, save_all=True, append_images=imgs[1:])
    return


def main(args):
    folder = args.folder
    save_fname = args.save_fname

    print(f"{folder = }")
    print(f"{save_fname = }")

    files = listfiles(folder, ['.jpg', '.jpeg', '.png'])
    # print(f"{files = }")

    imgs_to_pdf(files, save_fname)
    return


if __name__ == "__main__":
    args = parse_args()
    main(args)
    print("DONE")
