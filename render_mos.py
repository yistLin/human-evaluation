#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    html = template.render(
        page_title="MOS 實驗表單 1",
        form_url="http://localhost:8888",
        form_id=1,
        questions=[
            {
                "title": "問題 1",
                "audio_path": "wavs/test1.wav",
                "name": "q1"
            },
            {
                "title": "問題 2",
                "audio_path": "wavs/test2.wav",
                "name": "q2"
            },
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
