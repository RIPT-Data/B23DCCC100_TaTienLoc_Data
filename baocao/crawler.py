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