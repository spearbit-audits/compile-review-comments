# Compile review comments from a Spearbit audit GitHub repository

GitHub often has performance issues if the number of review comments get to large numbers. This script collects review comments from a pull request using the GitHub API and compiles it into a markdown file. The repository and the pull request number can be [configured](#configuration).

## Requirements

[PyGithub](https://pypi.org/project/PyGithub/)

```bash
pip install --user pygithub
```

## Configuration

You will need to generate a personal access token that can access private repositories. [GitHub docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Check the "repo" option: full control of private repositories.

After that update the [`config.py`](./config.py) file locally with the token and a reference to the GithHub repository as well as the pull request. 

## Running

```bash
python3 compile.py
```

The file `[Repo-Name]-pr-[number].md` would contain the generated markdown report.

## Notes

- The review comments can be added or edited and the markdown report can be regenerated.
