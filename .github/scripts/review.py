import os
import anthropic
import requests

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
changed_files = os.environ["CHANGED_FILES"].strip().split()

for filepath in changed_files:
    if not os.path.exists(filepath):
        continue

    with open(filepath) as f:
        code = f.read()

    # Get the review from Claude
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""Review this NeetCode/LeetCode solution:

```python
{code}
```

Provide:
1. Time and space complexity
2. Edge cases that may be unhandled
3. Pythonic improvements
4. The canonical approach for this problem type, if mine differs
5. One key insight to internalize for similar problems

Be concise."""
        }]
    )

    review = message.content[0].text

    # Post as a commit comment via GitHub API
    comment_body = f"## 🤖 Claude Review: `{filepath}`\n\n{review}"
    requests.post(
        f"https://api.github.com/repos/{os.environ['REPO']}/commits/{os.environ['COMMIT_SHA']}/comments",
        headers={
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "Accept": "application/vnd.github+json"
        },
        json={"body": comment_body}
    )
    print(f"Posted review for {filepath}")
