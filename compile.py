"""A simple script that collects issues from a repo and generate a markdown
file (Report.md).

A personal access token will need to be configured. Also the repo name will
need to be provided. Add these in `config.py`.

Requirements: pygithub.

`pip install --user pygithub`

"""
from github import Github
from diff import Diff
from review_comment import ReviewComment

import config

github = Github(config.TOKEN)
repo = github.get_repo(config.REPO)
pull_request = repo.get_pull(config.PR)

review_comments_dict : {str: {Diff: [ReviewComment]}} = {}

def clean_endings(body: str) -> str:
    """Cleans Windows line endings"""
    return body.replace("\r\n", "\n")

for review in pull_request.get_review_comments():
    diff = Diff(review.diff_hunk)
    review_comment = ReviewComment(review.user.login, review.body, review.html_url)
    if review.path not in review_comments_dict:
        review_comments_dict[review.path] = {
            diff :
            [review_comment]
        }
    elif diff in review_comments_dict[review.path]:
        review_comments_dict[review.path][diff].append(review_comment)
    else:
        review_comments_dict[review.path][diff] = [review_comment]

with open(f"{config.REPO.split('/')[-1]}-pr-{config.PR}.md", "w") as report:
    for fname in review_comments_dict:
        report.write(f"# {fname}\n\n")
        for diff in review_comments_dict[fname]:
            report.write(f"## L{diff.positions[0]}-{diff.positions[1]}\n\n")
            report.write(f"```diff\n{diff.diff_string}\n```\n\n")
            for review_comment in review_comments_dict[fname][diff]:
                report.write(f"[{review_comment.author}]({review_comment.url}): {review_comment.body}\n\n")

    general_comments = pull_request.get_issue_comments()
    if general_comments.totalCount != 0:
        report.write("# General comments\n\n")
        for comment in general_comments:
            report.write(f"[{comment.user.login}]({comment.html_url}): {clean_endings(comment.body)}\n\n")
