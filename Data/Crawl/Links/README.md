# 🔍 Infographics Links Crawling Process

To collect a diverse and representative dataset of Infographics in Vietnam, we conducted a thorough search of both major and minor reputable news sources that regularly publish Infographics. After evaluating many sources, we selected **26 Vietnamese news agencies**, listed below:

+ An Ninh Thủ Đô

+ An Toàn Thông Tin

+ Chính Phủ

+ Công Lý

+ Đại Đoàn Kết

+ Đảng Cộng Sản

+ Dân Trí

+ Dân Việt

+ Đấu Thầu

+ Gia Đình và Xã Hội

+ Giao Thông

+ Lao Động

+ Lao Động Công Đoàn

+ Nhân Dân

+ Pháp Luật

+ Phụ Nữ

+ Sài Gòn Giải Phóng

+ Sức Khoẻ và Đời Sống

+ Thanh Niên

+ Tiền Phong

+ TTXVN

+ Tuổi Trẻ

+ VnExpress

+ VOV

+ VTV

+ ZingNews

Among them, **24 sources were crawled automatically**, while **2 sources (An Toàn Thông Tin and Lao Động)** were crawled manually due to the small number of links available.

## ⚙️ Crawling Tools and Approach

We used two main Python libraries for link extraction:

+ `BeautifulSoup` (for static HTML parsing)

+ `Selenium` (for rendering and interacting with dynamic content)

**In most cases, BeautifulSoup was our preferred choice** due to its faster performance and lower resource consumption when parsing static content. It works well when the page structure is accessible via direct HTTP requests, and the relevant links are present in the returned HTML.

However, **some news websites (e.g., VOV)** implement JavaScript rendering or anti-bot measures that prevent direct access to their content. In such cases, we switched to **Selenium**, which can mimic human interactions in a browser, allowing us to access dynamic content and bypass certain client-side protections.

## 🧠 Crawling Strategy and Tips

Depending on the HTML structure of each website, we adapted our crawler accordingly. Still, most websites follow certain patterns that can be exploited for efficient automated crawling. Here are a few tips we followed during the process:

+ **Pay attention to page-level parameters** like page number, number of articles per page, etc. These are often reflected in the URL patterns (e.g., `?page=1`, `&limit=10`).

+ **Use the browser's developer tools**:

    + Right-click on the page and select **"Inspect"**. Try changing pages and observing how the URLs change. The first network requests are often indicative of the underlying pattern.

    + Use **"View Page Source"** to examine the raw HTML. Look for keywords or attributes that contain link information, such as `href`, `data-url`, or `src`.

+ **Avoid duplicate URLs**: Ensure that your crawler checks for repeated URLs to prevent redundant data collection.