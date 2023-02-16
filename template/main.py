import argparse
import tweetcounter


def main(file, term):
    tweets = tweetcounter.loadtweets(file)
    results = tweetcounter.searchtweets(tweets, term)

    print(results)

    count = tweetcounter.counttweets(results)

    print(f'''There are {count} tweets with the word {term}''')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--term", type=str, required=True, help="Pass in a term to find"
    )
    parser.add_argument("--file", type=str, required=True, help="Pass in a file to use")

    args = parser.parse_args()

    main(args.file, args.term)
