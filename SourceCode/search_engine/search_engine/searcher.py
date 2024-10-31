from whoosh.qparser import QueryParser
from whoosh.index import open_dir
from whoosh.query import NumericRange
import re
from termcolor import colored
import time


# Highlight the matching snippets
def highlight_snippet(snippet):
    # Whoosh uses <b></b> to bold the matching snippets, which only works in html
    # Remove the <b></b> tags, and use termcolor to highlight the matching snippets
    pattern = re.compile(r"<b[^>]*>(.*?)</b>", re.IGNORECASE)
    snippet_colored = pattern.sub(lambda m: colored(m.group(1), "yellow", attrs=["bold"]), snippet)
    return snippet_colored


# Execute keyword search (business name or review text)
def keyword_search(index_dir, field, query_string, top_n=10):
    # Record the start time
    start_time = time.time()
    # Open the index directory
    index = open_dir(index_dir)
    with index.searcher() as searcher:
        # Execute the search
        query = QueryParser(field, index.schema).parse(query_string)
        results = searcher.search(query, limit=top_n)
        # Extract useful information from results
        outputs = []
        for i, result in enumerate(results):
            # Get the matching snippets
            snippet = result.highlights(field)
            # Highlight
            snippet_colored = highlight_snippet(snippet)
            outputs.append({
                "rank": i + 1,
                "score": result.score,
                "docID": result.docnum,
                "snippet": snippet_colored,
            })
        # Record the time taken to process a query
        elapsed_time = time.time() - start_time
        return outputs, elapsed_time


# Execute geospatial search (bounding box)
def geospatial_search(index_dir, min_lat, max_lat, min_lon, max_lon, top_n=10):
    start_time = time.time()
    index = open_dir(index_dir)
    with index.searcher() as searcher:
        # Define the bounding box
        lat_range = NumericRange("latitude", min_lat, max_lat)
        lon_range = NumericRange("longitude", min_lon, max_lon)
        # Create the query
        query = lat_range & lon_range
        results = searcher.search(query, limit=top_n)
        outputs = []
        for i, result in enumerate(results):
            outputs.append({
                "rank": i + 1,
                "score": result.score,
                "docID": result.docnum,
                "name": result["name"],
                "latitude": result["latitude"],
                "longitude": result["longitude"]
            })
        elapsed_time = time.time() - start_time
        return outputs, elapsed_time
