import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    num_pages = len(corpus)
    probabilities = dict()

    links = corpus[page]
    if links:
        for p in corpus:
            probabilities[p] = (1 - damping_factor) / num_pages
        for linked_page in links:
            probabilities[linked_page] += damping_factor / len(links)
    else:
        # No outgoing links: assume it links to every page
        for p in corpus:
            probabilities[p] = 1 / num_pages

    return probabilities


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_rank = {page: 0 for page in corpus}
    page = random.choice(list(corpus.keys()))

    for _ in range(n):
        page_rank[page] += 1
        distribution = transition_model(corpus, page, damping_factor)
        page = random.choices(
            population=list(distribution.keys()),
            weights=list(distribution.values()),
            k=1
        )[0]

    total = sum(page_rank.values())
    for page in page_rank:
        page_rank[page] /= total

    return page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    tolerance = 0.001
    num_pages = len(corpus)
    ranks = {page: 1 / num_pages for page in corpus}

    # Deal with pages that have no links
    no_link_pages = {page for page in corpus if len(corpus[page]) == 0}
    for page in no_link_pages:
        corpus[page] = set(corpus.keys())
    
    converged = False
    while not converged:
        new_ranks = {}
        for page in corpus:
            total = 0
            for potential_linker in corpus:
                if page in corpus[potential_linker]:
                    total += ranks[potential_linker] / len(corpus[potential_linker])
            new_rank = ((1 - damping_factor) / num_pages) + (damping_factor * total)
            new_ranks[page] = new_rank

        converged = all(
            abs(new_ranks[page] - ranks[page]) < tolerance for page in corpus
        )
        ranks = new_ranks

    # Normalize to ensure sum is exactly 1
    total = sum(ranks.values())
    for page in ranks:
        ranks[page] /= total

    return ranks


if __name__ == "__main__":
    main()
