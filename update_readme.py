import datetime
import feedparser


def generate_readme_contents(*, sitemap_url: str) -> str:
    contents: List[str] = ["I'm the Head of Software Engineering at Octopus Energy."]

    # Add content from blog.
    contents.append("## Latest blog posts")
    for post_data in fetch_blog_posts(sitemap_url):
        contents.append(
            f"- [{post_data['title']}]({post_data['url']}) - {post_data['published_date']}"
        )

    return "\n".join(contents)


def fetch_blog_posts(url: str, max_entries: int = 8):
    for post in feedparser.parse(url)["entries"][:max_entries]:
        yield {
            "title": post["title"],
            "url": post["link"],
            "published_date": datetime.datetime(*post["published_parsed"][:6]).date(),
        }


if __name__ == "__main__":
    contents = generate_readme_contents(
        sitemap_url="https://codeinthehole.com/index.xml"
    )

    print(contents)
