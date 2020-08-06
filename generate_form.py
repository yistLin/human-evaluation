#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from bs4 import BeautifulSoup


HTML_TEMP = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.1/css/bootstrap.min.css" integrity="sha384-VCmXjywReHh4PwowAiWNagnWcLhlEJLA5buUprzK8rxFgeH0kww/aWY76TfkUoSX" crossorigin="anonymous">
</head>
<body>
    <div class="jumbotron jumbotron-fluid">
        <div class="container">
            <h1 class="display-4">語者判別實驗</h1>
            <p class="lead">判斷兩份語音是否出自同一個人</p>
            <hr class="my-4">
            <p>
                感謝您參與本次實驗！
            </p>
            <p>
                在這個實驗中，我們使用電腦合成及轉換人類語音。每一題都有兩個音檔，請使用耳機聽完後，根據兩個音檔的語者相似度作答（僅考慮說話者的音色，不須考慮語句內容）。
            </p>
            <p>
                評分標準為：
                <ul>
                    <li>確定是同一個語者 (same, absolutely sure)</li>
                    <li>不大確定，但傾向認為是同一個語者 (same, not sure)</li>
                    <li>不大確定，但傾向認為是不同語者 (different, not sure)</li>
                    <li>確定是不同語者 (different, absolutely sure)</li>
                </ul>
            </p>
        </div>
    </div>
    <div class="container" id="form_container">
    </div>
    <div class="container" style="padding-top: 60px;">
        <p class="text-center text-muted">&copy; 台大語音實驗室</p>
    </div>
</body>
</html>
"""

FORM_HTML_TEMP = """
<form action="#" method="GET">
    <div class="form-group">
        <label for="name">姓名：</label>
        <input class="form-control" type="text" name="name" required>
        <small class="form-text text-muted">必填*</small>
    </div>
    <div class="form-group">
        <label for="mail">電子郵件：</label>
        <input class="form-control" type="text" placeholder="account@example.com" name="mail">
        <small class="form-text text-muted">如果中獎，我們將以電子郵件通知您</small>
    </div>
    <input type="text" name="formid" value="{form_id:d}" hidden>
</form>
"""

QUESTION_HTML_TEMP = """
<div class="card form-group">
    <div class="card-header">{title:s}</div>
    <div class="card-body">
        <p>
            <audio controls src="{audio_path_1:s}">
                Your browser does not support the audio element.
            </audio>
        </p>
        <p>
            <audio controls src="{audio_path_2:s}">
                Your browser does not support the audio element.
            </audio>
        </p>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="{question_var:s}" id="{question_var:s}_1" value="1" required>
            <label class="form-check-label" for="{question_var:s}_1">確定是同一個語者 (same, absolutely sure)</label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="{question_var:s}" id="{question_var:s}_2" value="2" required>
            <label class="form-check-label" for="{question_var:s}_2">不大確定，但傾向認為是同一個語者 (same, not sure)</label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="{question_var:s}" id="{question_var:s}_3" value="3" required>
            <label class="form-check-label" for="{question_var:s}_3">不大確定，但傾向認為是不同語者 (different, not sure)</label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="{question_var:s}" id="{question_var:s}_4" value="4" required>
            <label class="form-check-label" for="{question_var:s}_4">確定是不同語者 (different, absolutely sure)</label>
        </div>
    </div>
</div>
"""

SUBMIT_HTML_TEMP = """
<input class="btn btn-info btn-lg" value="提交結果" type="submit">
"""


def main():
    """Main function."""

    form_html = FORM_HTML_TEMP.format(form_id=1)
    form_soup = BeautifulSoup(form_html, "html.parser")
    form_tag = form_soup.form

    for i in range(3):
        question_html = QUESTION_HTML_TEMP.format(title=f"問題 {i+1}",
                                                  audio_path_1="#",
                                                  audio_path_2="#",
                                                  question_var=f"q{i+1}")
        question_soup = BeautifulSoup(question_html, "html.parser")
        form_tag.append(question_soup)

    form_tag.append(BeautifulSoup(SUBMIT_HTML_TEMP, "html.parser"))

    soup = BeautifulSoup(HTML_TEMP, "html.parser")
    container_tag = soup.find("div", id="form_container")
    container_tag.append(form_soup)

    print(soup.prettify())


if __name__ == "__main__":
    main()
