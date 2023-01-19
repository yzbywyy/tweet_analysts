from Scweet.scweet import scrape


def sctweet(target_lis, mode_str, start_date_str, end_date_str, save_dir_name):
    data = scrape(words=target_lis,
                  since=start_date_str, until=end_date_str,
                  from_account=None,
                  interval=1, headless=True, display_type=mode_str, save_images=False,
                  proxy="127.0.0.1:7890", save_dir=save_dir_name,
                  resume=False, filter_replies=True, proximity=True)
    return [data, save_dir_name]


if __name__ == '__main__':
    print("Hello, World!")
