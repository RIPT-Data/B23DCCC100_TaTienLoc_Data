# Tìm hiểu về Crawler Data

## Mục lục

- [Tìm hiểu về Crawler Data](#tìm-hiểu-về-crawler-data)
  - [Mục lục](#mục-lục)
  - [Giới thiệu](#giới-thiệu)
  - [Crawler Data là gì?](#crawler-data-là-gì)
  - [Các ứng dụng của Crawler Data](#các-ứng-dụng-của-crawler-data)
  - [Chương trình mẫu](#chương-trình-mẫu)
    - [Yêu cầu](#yêu-cầu)
    - [Chương trình Crawler](#chương-trình-crawler)
    - [Giải thích chương trình](#giải-thích-chương-trình)
  - [Kết luận](#kết-luận)
  - [Tài liệu tham khảo](#tài-liệu-tham-khảo)

## Giới thiệu

Trong thời đại số hóa ngày nay, việc thu thập dữ liệu từ các nguồn khác nhau trên internet đóng vai trò quan trọng trong việc nghiên cứu và phân tích. Một trong những phương pháp phổ biến để thu thập dữ liệu là sử dụng các công cụ crawler. Báo cáo này sẽ giới thiệu tổng quan về khái niệm "Crawler Data", các ứng dụng của nó, và cách triển khai một chương trình crawler đơn giản để thu thập dữ liệu từ một trang báo trực tuyến và lưu trữ vào file CSV.

## Crawler Data là gì?

Crawler Data là dữ liệu được thu thập từ các trang web thông qua quá trình crawling (thu thập thông tin tự động) bằng cách sử dụng các công cụ phần mềm gọi là "web crawler" hoặc "web spider". Các trình crawler sẽ truy cập vào các trang web, đọc và phân tích nội dung của chúng, sau đó trích xuất và lưu trữ các thông tin cần thiết.

Các loại dữ liệu mà crawler có thể thu thập bao gồm:
- Nội dung văn bản của các bài viết.
- Siêu dữ liệu như tiêu đề, mô tả, và từ khóa.
- Các liên kết nội bộ và ngoại bộ trên trang web.
- Thông tin cấu trúc như bảng biểu, danh sách, và biểu đồ.

## Các ứng dụng của Crawler Data

Crawler Data có nhiều ứng dụng trong các lĩnh vực khác nhau, bao gồm:
- **Công cụ tìm kiếm**: Google, Bing và các công cụ tìm kiếm khác sử dụng web crawler để lập chỉ mục nội dung và cung cấp kết quả tìm kiếm cho người dùng.
- **Phân tích thị trường**: Thu thập thông tin sản phẩm, giá cả, và đánh giá để phân tích thị trường và theo dõi đối thủ cạnh tranh.
- **Nghiên cứu học thuật**: Thu thập dữ liệu từ nhiều nguồn khác nhau để nghiên cứu và phân tích các xu hướng và hành vi.
- **Quản lý nội dung**: Tự động thu thập và cập nhật thông tin từ nhiều nguồn vào hệ thống quản lý nội dung (CMS).

## Chương trình mẫu

Trong phần này, chúng ta sẽ viết một chương trình crawler đơn giản bằng Python để thu thập tiêu đề và liên kết các bài báo từ trang BBC News và lưu thông tin vào file CSV.

### Yêu cầu

- Python 3 đã được cài đặt trên hệ thống.
- Các thư viện cần thiết: `requests`, `beautifulsoup4`, `pandas`.

Cài đặt các thư viện bằng lệnh sau:

`pip install requests beautifulsoup4 pandas`

### Chương trình Crawler

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL của trang VnExpress muốn thu thập dữ liệu
url = "https://vnexpress.net/"

# Gửi yêu cầu HTTP để lấy nội dung của trang
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công hay không
if response.status_code == 200:
    # Phân tích cú pháp HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Tìm tất cả các phần tử chứa tiêu đề bài báo
    articles = soup.find_all('article', class_='item-news')

    # Danh sách để lưu dữ liệu
    data = []

    # Duyệt qua từng bài báo và lưu thông tin vào danh sách
    for article in articles:
        title_tag = article.find('h3', class_='title-news')
        if title_tag:
            title = title_tag.get_text(strip=True)  # Tiêu đề bài viết
            link = title_tag.find('a')['href']  # Liên kết bài viết
            time_tag = article.find('span', class_='time-public')
            time = time_tag.get_text(strip=True) if time_tag else 'N/A'  # Thời gian đăng bài
            data.append({"Title": title, "Link": link, "Time": time})

    # Chuyển đổi dữ liệu thành DataFrame của pandas
    df = pd.DataFrame(data)

    # Lưu vào file CSV
    df.to_csv('vnexpress_news.csv', index=False)
    print("Dữ liệu đã được lưu vào file 'vnexpress_news.csv'")
else:
    print(f"Lỗi khi gửi yêu cầu đến {url}: {response.status_code}")
```
### Giải thích chương trình

Chương trình crawler trên gồm các bước sau:

1. **Thư viện sử dụng**:
    - `requests`: Thư viện này được sử dụng để gửi yêu cầu HTTP đến trang web và nhận lại nội dung của trang.
    - `BeautifulSoup` từ `bs4`: Dùng để phân tích cú pháp HTML của trang web, trích xuất và thao tác với dữ liệu HTML.
    - `pandas`: Thư viện giúp lưu trữ và xử lý dữ liệu dưới dạng bảng (DataFrame) và dễ dàng xuất dữ liệu ra các định dạng khác như CSV.

2. **Gửi yêu cầu HTTP**:
    - Dòng `response = requests.get(url)` gửi một yêu cầu HTTP GET đến URL của trang web (ở đây là trang chủ của BBC News). Kết quả trả về của yêu cầu này được lưu vào biến `response`.

3. **Kiểm tra phản hồi**:
    - Dòng `if response.status_code == 200:` kiểm tra xem yêu cầu có thành công hay không (mã trạng thái 200 biểu thị thành công).

4. **Phân tích cú pháp HTML**:
    - Sử dụng `BeautifulSoup` để phân tích nội dung HTML của trang, cụ thể là phân tích cú pháp và trích xuất các thẻ `h3` có chứa tiêu đề của các bài báo. 

5. **Trích xuất và lưu dữ liệu**:
    - Dữ liệu được trích xuất bao gồm tiêu đề bài viết và đường dẫn của bài viết. Đường dẫn được chuyển đổi thành một liên kết đầy đủ nếu nó là đường dẫn tương đối.
    - Dữ liệu sau đó được lưu vào một danh sách các từ điển, mỗi từ điển đại diện cho một bài báo với tiêu đề và đường dẫn tương ứng.

6. **Lưu trữ dữ liệu vào file CSV**:
    - Dòng `df.to_csv('vnexpress_news.csv', index=False)` dùng thư viện pandas để lưu dữ liệu dưới dạng file CSV, với cột "Title" chứa tiêu đề bài viết và cột "Link" chứa liên kết bài viết.

## Kết luận

Crawler data là một công cụ mạnh mẽ trong việc thu thập thông tin từ các trang web để phục vụ cho nhiều mục đích khác nhau, từ phân tích dữ liệu đến nghiên cứu thị trường. Chương trình crawler mẫu trong báo cáo này minh họa cách trích xuất dữ liệu từ một trang báo điện tử và lưu trữ vào file CSV để dễ dàng quản lý và sử dụng. Điều này có thể áp dụng vào nhiều lĩnh vực và được mở rộng để trích xuất nhiều loại thông tin khác nhau từ các nguồn web khác.

## Tài liệu tham khảo

- BeautifulSoup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Requests Documentation: https://docs.python-requests.org/en/master/
- Pandas Documentation: https://pandas.pydata.org/pandas-docs/stable/
- VnExpress: https://vnexpress.net/
- ChatGPT : https://chatgpt.com/