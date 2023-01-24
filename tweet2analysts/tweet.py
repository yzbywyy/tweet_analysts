from Scweet.scweet import scrape
import sys


def sctweet(interval_day, search_mode, target_lis, hash_tag, mode_str, start_date_str, end_date_str, save_dir_name):
    if search_mode == 0:
        data = scrape(words=target_lis,
                      since=start_date_str, until=end_date_str,
                      from_account=None,
                      interval=interval_day, headless=True, display_type=mode_str, save_images=False,
                      proxy="127.0.0.1:7890", save_dir=save_dir_name,
                      resume=False, filter_replies=True, proximity=True)
    else:
        data = scrape(hashtag=hash_tag,
                      since=start_date_str, until=end_date_str,
                      from_account=None,
                      interval=interval_day, headless=True, display_type=mode_str, save_images=False,
                      proxy="127.0.0.1:7890", save_dir=save_dir_name,
                      resume=False, filter_replies=True, proximity=True)
    sys.sleep(1)
    return [data, save_dir_name]


if __name__ == '__main__':
    print("Hello, World!")
