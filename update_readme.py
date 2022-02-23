import datetime
import feedparser


def generate_readme_contents(*, blog_sitemap_url: str, til_sitemap_url: str, gists_url) -> str:
    contents: List[str] = [
        "## About me",
        "I'm the Head of Software Engineering at [Octopus Energy](https://octopus.energy/).",
        "",
        "I used to maintain several open-source projects but I do less open-source work these days. "
        "I'm the original author of [`django-oscar`](https://github.com/django-oscar/django-oscar) although I'm not active in the project any more. "
    ]

    # Add content from blog.
    contents.append("## Latest blog posts")
    for post_data in fetch_blog_posts(blog_sitemap_url):
        contents.append(
            f"- [{post_data['title']}]({post_data['url']}) - {post_data['published_date']}"
        )
    contents.append("")
    contents.append("[Browse all blog posts](https://codeinthehole.com/writing/)")

    # Add content from TIL site.
    contents.append("## Latest TIL posts")
    contents.append("I learnt...")
    for post_data in fetch_til_posts(til_sitemap_url):
        contents.append(
            f"- [{post_data['title']}]({post_data['url']}) on {post_data['published_date']}"
        )
    contents.append("")
    contents.append("[Browse all TIL posts](https://til.codeinthehole.com)")

    # Add content from public gists
    contents.append("## Latest Gists")
    for post_data in fetch_public_gists(gists_url):
        contents.append(
            f"- [{post_data['title']}]({post_data['url']}) on {post_data['published_date']}"
        )
    contents.append("")
    contents.append("[Browse all public Gists](https://gist.github.com/codeinthehole)")

    return "\n".join(contents)


def fetch_blog_posts(url: str, max_entries: int = 8):
    for post in feedparser.parse(url)["entries"][:max_entries]:
        yield {
            "title": post["title"],
            "url": post["link"],
            "published_date": datetime.datetime(*post["published_parsed"][:6]).date(),
        }


def fetch_til_posts(url: str, max_entries: int = 8):
    for post in feedparser.parse(url)["entries"][:max_entries]:
        yield {
            "title": post["title"],
            "url": post["link"],
            "published_date": datetime.datetime(*post["published_parsed"][:6]).date(),
        }


def fetch_public_gists(url: str, max_entries: int = 8):
    for post in feedparser.parse(url)["entries"][:max_entries]:
        yield {
            "title": post["title"],
            "url": post["link"],
            "published_date": datetime.datetime(*post["published_parsed"][:6]).date(),
        }


if __name__ == "__main__":
    contents = generate_readme_contents(
        blog_sitemap_url="https://codeinthehole.com/index.xml",
        til_sitemap_url="https://til.codeinthehole.com/posts/index.xml",
        gists_url="https://gist.github.com/codeinthehole.atom",
    )

    print(contents)
