#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from bs4 import BeautifulSoup


QUESTION_TEMP = """
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


def main():
    """Main function."""

    with open("template.html", "r") as template_file:
        document_template = template_file.read()

    for form_id in range(1):

        soup = BeautifulSoup(document_template, "html.parser")

        title_tag = soup.find("title")
        title_tag.string = f"表單 {form_id}"

        submit_tag = soup.find(id="submitBtn")

        formid_input_tag = soup.new_tag("input", attrs={
            "name": "formid",
            "type": "text",
            "hidden": "",
            "value": form_id,
        })
        submit_tag.insert_before(formid_input_tag)

        for q_id in range(2):

            question_html = QUESTION_TEMP.format(title=f"問題 {q_id+1}",
                                                 audio_path_1="#",
                                                 audio_path_2="#",
                                                 question_var=f"q{q_id+1}")
            question_soup = BeautifulSoup(question_html, "html.parser")

            submit_tag.insert_before(question_soup)

        with open(f"form{form_id}.html", "w") as output_file:
            output_file.write(soup.prettify())


if __name__ == "__main__":
    main()
