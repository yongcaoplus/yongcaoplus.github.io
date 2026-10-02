# yongcaoplus.github.io

Personal homepage of Yong Cao, served by GitHub Pages (Jekyll).

| What to edit | File |
| --- | --- |
| Bio text, news, talks, teaching, service, background, honors, header links | `_pages/about.md` |
| Publications | `_data/publications.yml` |
| Page layout and styles | `_layouts/homepage.html` |
| PDFs (CV, slides, posters) | `files/` |
| Photo and paper figures | `images/`, `images/papers/` |

## Adding a figure to a publication

1. Put the image in `images/papers/`, e.g. `images/papers/frankenmotion.png`.
2. Add `image: /images/papers/frankenmotion.png` to that paper's entry in `_data/publications.yml`.
3. By default the image is stretched to fill the 16:10 box exactly. Add `image_fit: cover` to fill it while keeping proportions (edges get cropped), or `image_fit: contain` to show the whole image without distortion.
