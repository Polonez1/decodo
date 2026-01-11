import google_search
import scraper_links
import click


@click.command()
@click.option("--search_by", prompt="Search query", help="The search query to scrape.")
@click.option("--page_from", default=1, help="The starting page number.")
@click.option("--page_count", default=10, help="The number of pages to scrape.")
def main(search_by, page_from, page_count):
    """Main function to run the scraper."""
    google_search.collect_data(
        search_by=search_by, page_from=page_from, page_count=page_count
    )
    scraper_links.scrap_links(
        search_by=search_by, page_from=page_from, page_count=page_count
    )


if __name__ == "__main__":
    main()
