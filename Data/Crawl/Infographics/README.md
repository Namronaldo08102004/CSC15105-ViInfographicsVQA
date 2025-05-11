# Image Crawler for News Websites
This script is designed to **automatically crawl and download images** from a list of article URLs from Vietnamese news sites. It’s a preparatory step for downstream tasks such as image-based QA generation or dataset building.

## 🚀 What It Does

- Reads a plain text file (`<site>_links.txt`) that contains a list of article URLs.
- Fetches each page using the `requests` library.
- Parses HTML content with `BeautifulSoup` to locate image tags.
- Extracts image URLs using site-specific HTML attributes (defined in a config dictionary).
- Supports:
  - Standard image URLs (e.g., `.jpg`, `.png`, etc.)
  - Inline base64-encoded images
- Saves images into a local folder named after the site.
- Automatically **skips already downloaded images** to prevent redundancy.

## 🧠 Key Features

- ✅ **Multi-site support** via a customizable `structure` dictionary for each news outlet's HTML pattern.
- ♻️ **Resumable downloads**: detects already downloaded files based on filenames and continues from the last.
- 🧼 **Smart URL handling**: removes query strings, resolves relative paths.
- 🔄 **Fallback support**: if standard detection fails, it optionally falls back to a fixed `<img>` tag index (`alter`).


## 🧰 Dependencies

- `requests`: To fetch page HTML and image content.
- `beautifulsoup4`: To parse and search HTML content.
- `tqdm`: To display a progress bar for the download process.


## 📌 Notes
- Only images with valid extensions (e.g., `.jpg`, `.png`, `.gif`, `.webp`) are saved.
- Handles inline `data:image/` base64 URLs automatically.
- Can be extended to support more news sources by updating the `structure` config.

