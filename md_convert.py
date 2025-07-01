import requests


def url_to_markdown(url, use_readerlm=False):
    prefix = "https://r.jina.ai/"
    headers = {}
    if use_readerlm:
        headers["x-engine"] = "readerlm-v2"
    res = requests.get(prefix + url, headers=headers)
    res.raise_for_status()
    return res.text


if __name__ == "__main__":
    import os

    discussion_urls = [
        "https://www.kaggle.com/competitions/ariel-data-challenge-2025/discussion/586478",
        "https://www.kaggle.com/competitions/ariel-data-challenge-2025/discussion/586229",
    ]
    os.makedirs("./docs", exist_ok=True)
    discussion_md = ""
    for url in discussion_urls:
        md = url_to_markdown(url)
        discussion_md += f"\n\n# Source: {url}\n\n"
        discussion_md += md.strip() + "\n"
    discussion_path = os.path.join("docs", "discussion.md")
    with open(discussion_path, "w", encoding="utf-8") as f:
        f.write(discussion_md.strip())
    print(f"Saved combined discussion markdown to {discussion_path}")
