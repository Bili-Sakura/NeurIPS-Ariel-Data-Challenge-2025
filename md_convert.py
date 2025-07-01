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

    urls = [
        "https://www.kaggle.com/competitions/ariel-data-challenge-2025/overview",
        "https://www.kaggle.com/competitions/ariel-data-challenge-2025/data",
        "https://www.kaggle.com/competitions/ariel-data-challenge-2025/rules",
    ]
    os.makedirs("./docs", exist_ok=True)
    for url in urls:
        md = url_to_markdown(url)
        filename = url.split("/")[-1] or "index"
        filepath = os.path.join("docs", f"{filename}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Saved markdown for {url} to {filepath}")
